"""Generated CLI commands for Albums tag (auto-generated, do not edit)."""

from __future__ import annotations

import typer
from uuid import UUID
from typing import Literal, TYPE_CHECKING

if TYPE_CHECKING:
    from immichpy import AsyncClient

from immichpy.cli.runtime import (
    parse_json_options,
    print_response,
    run_command,
    set_nested,
)
from immichpy.client.generated.models import *

app = typer.Typer(
    help="""An album is a collection of assets that can be shared with other users or via shared links.\n\n[link=https://api.immich.app/endpoints/albums]Immich API documentation[/link]"""
)


@app.command("add-assets-to-album", deprecated=False, rich_help_panel="API commands")
def add_assets_to_album(
    ctx: typer.Context,
    id: UUID = typer.Argument(..., help=r""""""),
    ids: list[UUID] = typer.Option(..., "--ids", help=r"""IDs to process"""),
) -> None:
    """Add assets to an album

    [link=https://api.immich.app/endpoints/albums/addAssetsToAlbum]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    kwargs["id"] = id
    set_nested(json_data, ["ids"], ids)
    bulk_ids_dto = BulkIdsDto.model_validate(json_data)
    kwargs["bulk_ids_dto"] = bulk_ids_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client.albums.add_assets_to_album, ctx=ctx, **kwargs)
    print_response(result, ctx=ctx)


@app.command("add-assets-to-albums", deprecated=False, rich_help_panel="API commands")
def add_assets_to_albums(
    ctx: typer.Context,
    album_ids: list[UUID] = typer.Option(..., "--album-ids", help=r"""Album IDs"""),
    asset_ids: list[UUID] = typer.Option(..., "--asset-ids", help=r"""Asset IDs"""),
) -> None:
    """Add assets to albums

    [link=https://api.immich.app/endpoints/albums/addAssetsToAlbums]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    set_nested(json_data, ["album_ids"], album_ids)
    set_nested(json_data, ["asset_ids"], asset_ids)
    albums_add_assets_dto = AlbumsAddAssetsDto.model_validate(json_data)
    kwargs["albums_add_assets_dto"] = albums_add_assets_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client.albums.add_assets_to_albums, ctx=ctx, **kwargs)
    print_response(result, ctx=ctx)


@app.command("add-users-to-album", deprecated=False, rich_help_panel="API commands")
def add_users_to_album(
    ctx: typer.Context,
    id: UUID = typer.Argument(..., help=r""""""),
    album_users: list[str] = typer.Option(
        ...,
        "--album-users",
        help=r"""Album users to add

As a JSON string with keys: role (string), userId (string)""",
    ),
) -> None:
    """Share album with users

    [link=https://api.immich.app/endpoints/albums/addUsersToAlbum]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    kwargs["id"] = id
    value_album_users = parse_json_options(album_users, "--album-users", ctx=ctx)
    set_nested(json_data, ["album_users"], value_album_users)
    add_users_dto = AddUsersDto.model_validate(json_data)
    kwargs["add_users_dto"] = add_users_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client.albums.add_users_to_album, ctx=ctx, **kwargs)
    print_response(result, ctx=ctx)


@app.command("create-album", deprecated=False, rich_help_panel="API commands")
def create_album(
    ctx: typer.Context,
    album_name: str = typer.Option(..., "--album-name", help=r"""Album name"""),
    album_users: list[str] | None = typer.Option(
        None,
        "--album-users",
        help=r"""Album users

As a JSON string with keys: role (string), userId (string)""",
    ),
    asset_ids: list[UUID] | None = typer.Option(
        None, "--asset-ids", help=r"""Initial asset IDs"""
    ),
    description: str | None = typer.Option(
        None, "--description", help=r"""Album description"""
    ),
) -> None:
    """Create an album

    [link=https://api.immich.app/endpoints/albums/createAlbum]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    set_nested(json_data, ["album_name"], album_name)
    if album_users is not None:
        value_album_users = parse_json_options(album_users, "--album-users", ctx=ctx)
        set_nested(json_data, ["album_users"], value_album_users)
    if asset_ids is not None:
        set_nested(json_data, ["asset_ids"], asset_ids)
    if description is not None:
        set_nested(json_data, ["description"], description)
    create_album_dto = CreateAlbumDto.model_validate(json_data)
    kwargs["create_album_dto"] = create_album_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client.albums.create_album, ctx=ctx, **kwargs)
    print_response(result, ctx=ctx)


@app.command("delete-album", deprecated=False, rich_help_panel="API commands")
def delete_album(
    ctx: typer.Context,
    id: UUID = typer.Argument(..., help=r""""""),
) -> None:
    """Delete an album

    [link=https://api.immich.app/endpoints/albums/deleteAlbum]Immich API documentation[/link]
    """
    kwargs = {}
    kwargs["id"] = id
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client.albums.delete_album, ctx=ctx, **kwargs)
    print_response(result, ctx=ctx)


@app.command("get-album-info", deprecated=False, rich_help_panel="API commands")
def get_album_info(
    ctx: typer.Context,
    id: UUID = typer.Argument(..., help=r""""""),
    key: str | None = typer.Option(None, "--key", help=r""""""),
    slug: str | None = typer.Option(None, "--slug", help=r""""""),
) -> None:
    """Retrieve an album

    [link=https://api.immich.app/endpoints/albums/getAlbumInfo]Immich API documentation[/link]
    """
    kwargs = {}
    kwargs["id"] = id
    if key is not None:
        kwargs["key"] = key
    if slug is not None:
        kwargs["slug"] = slug
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client.albums.get_album_info, ctx=ctx, **kwargs)
    print_response(result, ctx=ctx)


@app.command("get-album-map-markers", deprecated=False, rich_help_panel="API commands")
def get_album_map_markers(
    ctx: typer.Context,
    id: UUID = typer.Argument(..., help=r""""""),
    key: str | None = typer.Option(None, "--key", help=r""""""),
    slug: str | None = typer.Option(None, "--slug", help=r""""""),
) -> None:
    """Retrieve album map markers

    [link=https://api.immich.app/endpoints/albums/getAlbumMapMarkers]Immich API documentation[/link]
    """
    kwargs = {}
    kwargs["id"] = id
    if key is not None:
        kwargs["key"] = key
    if slug is not None:
        kwargs["slug"] = slug
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client.albums.get_album_map_markers, ctx=ctx, **kwargs)
    print_response(result, ctx=ctx)


@app.command("get-album-statistics", deprecated=False, rich_help_panel="API commands")
def get_album_statistics(
    ctx: typer.Context,
) -> None:
    """Retrieve album statistics

    [link=https://api.immich.app/endpoints/albums/getAlbumStatistics]Immich API documentation[/link]
    """
    kwargs = {}
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client.albums.get_album_statistics, ctx=ctx, **kwargs)
    print_response(result, ctx=ctx)


@app.command("get-all-albums", deprecated=False, rich_help_panel="API commands")
def get_all_albums(
    ctx: typer.Context,
    asset_id: UUID | None = typer.Option(
        None,
        "--asset-id",
        help=r"""Filter albums containing this asset ID (ignores other parameters)""",
    ),
    id: UUID | None = typer.Option(None, "--id", help=r"""Album ID"""),
    is_owned: Literal["true", "false"] | None = typer.Option(
        None,
        "--is-owned",
        help=r"""Filter by ownership: true = only owned, false = only shared-with-me, undefined = no filter""",
    ),
    is_shared: Literal["true", "false"] | None = typer.Option(
        None,
        "--is-shared",
        help=r"""Filter by shared status: true = only shared, false = not shared, undefined = no filter""",
    ),
    name: str | None = typer.Option(
        None, "--name", help=r"""Album name (exact match)"""
    ),
) -> None:
    """List all albums

    [link=https://api.immich.app/endpoints/albums/getAllAlbums]Immich API documentation[/link]
    """
    kwargs = {}
    if asset_id is not None:
        kwargs["asset_id"] = asset_id
    if id is not None:
        kwargs["id"] = id
    if is_owned is not None:
        kwargs["is_owned"] = is_owned.lower() == "true"
    if is_shared is not None:
        kwargs["is_shared"] = is_shared.lower() == "true"
    if name is not None:
        kwargs["name"] = name
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client.albums.get_all_albums, ctx=ctx, **kwargs)
    print_response(result, ctx=ctx)


@app.command(
    "remove-asset-from-album", deprecated=False, rich_help_panel="API commands"
)
def remove_asset_from_album(
    ctx: typer.Context,
    id: UUID = typer.Argument(..., help=r""""""),
    ids: list[UUID] = typer.Option(..., "--ids", help=r"""IDs to process"""),
) -> None:
    """Remove assets from an album

    [link=https://api.immich.app/endpoints/albums/removeAssetFromAlbum]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    kwargs["id"] = id
    set_nested(json_data, ["ids"], ids)
    bulk_ids_dto = BulkIdsDto.model_validate(json_data)
    kwargs["bulk_ids_dto"] = bulk_ids_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client.albums.remove_asset_from_album, ctx=ctx, **kwargs)
    print_response(result, ctx=ctx)


@app.command("remove-user-from-album", deprecated=False, rich_help_panel="API commands")
def remove_user_from_album(
    ctx: typer.Context,
    id: UUID = typer.Argument(..., help=r""""""),
    user_id: str = typer.Argument(..., help=r""""""),
) -> None:
    """Remove user from album

    [link=https://api.immich.app/endpoints/albums/removeUserFromAlbum]Immich API documentation[/link]
    """
    kwargs = {}
    kwargs["id"] = id
    kwargs["user_id"] = user_id
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client.albums.remove_user_from_album, ctx=ctx, **kwargs)
    print_response(result, ctx=ctx)


@app.command("update-album-info", deprecated=False, rich_help_panel="API commands")
def update_album_info(
    ctx: typer.Context,
    id: UUID = typer.Argument(..., help=r""""""),
    album_name: str | None = typer.Option(None, "--album-name", help=r"""Album name"""),
    album_thumbnail_asset_id: UUID | None = typer.Option(
        None, "--album-thumbnail-asset-id", help=r"""Album thumbnail asset ID"""
    ),
    description: str | None = typer.Option(
        None, "--description", help=r"""Album description"""
    ),
    is_activity_enabled: Literal["true", "false"] | None = typer.Option(
        None, "--is-activity-enabled", help=r"""Enable activity feed"""
    ),
    order: str | None = typer.Option(None, "--order", help=r"""Asset sort order"""),
) -> None:
    """Update an album

    [link=https://api.immich.app/endpoints/albums/updateAlbumInfo]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    kwargs["id"] = id
    if album_name is not None:
        set_nested(json_data, ["album_name"], album_name)
    if album_thumbnail_asset_id is not None:
        set_nested(json_data, ["album_thumbnail_asset_id"], album_thumbnail_asset_id)
    if description is not None:
        set_nested(json_data, ["description"], description)
    if is_activity_enabled is not None:
        set_nested(
            json_data, ["is_activity_enabled"], is_activity_enabled.lower() == "true"
        )
    if order is not None:
        set_nested(json_data, ["order"], order)
    update_album_dto = UpdateAlbumDto.model_validate(json_data)
    kwargs["update_album_dto"] = update_album_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client.albums.update_album_info, ctx=ctx, **kwargs)
    print_response(result, ctx=ctx)


@app.command("update-album-user", deprecated=False, rich_help_panel="API commands")
def update_album_user(
    ctx: typer.Context,
    id: UUID = typer.Argument(..., help=r""""""),
    user_id: str = typer.Argument(..., help=r""""""),
    role: str = typer.Option(..., "--role", help=r"""Album user role"""),
) -> None:
    """Update user role

    [link=https://api.immich.app/endpoints/albums/updateAlbumUser]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    kwargs["id"] = id
    kwargs["user_id"] = user_id
    set_nested(json_data, ["role"], role)
    update_album_user_dto = UpdateAlbumUserDto.model_validate(json_data)
    kwargs["update_album_user_dto"] = update_album_user_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client.albums.update_album_user, ctx=ctx, **kwargs)
    print_response(result, ctx=ctx)
