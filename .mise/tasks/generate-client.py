#!/usr/bin/env -S uv run --script
# fmt: off
#MISE description="Generate Immich API client"
# fmt: on
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "openapi-generator-cli[jdk4py]==7.26.0",
# ]
# ///

from __future__ import annotations

import ast
import json
import os
import re
import shutil
import subprocess  # nosec: B404
import tempfile
import urllib.request
from pathlib import Path


def project_root() -> Path:
    # This file lives at .mise/tasks/generate-client.py
    return Path(__file__).resolve().parents[2]


def openapi_url(ref: str) -> str:
    return (
        "https://raw.githubusercontent.com/immich-app/immich/"
        f"{ref}/open-api/immich-openapi-specs.json"
    )


# `re` cannot compile the unicode email pattern, and the uuid/date patterns only
# repeat the field's type (stricter: v4-only UUIDs). Drop them, server validates anyways.
PATTERN_FREE_FORMATS = {"email", "uuid", "date-time", "date"}


def drop_format_patterns(schema: dict[str, object]) -> dict[str, object]:
    if (
        isinstance(schema.get("format"), str)
        and schema["format"] in PATTERN_FREE_FORMATS
    ):
        schema.pop("pattern", None)
    return schema


# Newer Immich servers add enum values in non-breaking releases; keep them as
# pseudo-members instead of failing to parse the whole response.
ENUM_MISSING_METHOD = """

    @classmethod
    def _missing_(cls, value: object) -> Self | None:
        if not isinstance(value, cls._member_type_):
            return None
        member = cls._member_type_.__new__(cls, value)
        member._name_ = str(value)
        member._value_ = value
        return member
"""

# anyOf/oneOf wrappers only (de)serialize `actual_instance` in `from_json`/`to_dict`; plain
# `model_validate` drops raw values and `model_dump` returns the wrapper's own fields.
WRAPPER_RAW_METHODS = """    @model_validator(mode="before")
    @classmethod
    def _from_raw(cls, data: Any) -> Any:
        if isinstance(data, dict) and "actual_instance" not in data:
            return {"actual_instance": cls.from_dict(data).actual_instance}
        return data

    @model_serializer
    def _to_raw(self) -> Any:
        return self.actual_instance

    def __init__(self, *args, **kwargs) -> None:"""


# `%z` renders +0000, but the server requires Z or +00:00.
# TODO: drop once https://github.com/OpenAPITools/openapi-generator/pull/25098
# is released and generate-client uses that openapi-generator-cli version
DATETIME_QUERY_FORMAT = re.compile(
    r"\.strftime\(\s*self\.api_client\.configuration\.datetime_format\s*\)"
)


def rewrite_imports_in_tree(root: Path) -> int:
    """
    Rewrite OpenAPI generator absolute imports:
      from generated...  -> from immichpy.client.generated...
      import generated... -> import immichpy.client.generated...

    Also swap `dateutil` for `fromisoformat`, which parses ISO 8601 since 3.11,
    serialize datetime query params with `isoformat`, make enums accept unknown values,
    and let anyOf/oneOf wrappers validate and dump raw values.
    """
    replacements: list[tuple[str, str]] = [
        ("from generated.", "from immichpy.client.generated."),
        ("from generated ", "from immichpy.client.generated "),
        ("import generated.", "import immichpy.client.generated."),
        ("import generated", "import immichpy.client.generated"),
        ("klass = getattr(generated", "klass = getattr(immichpy.client.generated"),
        ("from dateutil.parser import parse\n", ""),
        ("parse(string).date()", "datetime.datetime.fromisoformat(string).date()"),
        ("parse(string)", "datetime.datetime.fromisoformat(string)"),
        (
            "return cls(json.loads(json_str))\n",
            "return cls(json.loads(json_str))\n" + ENUM_MISSING_METHOD,
        ),
        ("    def __init__(self, *args, **kwargs) -> None:", WRAPPER_RAW_METHODS),
        (
            "from typing_extensions import Literal, Self\n",
            "from typing_extensions import Literal, Self\nfrom pydantic import model_serializer, model_validator\n",
        ),
    ]

    changed = 0
    for path in root.rglob("*.py"):
        text = path.read_text(encoding="utf-8")
        new_text = text
        for old, new in replacements:
            new_text = new_text.replace(old, new)
        new_text = DATETIME_QUERY_FORMAT.sub(".isoformat()", new_text)
        if new_text != text:
            path.write_text(new_text, encoding="utf-8")
            changed += 1
    return changed


LAZY_INIT_TEMPLATE = """

from typing import TYPE_CHECKING

if TYPE_CHECKING:
{type_checking_imports}

_LAZY_IMPORTS: dict[str, tuple[str, str]] = {{
{mapping}
}}


def __getattr__(name: str) -> object:
    try:
        module, attr = _LAZY_IMPORTS[name]
    except KeyError:
        raise AttributeError(
            f"module {{__name__!r}} has no attribute {{name!r}}"
        ) from None
    from importlib import import_module

    value = getattr(import_module(module), attr)
    globals()[name] = value
    return value
"""


def make_init_lazy(path: Path) -> None:
    """
    Rewrite a generated __init__.py so its re-exports resolve lazily (PEP 562):
    the eager `from immichpy.client.generated... import X` block moves under
    TYPE_CHECKING and a module __getattr__ imports each name on first access.
    """
    source = path.read_text(encoding="utf-8")
    lines = source.splitlines()
    lazy: dict[str, tuple[str, str]] = {}
    drop: set[int] = set()
    import_lines: list[str] = []
    for node in ast.parse(source).body:
        if not (
            isinstance(node, ast.ImportFrom)
            and node.module is not None
            and node.module.startswith("immichpy.client.generated")
        ):
            continue
        for alias in node.names:
            lazy[alias.asname or alias.name] = (node.module, alias.name)
        end_lineno = node.end_lineno or node.lineno
        import_lines.extend(lines[node.lineno - 1 : end_lineno])
        drop.update(range(node.lineno - 1, end_lineno))

    kept = "\n".join(line for i, line in enumerate(lines) if i not in drop)
    lazy_block = LAZY_INIT_TEMPLATE.format(
        type_checking_imports="\n".join(f"    {line}" for line in import_lines),
        mapping="\n".join(
            f'    "{name}": ("{module}", "{attr}"),'
            for name, (module, attr) in sorted(lazy.items())
        ),
    )
    path.write_text(kept.rstrip() + "\n" + lazy_block.lstrip("\n"), encoding="utf-8")


def main() -> int:
    root = project_root()
    out_dir = root / "immichpy" / "client"
    client_dir = out_dir / "generated"

    url = openapi_url(os.environ.get("IMMICH_OPENAPI_REF", "main"))
    print(f"Fetching OpenAPI spec from: {url}")
    with urllib.request.urlopen(url) as response:  # nosec: B310
        spec = json.load(response, object_hook=drop_format_patterns)
    spec_file = Path(tempfile.mkdtemp()) / "immich-openapi-specs.json"
    spec_file.write_text(json.dumps(spec), encoding="utf-8")

    if client_dir.exists():
        print("Deleting existing generated client folder:", client_dir)
        shutil.rmtree(client_dir)

    generator_cmd = [
        "openapi-generator-cli",
        "generate",
        "-i",
        str(spec_file),
        "-g",
        "python",
        "--package-name",
        "generated",
        "--global-property",
        "supportingFiles,models,apis",
        "--additional-properties",
        "pipPackageName=immichpy",
        "-o",
        str(out_dir),
        "--openapi-generator-ignore-list",
        "setup.py,setup.cfg,pyproject.toml,tox.ini,py.typed,.gitignore,.gitlab-ci.yml,.github/,git_push.sh,test/,docs/,.travis.yml,test-requirements.txt,requirements.txt,README.md,.openapi-generator-ignore",
        "--minimal-update",
        "--library",
        "asyncio",
    ]
    subprocess.run(generator_cmd, cwd=str(root), check=True)  # nosec: B603

    if not client_dir.exists():
        print(f"Expected generated directory not found: {client_dir}")
        return 1

    changed = rewrite_imports_in_tree(client_dir)
    print(f"Rewrote imports in {changed} files under {client_dir}")

    for init in (
        client_dir / "__init__.py",
        client_dir / "api" / "__init__.py",
        client_dir / "models" / "__init__.py",
    ):
        make_init_lazy(init)
        print(f"Made re-exports lazy in {init}")
    print("Done.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
