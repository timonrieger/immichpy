from __future__ import annotations

from email.message import Message
from mimetypes import guess_extension
from pathlib import Path
from typing import Optional


def filename_from_headers(
    headers: dict[str, str] | None, *, fallback_base: str
) -> Optional[str]:
    """
    Derive a filename from response headers.

    Order of precedence:
    - Content-Disposition filename (if present)
      - if it has no extension, append an extension derived from Content-Type (if available)
    - Content-Type derived extension + `fallback_base`

    :param headers: The response headers.
    :param fallback_base: The filename without extension if we cannot derive the original filename from the Content-Disposition header.

    :returns: The derived filename or None if we cannot derive the filename from the headers.
    """
    if not headers:
        return None

    def h(name: str) -> Optional[str]:
        return next((v for k, v in headers.items() if k.lower() == name.lower()), None)

    cd_name: Optional[str] = None
    if cd := h("content-disposition"):
        msg = Message()
        msg["content-disposition"] = cd
        if filename := msg.get_filename():
            cd_name = Path(filename).name

    ext = (
        guess_extension(ct.partition(";")[0].strip())
        if (ct := h("content-type"))
        else None
    )

    # Content-Disposition wins for the base name; Content-Type is the safety net for the extension.
    if cd_name:
        return cd_name if Path(cd_name).suffix or not ext else f"{cd_name}{ext}"

    return f"{fallback_base}{ext}" if ext else None


def resolve_output_filename(
    headers: dict[str, str] | None,
    *,
    name: Optional[str] = None,
    default_base: str,
    default_ext: Optional[str] = None,
) -> str:
    """
    Resolve an output filename by selecting a base name and an extension.

    Base name precedence:
    - user-supplied `name`
    - Content-Disposition filename
    - `default_base`

    Extension precedence:
    - `default_ext` (if provided; overrides any other extension)
    - extension present on the chosen base name (e.g. from Content-Disposition)
    - Content-Type derived extension
    - none

    :param headers: The response headers.
    :param name: The user-supplied name.
    :param default_base: The default base name, used when no user/header filename can be derived.
    :param default_ext: The default extension (must start with `.`), used when you want to force a specific extension (e.g. `.zip`).

    :returns: The resolved filename.
    """
    if default_ext and not default_ext.startswith("."):
        raise ValueError("default_ext must start with '.' (e.g. '.zip')")

    base = default_base
    ext = None

    header_path = None
    if _ := filename_from_headers(headers, fallback_base=default_base):
        header_path = Path(_)

    # Base name
    if name:
        base = Path(name).stem
    elif header_path:
        base = header_path.stem

    # Extension
    if default_ext:
        ext = default_ext
    elif header_path:
        ext = header_path.suffix
    return f"{base}{ext}" if ext else base
