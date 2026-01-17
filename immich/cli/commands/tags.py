"""Generated CLI commands for Tags tag (auto-generated, do not edit)."""

from __future__ import annotations

import typer

from immich.cli.runtime import print_response, run_command, set_nested
from immich.client.models import *

app = typer.Typer(
    help="""A tag is a user-defined label that can be applied to assets for organizational purposes. Tags can also be hierarchical, allowing for parent-child relationships between tags.

Docs: https://api.immich.app/endpoints/tags"""
)


@app.command("bulk-tag-assets", deprecated=False)
def bulk_tag_assets(
    ctx: typer.Context,
    asset_ids: list[str] = typer.Option(..., "--assetIds", help="""Asset IDs"""),
    tag_ids: list[str] = typer.Option(..., "--tagIds", help="""Tag IDs"""),
) -> None:
    """Tag assets

    Docs: https://api.immich.app/endpoints/tags/bulkTagAssets
    """
    kwargs = {}
    has_flags = any([asset_ids, tag_ids])
    if not has_flags:
        raise SystemExit("Error: Request body is required. Use dotted body flags.")
    if any([asset_ids, tag_ids]):
        json_data = {}
        set_nested(json_data, ["assetIds"], asset_ids)
        set_nested(json_data, ["tagIds"], tag_ids)
        from immich.client.models.tag_bulk_assets_dto import TagBulkAssetsDto

        tag_bulk_assets_dto = TagBulkAssetsDto.model_validate(json_data)
        kwargs["tag_bulk_assets_dto"] = tag_bulk_assets_dto
    client = ctx.obj["client"]
    result = run_command(client, client.tags, "bulk_tag_assets", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("create-tag", deprecated=False)
def create_tag(
    ctx: typer.Context,
    color: str | None = typer.Option(None, "--color", help="""Tag color (hex)"""),
    name: str = typer.Option(..., "--name", help="""Tag name"""),
    parent_id: str | None = typer.Option(None, "--parentId", help="""Parent tag ID"""),
) -> None:
    """Create a tag

    Docs: https://api.immich.app/endpoints/tags/createTag
    """
    kwargs = {}
    has_flags = any([color, name, parent_id])
    if not has_flags:
        raise SystemExit("Error: Request body is required. Use dotted body flags.")
    if any([color, name, parent_id]):
        json_data = {}
        if color is not None:
            set_nested(json_data, ["color"], color)
        set_nested(json_data, ["name"], name)
        if parent_id is not None:
            set_nested(json_data, ["parentId"], parent_id)
        from immich.client.models.tag_create_dto import TagCreateDto

        tag_create_dto = TagCreateDto.model_validate(json_data)
        kwargs["tag_create_dto"] = tag_create_dto
    client = ctx.obj["client"]
    result = run_command(client, client.tags, "create_tag", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("delete-tag", deprecated=False)
def delete_tag(
    ctx: typer.Context,
    id: str,
) -> None:
    """Delete a tag

    Docs: https://api.immich.app/endpoints/tags/deleteTag
    """
    kwargs = {}
    kwargs["id"] = id
    client = ctx.obj["client"]
    result = run_command(client, client.tags, "delete_tag", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("get-all-tags", deprecated=False)
def get_all_tags(
    ctx: typer.Context,
) -> None:
    """Retrieve tags

    Docs: https://api.immich.app/endpoints/tags/getAllTags
    """
    kwargs = {}
    client = ctx.obj["client"]
    result = run_command(client, client.tags, "get_all_tags", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("get-tag-by-id", deprecated=False)
def get_tag_by_id(
    ctx: typer.Context,
    id: str,
) -> None:
    """Retrieve a tag

    Docs: https://api.immich.app/endpoints/tags/getTagById
    """
    kwargs = {}
    kwargs["id"] = id
    client = ctx.obj["client"]
    result = run_command(client, client.tags, "get_tag_by_id", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("tag-assets", deprecated=False)
def tag_assets(
    ctx: typer.Context,
    id: str,
    ids: list[str] = typer.Option(..., "--ids", help="""IDs to process"""),
) -> None:
    """Tag assets

    Docs: https://api.immich.app/endpoints/tags/tagAssets
    """
    kwargs = {}
    kwargs["id"] = id
    has_flags = any([ids])
    if not has_flags:
        raise SystemExit("Error: Request body is required. Use dotted body flags.")
    if any([ids]):
        json_data = {}
        set_nested(json_data, ["ids"], ids)
        from immich.client.models.bulk_ids_dto import BulkIdsDto

        bulk_ids_dto = BulkIdsDto.model_validate(json_data)
        kwargs["bulk_ids_dto"] = bulk_ids_dto
    client = ctx.obj["client"]
    result = run_command(client, client.tags, "tag_assets", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("untag-assets", deprecated=False)
def untag_assets(
    ctx: typer.Context,
    id: str,
    ids: list[str] = typer.Option(..., "--ids", help="""IDs to process"""),
) -> None:
    """Untag assets

    Docs: https://api.immich.app/endpoints/tags/untagAssets
    """
    kwargs = {}
    kwargs["id"] = id
    has_flags = any([ids])
    if not has_flags:
        raise SystemExit("Error: Request body is required. Use dotted body flags.")
    if any([ids]):
        json_data = {}
        set_nested(json_data, ["ids"], ids)
        from immich.client.models.bulk_ids_dto import BulkIdsDto

        bulk_ids_dto = BulkIdsDto.model_validate(json_data)
        kwargs["bulk_ids_dto"] = bulk_ids_dto
    client = ctx.obj["client"]
    result = run_command(client, client.tags, "untag_assets", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("update-tag", deprecated=False)
def update_tag(
    ctx: typer.Context,
    id: str,
    color: str | None = typer.Option(None, "--color", help="""Tag color (hex)"""),
) -> None:
    """Update a tag

    Docs: https://api.immich.app/endpoints/tags/updateTag
    """
    kwargs = {}
    kwargs["id"] = id
    has_flags = any([color])
    if not has_flags:
        raise SystemExit("Error: Request body is required. Use dotted body flags.")
    if any([color]):
        json_data = {}
        if color is not None:
            set_nested(json_data, ["color"], color)
        from immich.client.models.tag_update_dto import TagUpdateDto

        tag_update_dto = TagUpdateDto.model_validate(json_data)
        kwargs["tag_update_dto"] = tag_update_dto
    client = ctx.obj["client"]
    result = run_command(client, client.tags, "update_tag", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)


@app.command("upsert-tags", deprecated=False)
def upsert_tags(
    ctx: typer.Context,
    tags: list[str] = typer.Option(..., "--tags", help="""Tag names to upsert"""),
) -> None:
    """Upsert tags

    Docs: https://api.immich.app/endpoints/tags/upsertTags
    """
    kwargs = {}
    has_flags = any([tags])
    if not has_flags:
        raise SystemExit("Error: Request body is required. Use dotted body flags.")
    if any([tags]):
        json_data = {}
        set_nested(json_data, ["tags"], tags)
        from immich.client.models.tag_upsert_dto import TagUpsertDto

        tag_upsert_dto = TagUpsertDto.model_validate(json_data)
        kwargs["tag_upsert_dto"] = tag_upsert_dto
    client = ctx.obj["client"]
    result = run_command(client, client.tags, "upsert_tags", **kwargs)
    format_mode = ctx.obj.get("format", "pretty")
    print_response(result, format_mode)
