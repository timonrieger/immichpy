"""Generated CLI commands for Sync tag (auto-generated, do not edit)."""

from __future__ import annotations

import typer
from typing import Literal, TYPE_CHECKING

if TYPE_CHECKING:
    from immichpy import AsyncClient

from immichpy.cli.runtime import print_response, run_command, set_nested
from immichpy.client.generated.models import *

app = typer.Typer(
    help="""A collection of endpoints for the new mobile synchronization implementation.\n\n[link=https://api.immich.app/endpoints/sync]Immich API documentation[/link]"""
)


@app.command("delete-sync-ack", deprecated=False, rich_help_panel="API commands")
def delete_sync_ack(
    ctx: typer.Context,
    types: list[SyncEntityType] | None = typer.Option(
        None, "--types", help="""Sync entity types to delete acks for"""
    ),
) -> None:
    """Delete acknowledgements

    [link=https://api.immich.app/endpoints/sync/deleteSyncAck]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    if types is not None:
        set_nested(json_data, ["types"], types)
    sync_ack_delete_dto = SyncAckDeleteDto.model_validate(json_data)
    kwargs["sync_ack_delete_dto"] = sync_ack_delete_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client.sync.delete_sync_ack, ctx=ctx, **kwargs)
    print_response(result, ctx)


@app.command("get-sync-ack", deprecated=False, rich_help_panel="API commands")
def get_sync_ack(
    ctx: typer.Context,
) -> None:
    """Retrieve acknowledgements

    [link=https://api.immich.app/endpoints/sync/getSyncAck]Immich API documentation[/link]
    """
    kwargs = {}
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client.sync.get_sync_ack, ctx=ctx, **kwargs)
    print_response(result, ctx)


@app.command("get-sync-stream", deprecated=False, rich_help_panel="API commands")
def get_sync_stream(
    ctx: typer.Context,
    reset: Literal["true", "false"] | None = typer.Option(
        None, "--reset", help="""Reset sync state"""
    ),
    types: list[SyncRequestType] = typer.Option(
        ..., "--types", help="""Sync request types"""
    ),
) -> None:
    """Stream sync changes

    [link=https://api.immich.app/endpoints/sync/getSyncStream]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    if reset is not None:
        set_nested(json_data, ["reset"], reset.lower() == "true")
    set_nested(json_data, ["types"], types)
    sync_stream_dto = SyncStreamDto.model_validate(json_data)
    kwargs["sync_stream_dto"] = sync_stream_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client.sync.get_sync_stream, ctx=ctx, **kwargs)
    print_response(result, ctx)


@app.command("send-sync-ack", deprecated=False, rich_help_panel="API commands")
def send_sync_ack(
    ctx: typer.Context,
    acks: list[str] = typer.Option(
        ..., "--acks", help="""Acknowledgment IDs (max 1000)"""
    ),
) -> None:
    """Acknowledge changes

    [link=https://api.immich.app/endpoints/sync/sendSyncAck]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    set_nested(json_data, ["acks"], acks)
    sync_ack_set_dto = SyncAckSetDto.model_validate(json_data)
    kwargs["sync_ack_set_dto"] = sync_ack_set_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client.sync.send_sync_ack, ctx=ctx, **kwargs)
    print_response(result, ctx)
