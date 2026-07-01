"""Generated CLI commands for Shared links tag (auto-generated, do not edit)."""

from __future__ import annotations

import typer
from datetime import datetime
from uuid import UUID
from typing import Literal, TYPE_CHECKING

if TYPE_CHECKING:
    from immichpy import AsyncClient

from immichpy.cli.runtime import print_response, run_command, set_nested
from immichpy.client.generated.models import *

app = typer.Typer(
    help="""A shared link is a public url that provides access to a specific album, asset, or collection of assets. A shared link can be protected with a password, include a specific slug, allow or disallow downloads, and optionally include an expiration date.\n\n[link=https://api.immich.app/endpoints/shared-links]Immich API documentation[/link]"""
)


@app.command("add-shared-link-assets", deprecated=False, rich_help_panel="API commands")
def add_shared_link_assets(
    ctx: typer.Context,
    id: UUID = typer.Argument(..., help=r""""""),
    asset_ids: list[UUID] = typer.Option(..., "--asset-ids", help=r"""Asset IDs"""),
) -> None:
    """Add assets to a shared link

    [link=https://api.immich.app/endpoints/shared-links/addSharedLinkAssets]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    kwargs["id"] = id
    set_nested(json_data, ["asset_ids"], asset_ids)
    asset_ids_dto = AssetIdsDto.model_validate(json_data)
    kwargs["asset_ids_dto"] = asset_ids_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client.shared_links.add_shared_link_assets, ctx=ctx, **kwargs)
    print_response(result, ctx=ctx)


@app.command("create-shared-link", deprecated=False, rich_help_panel="API commands")
def create_shared_link(
    ctx: typer.Context,
    album_id: UUID | None = typer.Option(
        None, "--album-id", help=r"""Album ID (for album sharing)"""
    ),
    allow_download: Literal["true", "false"] | None = typer.Option(
        None, "--allow-download", help=r"""Allow downloads"""
    ),
    allow_upload: Literal["true", "false"] | None = typer.Option(
        None, "--allow-upload", help=r"""Allow uploads"""
    ),
    asset_ids: list[UUID] | None = typer.Option(
        None, "--asset-ids", help=r"""Asset IDs (for individual assets)"""
    ),
    description: str | None = typer.Option(
        None, "--description", help=r"""Link description"""
    ),
    expires_at: datetime | None = typer.Option(
        None,
        "--expires-at",
        help=r"""Expiration date

Example: 2024-01-01T00:00:00.000Z""",
    ),
    password: str | None = typer.Option(None, "--password", help=r"""Link password"""),
    show_metadata: Literal["true", "false"] | None = typer.Option(
        None, "--show-metadata", help=r"""Show metadata"""
    ),
    slug: str | None = typer.Option(None, "--slug", help=r"""Custom URL slug"""),
    type: str = typer.Option(..., "--type", help=r"""Shared link type"""),
) -> None:
    """Create a shared link

    [link=https://api.immich.app/endpoints/shared-links/createSharedLink]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    if album_id is not None:
        set_nested(json_data, ["album_id"], album_id)
    if allow_download is not None:
        set_nested(json_data, ["allow_download"], allow_download.lower() == "true")
    if allow_upload is not None:
        set_nested(json_data, ["allow_upload"], allow_upload.lower() == "true")
    if asset_ids is not None:
        set_nested(json_data, ["asset_ids"], asset_ids)
    if description is not None:
        set_nested(json_data, ["description"], description)
    if expires_at is not None:
        set_nested(json_data, ["expires_at"], expires_at)
    if password is not None:
        set_nested(json_data, ["password"], password)
    if show_metadata is not None:
        set_nested(json_data, ["show_metadata"], show_metadata.lower() == "true")
    if slug is not None:
        set_nested(json_data, ["slug"], slug)
    set_nested(json_data, ["type"], type)
    shared_link_create_dto = SharedLinkCreateDto.model_validate(json_data)
    kwargs["shared_link_create_dto"] = shared_link_create_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client.shared_links.create_shared_link, ctx=ctx, **kwargs)
    print_response(result, ctx=ctx)


@app.command("get-all-shared-links", deprecated=False, rich_help_panel="API commands")
def get_all_shared_links(
    ctx: typer.Context,
    album_id: UUID | None = typer.Option(
        None, "--album-id", help=r"""Filter by album ID"""
    ),
    id: UUID | None = typer.Option(None, "--id", help=r"""Filter by shared link ID"""),
) -> None:
    """Retrieve all shared links

    [link=https://api.immich.app/endpoints/shared-links/getAllSharedLinks]Immich API documentation[/link]
    """
    kwargs = {}
    if album_id is not None:
        kwargs["album_id"] = album_id
    if id is not None:
        kwargs["id"] = id
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client.shared_links.get_all_shared_links, ctx=ctx, **kwargs)
    print_response(result, ctx=ctx)


@app.command("get-my-shared-link", deprecated=False, rich_help_panel="API commands")
def get_my_shared_link(
    ctx: typer.Context,
    key: str | None = typer.Option(None, "--key", help=r""""""),
    slug: str | None = typer.Option(None, "--slug", help=r""""""),
) -> None:
    """Retrieve current shared link

    [link=https://api.immich.app/endpoints/shared-links/getMySharedLink]Immich API documentation[/link]
    """
    kwargs = {}
    if key is not None:
        kwargs["key"] = key
    if slug is not None:
        kwargs["slug"] = slug
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client.shared_links.get_my_shared_link, ctx=ctx, **kwargs)
    print_response(result, ctx=ctx)


@app.command("get-shared-link-by-id", deprecated=False, rich_help_panel="API commands")
def get_shared_link_by_id(
    ctx: typer.Context,
    id: UUID = typer.Argument(..., help=r""""""),
) -> None:
    """Retrieve a shared link

    [link=https://api.immich.app/endpoints/shared-links/getSharedLinkById]Immich API documentation[/link]
    """
    kwargs = {}
    kwargs["id"] = id
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client.shared_links.get_shared_link_by_id, ctx=ctx, **kwargs)
    print_response(result, ctx=ctx)


@app.command("remove-shared-link", deprecated=False, rich_help_panel="API commands")
def remove_shared_link(
    ctx: typer.Context,
    id: UUID = typer.Argument(..., help=r""""""),
) -> None:
    """Delete a shared link

    [link=https://api.immich.app/endpoints/shared-links/removeSharedLink]Immich API documentation[/link]
    """
    kwargs = {}
    kwargs["id"] = id
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client.shared_links.remove_shared_link, ctx=ctx, **kwargs)
    print_response(result, ctx=ctx)


@app.command(
    "remove-shared-link-assets", deprecated=False, rich_help_panel="API commands"
)
def remove_shared_link_assets(
    ctx: typer.Context,
    id: UUID = typer.Argument(..., help=r""""""),
    asset_ids: list[UUID] = typer.Option(..., "--asset-ids", help=r"""Asset IDs"""),
) -> None:
    """Remove assets from a shared link

    [link=https://api.immich.app/endpoints/shared-links/removeSharedLinkAssets]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    kwargs["id"] = id
    set_nested(json_data, ["asset_ids"], asset_ids)
    asset_ids_dto = AssetIdsDto.model_validate(json_data)
    kwargs["asset_ids_dto"] = asset_ids_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(
        client.shared_links.remove_shared_link_assets, ctx=ctx, **kwargs
    )
    print_response(result, ctx=ctx)


@app.command("shared-link-login", deprecated=False, rich_help_panel="API commands")
def shared_link_login(
    ctx: typer.Context,
    key: str | None = typer.Option(None, "--key", help=r""""""),
    password: str = typer.Option(
        ...,
        "--password",
        help=r"""Shared link password

Example: password""",
    ),
    slug: str | None = typer.Option(None, "--slug", help=r""""""),
) -> None:
    """Shared link login

    [link=https://api.immich.app/endpoints/shared-links/sharedLinkLogin]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    if key is not None:
        kwargs["key"] = key
    if slug is not None:
        kwargs["slug"] = slug
    set_nested(json_data, ["password"], password)
    shared_link_login_dto = SharedLinkLoginDto.model_validate(json_data)
    kwargs["shared_link_login_dto"] = shared_link_login_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client.shared_links.shared_link_login, ctx=ctx, **kwargs)
    print_response(result, ctx=ctx)


@app.command("update-shared-link", deprecated=False, rich_help_panel="API commands")
def update_shared_link(
    ctx: typer.Context,
    id: UUID = typer.Argument(..., help=r""""""),
    allow_download: Literal["true", "false"] | None = typer.Option(
        None, "--allow-download", help=r"""Allow downloads"""
    ),
    allow_upload: Literal["true", "false"] | None = typer.Option(
        None, "--allow-upload", help=r"""Allow uploads"""
    ),
    description: str | None = typer.Option(
        None, "--description", help=r"""Link description"""
    ),
    expires_at: datetime | None = typer.Option(
        None,
        "--expires-at",
        help=r"""Expiration date

Example: 2024-01-01T00:00:00.000Z""",
    ),
    password: str | None = typer.Option(None, "--password", help=r"""Link password"""),
    show_metadata: Literal["true", "false"] | None = typer.Option(
        None, "--show-metadata", help=r"""Show metadata"""
    ),
    slug: str | None = typer.Option(None, "--slug", help=r"""Custom URL slug"""),
) -> None:
    """Update a shared link

    [link=https://api.immich.app/endpoints/shared-links/updateSharedLink]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    kwargs["id"] = id
    if allow_download is not None:
        set_nested(json_data, ["allow_download"], allow_download.lower() == "true")
    if allow_upload is not None:
        set_nested(json_data, ["allow_upload"], allow_upload.lower() == "true")
    if description is not None:
        set_nested(json_data, ["description"], description)
    if expires_at is not None:
        set_nested(json_data, ["expires_at"], expires_at)
    if password is not None:
        set_nested(json_data, ["password"], password)
    if show_metadata is not None:
        set_nested(json_data, ["show_metadata"], show_metadata.lower() == "true")
    if slug is not None:
        set_nested(json_data, ["slug"], slug)
    shared_link_edit_dto = SharedLinkEditDto.model_validate(json_data)
    kwargs["shared_link_edit_dto"] = shared_link_edit_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client.shared_links.update_shared_link, ctx=ctx, **kwargs)
    print_response(result, ctx=ctx)
