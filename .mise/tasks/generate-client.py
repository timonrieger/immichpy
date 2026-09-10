#!/usr/bin/env -S uv run --script
# fmt: off
#MISE description="Generate Immich API client"
# fmt: on
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "openapi-generator-cli[jdk4py]==7.25.0",
# ]
# ///

from __future__ import annotations

import ast
import os
import shutil
import subprocess  # nosec: B404
from pathlib import Path


def project_root() -> Path:
    # This file lives at .mise/tasks/generate-client.py
    return Path(__file__).resolve().parents[2]


def openapi_url(ref: str) -> str:
    return (
        "https://raw.githubusercontent.com/immich-app/immich/"
        f"{ref}/open-api/immich-openapi-specs.json"
    )


def rewrite_imports_in_tree(root: Path) -> int:
    """
    Rewrite OpenAPI generator absolute imports:
      from generated...  -> from immichpy.client.generated...
      import generated... -> import immichpy.client.generated...

    Also swap `re` for the `regex` package, since spec patterns use `\\p{...}`
    Unicode property escapes, which Python's `re` cannot compile.
    """
    replacements: list[tuple[str, str]] = [
        ("from generated.", "from immichpy.client.generated."),
        ("from generated ", "from immichpy.client.generated "),
        ("import generated.", "import immichpy.client.generated."),
        ("import generated", "import immichpy.client.generated"),
        ("klass = getattr(generated", "klass = getattr(immichpy.client.generated"),
        ("import re  # noqa: F401", "import regex as re  # noqa: F401"),
    ]

    changed = 0
    for path in root.rglob("*.py"):
        text = path.read_text(encoding="utf-8")
        new_text = text
        for old, new in replacements:
            new_text = new_text.replace(old, new)
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

    if client_dir.exists():
        print("Deleting existing generated client folder:", client_dir)
        shutil.rmtree(client_dir)

    generator_cmd = [
        "openapi-generator-cli",
        "generate",
        "-i",
        url,
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
