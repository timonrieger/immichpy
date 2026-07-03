#!/usr/bin/env python3
"""Generate API documentation markdown files from client classes."""

from pathlib import Path
import re
import shutil

import rtoml

# Explicit mapping for special cases
SPECIAL_CASES: dict[str, tuple[str, str]] = {
    "api_keys_api": ("APIKeysApi", "API Keys Api"),
    "clip_config": ("CLIPConfig", "CLIP Config"),
    "transcode_hw_accel": ("TranscodeHWAccel", "Transcode HW Accel"),
    "o_auth_callback_dto": ("OAuthCallbackDto", "OAuth Callback Dto"),
    "cq_mode": ("CQMode", "CQ Mode"),
}


def filename_to_title(filename: str) -> str:
    """Convert filename like 'activities_api.py' to 'Activities Api'."""
    name = filename.replace(".py", "")
    if name in SPECIAL_CASES:
        return SPECIAL_CASES[name][1]

    parts = name.split("_")
    return " ".join(part.capitalize() for part in parts)


def filename_to_class_name(filename: str) -> str:
    """Convert filename like 'activities_api.py' to 'ActivitiesApi'.

    Special cases are handled via explicit mapping, otherwise falls back to
    split by underscore, capitalize each part, and join.
    """
    name = filename.replace(".py", "")

    if name in SPECIAL_CASES:
        return SPECIAL_CASES[name][0]

    # Default: split by underscore, capitalize each part, join
    parts = name.split("_")
    return "".join(part.capitalize() for part in parts)


def get_module_path(file_path: Path, project_root: Path) -> str:
    """Convert file path to Python module path."""
    rel_path = file_path.relative_to(project_root)
    module_path = str(rel_path).replace("/", ".").replace(".py", "")
    return module_path


def generate_markdown_content(title: str, module_path: str, class_name: str) -> str:
    """Generate markdown content for a class."""
    return f"""# {title}

::: {module_path}.{class_name}
"""


def process_directory(
    source_dir: Path,
    output_dir: Path,
    project_root: Path,
    file_pattern: str,
) -> int:
    """Process a directory and generate markdown files.

    Returns the number of files generated.
    """
    output_dir.mkdir(parents=True, exist_ok=True)

    files = sorted(source_dir.glob(file_pattern))
    files = [f for f in files if not f.name.startswith("__")]

    for source_file in files:
        filename = source_file.name
        module_path = get_module_path(source_file, project_root)

        title = filename_to_title(filename)
        class_name = filename_to_class_name(filename)
        content = generate_markdown_content(title, module_path, class_name)

        output_file = output_dir / filename.replace(".py", ".md")
        output_file.write_text(content)
        print(f"  Generated: {output_file.relative_to(project_root)}")

    return len(files)


def update_nav(project_root: Path) -> None:
    """Rewrite the API and Models nav arrays in zensical.toml to match the
    reference pages on disk, keeping every other line (comments, curated
    sections, hand-authored root pages) untouched.

    Pages are read from ``docs/client/reference/{api,models,custom}``. Wrapper
    pages (``custom/*_api_wrapped.md``) join the API section; any other custom
    page (e.g. the hand-authored ``upload_result.md``) joins Models. Each
    section is sorted by filename so custom pages land next to their siblings.
    """
    docs_dir = project_root / "docs"
    ref_dir = docs_dir / "client" / "reference"

    def nav_paths(subdir: str) -> list[str]:
        return [
            p.relative_to(docs_dir).as_posix() for p in ref_dir.glob(f"{subdir}/*.md")
        ]

    def nav_key(path: str) -> str:
        return path.rsplit("/", 1)[-1]

    wrapped: list[str] = []
    other: list[str] = []
    for path in nav_paths("custom"):
        bucket = wrapped if nav_key(path).endswith("_api_wrapped.md") else other
        bucket.append(path)

    sections = {
        "API": sorted(nav_paths("api") + wrapped, key=nav_key),
        "Models": sorted(nav_paths("models") + other, key=nav_key),
    }

    config_path = project_root / "zensical.toml"
    text = config_path.read_text()

    item_indent = " " * 16
    close_indent = " " * 12
    for key, paths in sections.items():
        body = "\n".join(f'{item_indent}"{path}",' for path in paths)
        replacement = f"{{ {key} = [\n{body}\n{close_indent}] }},"
        pattern = re.compile(r"\{ " + key + r" = \[.*?\] \},", re.DOTALL)
        # function replacement keeps the splice literal (no backslash/group expansion)
        text = pattern.sub(lambda _: replacement, text, count=1)

    config_path.write_text(text)
    rtoml.load(config_path)  # fail loudly if the splice produced invalid TOML
    print(
        f"  Updated nav: {len(sections['API'])} API, {len(sections['Models'])} models"
    )


def main():
    """Generate markdown files for all client classes."""
    project_root = Path(__file__).parent.parent.parent
    client_dir = project_root / "immichpy" / "client"
    docs_ref_dir = project_root / "docs" / "client" / "reference"

    total_generated = 0

    # 1. generated/api/ -> docs/client/reference/api/
    print("\nProcessing generated/api/...")
    shutil.rmtree(docs_ref_dir / "api", ignore_errors=True)
    count = process_directory(
        source_dir=client_dir / "generated" / "api",
        output_dir=docs_ref_dir / "api",
        project_root=project_root,
        file_pattern="*_api.py",
    )
    total_generated += count
    print(f"  {count} API files")

    # 2. generated/models/ -> docs/client/reference/models/
    print("\nProcessing generated/models/...")
    shutil.rmtree(docs_ref_dir / "models", ignore_errors=True)
    count = process_directory(
        source_dir=client_dir / "generated" / "models",
        output_dir=docs_ref_dir / "models",
        project_root=project_root,
        file_pattern="*.py",
    )
    total_generated += count
    print(f"  {count} model files")

    # 3. wrapper/ -> docs/client/reference/api
    print("\nProcessing wrapper/...")
    # don't delete the directory since there might be other custom files
    count = process_directory(
        source_dir=client_dir / "wrapper",
        output_dir=docs_ref_dir / "custom",
        project_root=project_root,
        file_pattern="*.py",
    )
    total_generated += count
    print(f"  {count} wrapper files")

    # 4. Sync the API and Models nav arrays in zensical.toml
    print("\nUpdating zensical.toml nav...")
    update_nav(project_root)

    print(f"\nTotal: {total_generated} documentation files generated")


if __name__ == "__main__":
    main()
