"""Generated CLI commands for Asset files tag (auto-generated, do not edit)."""

from __future__ import annotations

from typing import TYPE_CHECKING, Literal
from uuid import UUID

import typer

if TYPE_CHECKING:
    from immichpy import AsyncClient

from immichpy.cli.runtime import print_response, run_command
from immichpy.client.generated.models import AssetFileType

app = typer.Typer(
    help="""An asset file is a file associated with an asset, including edited versions, thumbnails, etc.\n\n[link=https://api.immich.app/endpoints/asset-files]Immich API documentation[/link]"""
)


@app.command("delete-asset-file", deprecated=False, rich_help_panel="API commands")
def delete_asset_file(
    ctx: typer.Context,
    id: UUID = typer.Argument(..., help=r""""""),
) -> None:
    """Delete an asset file

    [link=https://api.immich.app/endpoints/asset-files/deleteAssetFile]Immich API documentation[/link]
    """
    kwargs = {}
    kwargs["id"] = id
    client: AsyncClient = ctx.obj["client"]
    result = run_command(client.asset_files.delete_asset_file, ctx=ctx, **kwargs)
    print_response(result, ctx=ctx)


@app.command("download-asset-file", deprecated=False, rich_help_panel="API commands")
def download_asset_file(
    ctx: typer.Context,
    id: UUID = typer.Argument(..., help=r""""""),
) -> None:
    """Download an asset file

    [link=https://api.immich.app/endpoints/asset-files/downloadAssetFile]Immich API documentation[/link]
    """
    kwargs = {}
    kwargs["id"] = id
    client: AsyncClient = ctx.obj["client"]
    result = run_command(client.asset_files.download_asset_file, ctx=ctx, **kwargs)
    print_response(result, ctx=ctx)


@app.command("get-asset-file", deprecated=False, rich_help_panel="API commands")
def get_asset_file(
    ctx: typer.Context,
    id: UUID = typer.Argument(..., help=r""""""),
) -> None:
    """Retrieve an asset file

    [link=https://api.immich.app/endpoints/asset-files/getAssetFile]Immich API documentation[/link]
    """
    kwargs = {}
    kwargs["id"] = id
    client: AsyncClient = ctx.obj["client"]
    result = run_command(client.asset_files.get_asset_file, ctx=ctx, **kwargs)
    print_response(result, ctx=ctx)


@app.command("search-asset-files", deprecated=False, rich_help_panel="API commands")
def search_asset_files(
    ctx: typer.Context,
    asset_id: UUID = typer.Option(
        ..., "--asset-id", help=r"""Asset ID to filter files by"""
    ),
    is_edited: Literal["true", "false"] | None = typer.Option(
        None, "--is-edited", help=r"""The file was generated from an edit"""
    ),
    is_progressive: Literal["true", "false"] | None = typer.Option(
        None, "--is-progressive", help=r"""The file is a progressively encoded JPEG"""
    ),
    is_transparent: Literal["true", "false"] | None = typer.Option(
        None, "--is-transparent", help=r"""The file is transparent"""
    ),
    type: AssetFileType | None = typer.Option(
        None, "--type", help=r"""Filter by type of file"""
    ),
) -> None:
    """Search asset files

    [link=https://api.immich.app/endpoints/asset-files/searchAssetFiles]Immich API documentation[/link]
    """
    kwargs = {}
    kwargs["asset_id"] = asset_id
    if is_edited is not None:
        kwargs["is_edited"] = is_edited.lower() == "true"
    if is_progressive is not None:
        kwargs["is_progressive"] = is_progressive.lower() == "true"
    if is_transparent is not None:
        kwargs["is_transparent"] = is_transparent.lower() == "true"
    if type is not None:
        kwargs["type"] = type
    client: AsyncClient = ctx.obj["client"]
    result = run_command(client.asset_files.search_asset_files, ctx=ctx, **kwargs)
    print_response(result, ctx=ctx)
