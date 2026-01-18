"""CLI wrapper commands for DownloadApiWrapped convenience methods."""

from __future__ import annotations

from pathlib import Path

import typer

from immich.cli.commands import download as download_commands
from immich.cli.runtime import (
    print_response,
    run_command,
    set_nested,
)

# Reuse the existing app from the generated commands
app = download_commands.app


@app.command("download-archive-to-file", rich_help_panel="Custom commands")
def download_archive_to_file(
    ctx: typer.Context,
    out_dir: Path = typer.Argument(
        ..., help="Output directory for the downloaded ZIP archives"
    ),
    key: str | None = typer.Option(
        None, "--key", help="Public share key (last path segment of /share/<key>)"
    ),
    slug: str | None = typer.Option(
        None, "--slug", help="Public share slug (last path segment of /s/<slug>)"
    ),
    show_progress: bool = typer.Option(
        True,
        "--show-progress",
        help="Show progress bars (per-archive bytes + overall archive count)",
    ),
    album_id: str | None = typer.Option(None, "--albumId", help="Album ID to download"),
    archive_size: int | None = typer.Option(
        None, "--archiveSize", help="Archive size limit in bytes"
    ),
    asset_ids: list[str] | None = typer.Option(
        None, "--assetIds", help="Asset IDs to download"
    ),
    user_id: str | None = typer.Option(
        None, "--userId", help="User ID to download assets from"
    ),
) -> None:
    """Download one or more asset archives and save them to ZIP files.

    Downloads archives sequentially (not in parallel) to avoid overloading the server.
    The download_info parameter can be provided via --json or using dotted flags.
    """
    json_data = {}
    if album_id is not None:
        set_nested(json_data, ["albumId"], album_id)
    if archive_size is not None:
        set_nested(json_data, ["archiveSize"], archive_size)
    if asset_ids is not None:
        set_nested(json_data, ["assetIds"], asset_ids)
    if user_id is not None:
        set_nested(json_data, ["userId"], user_id)
    from immich.client.models.download_info_dto import DownloadInfoDto

    download_info = DownloadInfoDto.model_validate(json_data)

    kwargs = {}
    kwargs["download_info"] = download_info
    kwargs["out_dir"] = out_dir
    kwargs["key"] = key
    kwargs["slug"] = slug
    kwargs["show_progress"] = show_progress

    client = ctx.obj["client"]
    result = run_command(client, client.download, "download_archive_to_file", **kwargs)
    format_mode = ctx.obj.get("format")
    print_response(result, format_mode)
