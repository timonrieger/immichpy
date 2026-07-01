"""Generated CLI commands for Duplicates tag (auto-generated, do not edit)."""

from __future__ import annotations

import typer
from uuid import UUID
from typing import TYPE_CHECKING

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
    help="""Endpoints for managing and identifying duplicate assets.\n\n[link=https://api.immich.app/endpoints/duplicates]Immich API documentation[/link]"""
)


@app.command("delete-duplicate", deprecated=False, rich_help_panel="API commands")
def delete_duplicate(
    ctx: typer.Context,
    id: UUID = typer.Argument(..., help=r""""""),
) -> None:
    """Dismiss a duplicate group

    [link=https://api.immich.app/endpoints/duplicates/deleteDuplicate]Immich API documentation[/link]
    """
    kwargs = {}
    kwargs["id"] = id
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client.duplicates.delete_duplicate, ctx=ctx, **kwargs)
    print_response(result, ctx=ctx)


@app.command("delete-duplicates", deprecated=False, rich_help_panel="API commands")
def delete_duplicates(
    ctx: typer.Context,
    ids: list[UUID] = typer.Option(..., "--ids", help=r"""IDs to process"""),
) -> None:
    """Delete duplicates

    [link=https://api.immich.app/endpoints/duplicates/deleteDuplicates]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    set_nested(json_data, ["ids"], ids)
    bulk_ids_dto = BulkIdsDto.model_validate(json_data)
    kwargs["bulk_ids_dto"] = bulk_ids_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client.duplicates.delete_duplicates, ctx=ctx, **kwargs)
    print_response(result, ctx=ctx)


@app.command("get-asset-duplicates", deprecated=False, rich_help_panel="API commands")
def get_asset_duplicates(
    ctx: typer.Context,
) -> None:
    """Retrieve duplicates

    [link=https://api.immich.app/endpoints/duplicates/getAssetDuplicates]Immich API documentation[/link]
    """
    kwargs = {}
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client.duplicates.get_asset_duplicates, ctx=ctx, **kwargs)
    print_response(result, ctx=ctx)


@app.command("resolve-duplicates", deprecated=False, rich_help_panel="API commands")
def resolve_duplicates(
    ctx: typer.Context,
    groups: list[str] = typer.Option(
        ...,
        "--groups",
        help=r"""List of duplicate groups to resolve

As a JSON string with keys: duplicateId (string), keepAssetIds (string[]), trashAssetIds (string[])""",
    ),
) -> None:
    """Resolve duplicate groups

    [link=https://api.immich.app/endpoints/duplicates/resolveDuplicates]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    value_groups = parse_json_options(groups, "--groups", ctx=ctx)
    set_nested(json_data, ["groups"], value_groups)
    duplicate_resolve_dto = DuplicateResolveDto.model_validate(json_data)
    kwargs["duplicate_resolve_dto"] = duplicate_resolve_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client.duplicates.resolve_duplicates, ctx=ctx, **kwargs)
    print_response(result, ctx=ctx)
