"""Generated CLI commands for Assets tag (auto-generated, do not edit)."""

from __future__ import annotations

import typer
import json
from datetime import datetime
from pathlib import Path
from uuid import UUID
from typing import Literal, TYPE_CHECKING

if TYPE_CHECKING:
    from immichpy import AsyncClient

from immichpy.cli.runtime import print_response, run_command, set_nested
from immichpy.client.generated.models import *

app = typer.Typer(
    help="""An asset is an image or video that has been uploaded to Immich.\n\n[link=https://api.immich.app/endpoints/assets]Immich API documentation[/link]"""
)


@app.command("check-bulk-upload", deprecated=False, rich_help_panel="API commands")
def check_bulk_upload(
    ctx: typer.Context,
    assets: list[str] = typer.Option(
        ...,
        "--assets",
        help=r"""Assets to check

As a JSON string with keys: checksum (string), id (string)""",
    ),
) -> None:
    """Check bulk upload

    [link=https://api.immich.app/endpoints/assets/checkBulkUpload]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    value_assets = [json.loads(i) for i in assets]
    set_nested(json_data, ["assets"], value_assets)
    asset_bulk_upload_check_dto = AssetBulkUploadCheckDto.model_validate(json_data)
    kwargs["asset_bulk_upload_check_dto"] = asset_bulk_upload_check_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client.assets.check_bulk_upload, ctx=ctx, **kwargs)
    print_response(result, ctx)


@app.command("copy-asset", deprecated=False, rich_help_panel="API commands")
def copy_asset(
    ctx: typer.Context,
    albums: Literal["true", "false"] | None = typer.Option(
        None, "--albums", help=r"""Copy album associations"""
    ),
    favorite: Literal["true", "false"] | None = typer.Option(
        None, "--favorite", help=r"""Copy favorite status"""
    ),
    shared_links: Literal["true", "false"] | None = typer.Option(
        None, "--shared-links", help=r"""Copy shared links"""
    ),
    sidecar: Literal["true", "false"] | None = typer.Option(
        None, "--sidecar", help=r"""Copy sidecar file"""
    ),
    source_id: UUID = typer.Option(..., "--source-id", help=r"""Source asset ID"""),
    stack: Literal["true", "false"] | None = typer.Option(
        None, "--stack", help=r"""Copy stack association"""
    ),
    target_id: UUID = typer.Option(..., "--target-id", help=r"""Target asset ID"""),
) -> None:
    """Copy asset

    [link=https://api.immich.app/endpoints/assets/copyAsset]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    if albums is not None:
        set_nested(json_data, ["albums"], albums.lower() == "true")
    if favorite is not None:
        set_nested(json_data, ["favorite"], favorite.lower() == "true")
    if shared_links is not None:
        set_nested(json_data, ["shared_links"], shared_links.lower() == "true")
    if sidecar is not None:
        set_nested(json_data, ["sidecar"], sidecar.lower() == "true")
    set_nested(json_data, ["source_id"], source_id)
    if stack is not None:
        set_nested(json_data, ["stack"], stack.lower() == "true")
    set_nested(json_data, ["target_id"], target_id)
    asset_copy_dto = AssetCopyDto.model_validate(json_data)
    kwargs["asset_copy_dto"] = asset_copy_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client.assets.copy_asset, ctx=ctx, **kwargs)
    print_response(result, ctx)


@app.command("delete-asset-metadata", deprecated=False, rich_help_panel="API commands")
def delete_asset_metadata(
    ctx: typer.Context,
    id: UUID = typer.Argument(..., help=r"""Asset ID"""),
    key: str = typer.Argument(..., help=r"""Metadata key"""),
) -> None:
    """Delete asset metadata by key

    [link=https://api.immich.app/endpoints/assets/deleteAssetMetadata]Immich API documentation[/link]
    """
    kwargs = {}
    kwargs["id"] = id
    kwargs["key"] = key
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client.assets.delete_asset_metadata, ctx=ctx, **kwargs)
    print_response(result, ctx)


@app.command("delete-assets", deprecated=False, rich_help_panel="API commands")
def delete_assets(
    ctx: typer.Context,
    force: Literal["true", "false"] | None = typer.Option(
        None, "--force", help=r"""Force delete even if in use"""
    ),
    ids: list[UUID] = typer.Option(..., "--ids", help=r"""IDs to process"""),
) -> None:
    """Delete assets

    [link=https://api.immich.app/endpoints/assets/deleteAssets]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    if force is not None:
        set_nested(json_data, ["force"], force.lower() == "true")
    set_nested(json_data, ["ids"], ids)
    asset_bulk_delete_dto = AssetBulkDeleteDto.model_validate(json_data)
    kwargs["asset_bulk_delete_dto"] = asset_bulk_delete_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client.assets.delete_assets, ctx=ctx, **kwargs)
    print_response(result, ctx)


@app.command(
    "delete-bulk-asset-metadata", deprecated=False, rich_help_panel="API commands"
)
def delete_bulk_asset_metadata(
    ctx: typer.Context,
    items: list[str] = typer.Option(
        ...,
        "--items",
        help=r"""Metadata items to delete

As a JSON string with keys: assetId (string), key (string)""",
    ),
) -> None:
    """Delete asset metadata

    [link=https://api.immich.app/endpoints/assets/deleteBulkAssetMetadata]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    value_items = [json.loads(i) for i in items]
    set_nested(json_data, ["items"], value_items)
    asset_metadata_bulk_delete_dto = AssetMetadataBulkDeleteDto.model_validate(
        json_data
    )
    kwargs["asset_metadata_bulk_delete_dto"] = asset_metadata_bulk_delete_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client.assets.delete_bulk_asset_metadata, ctx=ctx, **kwargs)
    print_response(result, ctx)


@app.command("download-asset", deprecated=False, rich_help_panel="API commands")
def download_asset(
    ctx: typer.Context,
    id: UUID = typer.Argument(..., help=r""""""),
    edited: Literal["true", "false"] | None = typer.Option(
        None, "--edited", help=r"""Return edited asset if available"""
    ),
    key: str | None = typer.Option(None, "--key", help=r""""""),
    slug: str | None = typer.Option(None, "--slug", help=r""""""),
) -> None:
    """Download original asset

    [link=https://api.immich.app/endpoints/assets/downloadAsset]Immich API documentation[/link]
    """
    kwargs = {}
    if edited is not None:
        kwargs["edited"] = edited.lower() == "true"
    kwargs["id"] = id
    if key is not None:
        kwargs["key"] = key
    if slug is not None:
        kwargs["slug"] = slug
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client.assets.download_asset, ctx=ctx, **kwargs)
    print_response(result, ctx)


@app.command("edit-asset", deprecated=False, rich_help_panel="API commands")
def edit_asset(
    ctx: typer.Context,
    id: UUID = typer.Argument(..., help=r""""""),
    edits: list[str] = typer.Option(
        ...,
        "--edits",
        help=r"""List of edit actions to apply (crop, rotate, or mirror)

As a JSON string with keys: action (string), parameters (string)""",
    ),
) -> None:
    """Apply edits to an existing asset

    [link=https://api.immich.app/endpoints/assets/editAsset]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    kwargs["id"] = id
    value_edits = [json.loads(i) for i in edits]
    set_nested(json_data, ["edits"], value_edits)
    asset_edits_create_dto = AssetEditsCreateDto.model_validate(json_data)
    kwargs["asset_edits_create_dto"] = asset_edits_create_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client.assets.edit_asset, ctx=ctx, **kwargs)
    print_response(result, ctx)


@app.command("end-session", deprecated=False, rich_help_panel="API commands")
def end_session(
    ctx: typer.Context,
    id: UUID = typer.Argument(..., help=r""""""),
    session_id: UUID = typer.Argument(..., help=r""""""),
    key: str | None = typer.Option(None, "--key", help=r""""""),
    slug: str | None = typer.Option(None, "--slug", help=r""""""),
) -> None:
    """End HLS streaming session

    [link=https://api.immich.app/endpoints/assets/endSession]Immich API documentation[/link]
    """
    kwargs = {}
    kwargs["id"] = id
    if key is not None:
        kwargs["key"] = key
    kwargs["session_id"] = session_id
    if slug is not None:
        kwargs["slug"] = slug
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client.assets.end_session, ctx=ctx, **kwargs)
    print_response(result, ctx)


@app.command("get-asset-edits", deprecated=False, rich_help_panel="API commands")
def get_asset_edits(
    ctx: typer.Context,
    id: UUID = typer.Argument(..., help=r""""""),
) -> None:
    """Retrieve edits for an existing asset

    [link=https://api.immich.app/endpoints/assets/getAssetEdits]Immich API documentation[/link]
    """
    kwargs = {}
    kwargs["id"] = id
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client.assets.get_asset_edits, ctx=ctx, **kwargs)
    print_response(result, ctx)


@app.command("get-asset-info", deprecated=False, rich_help_panel="API commands")
def get_asset_info(
    ctx: typer.Context,
    id: UUID = typer.Argument(..., help=r""""""),
    key: str | None = typer.Option(None, "--key", help=r""""""),
    slug: str | None = typer.Option(None, "--slug", help=r""""""),
) -> None:
    """Retrieve an asset

    [link=https://api.immich.app/endpoints/assets/getAssetInfo]Immich API documentation[/link]
    """
    kwargs = {}
    kwargs["id"] = id
    if key is not None:
        kwargs["key"] = key
    if slug is not None:
        kwargs["slug"] = slug
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client.assets.get_asset_info, ctx=ctx, **kwargs)
    print_response(result, ctx)


@app.command("get-asset-metadata", deprecated=False, rich_help_panel="API commands")
def get_asset_metadata(
    ctx: typer.Context,
    id: UUID = typer.Argument(..., help=r""""""),
) -> None:
    """Get asset metadata

    [link=https://api.immich.app/endpoints/assets/getAssetMetadata]Immich API documentation[/link]
    """
    kwargs = {}
    kwargs["id"] = id
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client.assets.get_asset_metadata, ctx=ctx, **kwargs)
    print_response(result, ctx)


@app.command(
    "get-asset-metadata-by-key", deprecated=False, rich_help_panel="API commands"
)
def get_asset_metadata_by_key(
    ctx: typer.Context,
    id: UUID = typer.Argument(..., help=r"""Asset ID"""),
    key: str = typer.Argument(..., help=r"""Metadata key"""),
) -> None:
    """Retrieve asset metadata by key

    [link=https://api.immich.app/endpoints/assets/getAssetMetadataByKey]Immich API documentation[/link]
    """
    kwargs = {}
    kwargs["id"] = id
    kwargs["key"] = key
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client.assets.get_asset_metadata_by_key, ctx=ctx, **kwargs)
    print_response(result, ctx)


@app.command("get-asset-ocr", deprecated=False, rich_help_panel="API commands")
def get_asset_ocr(
    ctx: typer.Context,
    id: UUID = typer.Argument(..., help=r""""""),
) -> None:
    """Retrieve asset OCR data

    [link=https://api.immich.app/endpoints/assets/getAssetOcr]Immich API documentation[/link]
    """
    kwargs = {}
    kwargs["id"] = id
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client.assets.get_asset_ocr, ctx=ctx, **kwargs)
    print_response(result, ctx)


@app.command("get-asset-statistics", deprecated=False, rich_help_panel="API commands")
def get_asset_statistics(
    ctx: typer.Context,
    is_favorite: Literal["true", "false"] | None = typer.Option(
        None, "--is-favorite", help=r"""Filter by favorite status"""
    ),
    is_trashed: Literal["true", "false"] | None = typer.Option(
        None, "--is-trashed", help=r"""Filter by trash status"""
    ),
    visibility: AssetVisibility | None = typer.Option(
        None, "--visibility", help=r""""""
    ),
) -> None:
    """Get asset statistics

    [link=https://api.immich.app/endpoints/assets/getAssetStatistics]Immich API documentation[/link]
    """
    kwargs = {}
    if is_favorite is not None:
        kwargs["is_favorite"] = is_favorite.lower() == "true"
    if is_trashed is not None:
        kwargs["is_trashed"] = is_trashed.lower() == "true"
    if visibility is not None:
        kwargs["visibility"] = visibility
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client.assets.get_asset_statistics, ctx=ctx, **kwargs)
    print_response(result, ctx)


@app.command("get-main-playlist", deprecated=False, rich_help_panel="API commands")
def get_main_playlist(
    ctx: typer.Context,
    id: UUID = typer.Argument(..., help=r""""""),
    key: str | None = typer.Option(None, "--key", help=r""""""),
    slug: str | None = typer.Option(None, "--slug", help=r""""""),
) -> None:
    """Get HLS main playlist

    [link=https://api.immich.app/endpoints/assets/getMainPlaylist]Immich API documentation[/link]
    """
    kwargs = {}
    kwargs["id"] = id
    if key is not None:
        kwargs["key"] = key
    if slug is not None:
        kwargs["slug"] = slug
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client.assets.get_main_playlist, ctx=ctx, **kwargs)
    print_response(result, ctx)


@app.command("get-media-playlist", deprecated=False, rich_help_panel="API commands")
def get_media_playlist(
    ctx: typer.Context,
    id: UUID = typer.Argument(..., help=r""""""),
    session_id: UUID = typer.Argument(..., help=r""""""),
    variant_index: int = typer.Argument(..., help=r""""""),
    key: str | None = typer.Option(None, "--key", help=r""""""),
    slug: str | None = typer.Option(None, "--slug", help=r""""""),
    x_immich_hls_pos: float | None = typer.Option(
        None, "--x-immich-hls-pos", help=r"""""", min=0
    ),
) -> None:
    """Get HLS media playlist

    [link=https://api.immich.app/endpoints/assets/getMediaPlaylist]Immich API documentation[/link]
    """
    kwargs = {}
    kwargs["id"] = id
    if key is not None:
        kwargs["key"] = key
    kwargs["session_id"] = session_id
    if slug is not None:
        kwargs["slug"] = slug
    kwargs["variant_index"] = variant_index
    if x_immich_hls_pos is not None:
        kwargs["x_immich_hls_pos"] = x_immich_hls_pos
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client.assets.get_media_playlist, ctx=ctx, **kwargs)
    print_response(result, ctx)


@app.command("get-segment", deprecated=False, rich_help_panel="API commands")
def get_segment(
    ctx: typer.Context,
    filename: str = typer.Argument(..., help=r""""""),
    id: UUID = typer.Argument(..., help=r""""""),
    session_id: UUID = typer.Argument(..., help=r""""""),
    variant_index: int = typer.Argument(..., help=r""""""),
    key: str | None = typer.Option(None, "--key", help=r""""""),
    slug: str | None = typer.Option(None, "--slug", help=r""""""),
    x_immich_hls_msn: int | None = typer.Option(
        None, "--x-immich-hls-msn", help=r"""""", min=0, max=9007199254740991
    ),
) -> None:
    """Get HLS segment or init file

    [link=https://api.immich.app/endpoints/assets/getSegment]Immich API documentation[/link]
    """
    kwargs = {}
    kwargs["filename"] = filename
    kwargs["id"] = id
    if key is not None:
        kwargs["key"] = key
    kwargs["session_id"] = session_id
    if slug is not None:
        kwargs["slug"] = slug
    kwargs["variant_index"] = variant_index
    if x_immich_hls_msn is not None:
        kwargs["x_immich_hls_msn"] = x_immich_hls_msn
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client.assets.get_segment, ctx=ctx, **kwargs)
    print_response(result, ctx)


@app.command("play-asset-video", deprecated=False, rich_help_panel="API commands")
def play_asset_video(
    ctx: typer.Context,
    id: UUID = typer.Argument(..., help=r""""""),
    key: str | None = typer.Option(None, "--key", help=r""""""),
    slug: str | None = typer.Option(None, "--slug", help=r""""""),
) -> None:
    """Play asset video

    [link=https://api.immich.app/endpoints/assets/playAssetVideo]Immich API documentation[/link]
    """
    kwargs = {}
    kwargs["id"] = id
    if key is not None:
        kwargs["key"] = key
    if slug is not None:
        kwargs["slug"] = slug
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client.assets.play_asset_video, ctx=ctx, **kwargs)
    print_response(result, ctx)


@app.command("remove-asset-edits", deprecated=False, rich_help_panel="API commands")
def remove_asset_edits(
    ctx: typer.Context,
    id: UUID = typer.Argument(..., help=r""""""),
) -> None:
    """Remove edits from an existing asset

    [link=https://api.immich.app/endpoints/assets/removeAssetEdits]Immich API documentation[/link]
    """
    kwargs = {}
    kwargs["id"] = id
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client.assets.remove_asset_edits, ctx=ctx, **kwargs)
    print_response(result, ctx)


@app.command("run-asset-jobs", deprecated=False, rich_help_panel="API commands")
def run_asset_jobs(
    ctx: typer.Context,
    asset_ids: list[UUID] = typer.Option(..., "--asset-ids", help=r"""Asset IDs"""),
    name: str = typer.Option(..., "--name", help=r"""Job name"""),
) -> None:
    """Run an asset job

    [link=https://api.immich.app/endpoints/assets/runAssetJobs]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    set_nested(json_data, ["asset_ids"], asset_ids)
    set_nested(json_data, ["name"], name)
    asset_jobs_dto = AssetJobsDto.model_validate(json_data)
    kwargs["asset_jobs_dto"] = asset_jobs_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client.assets.run_asset_jobs, ctx=ctx, **kwargs)
    print_response(result, ctx)


@app.command("update-asset", deprecated=True, rich_help_panel="API commands")
def update_asset(
    ctx: typer.Context,
    id: UUID = typer.Argument(..., help=r""""""),
    date_time_original: str | None = typer.Option(
        None, "--date-time-original", help=r"""Original date and time"""
    ),
    description: str | None = typer.Option(
        None, "--description", help=r"""Asset description"""
    ),
    is_favorite: Literal["true", "false"] | None = typer.Option(
        None, "--is-favorite", help=r"""Mark as favorite"""
    ),
    latitude: float | None = typer.Option(
        None, "--latitude", help=r"""Latitude coordinate""", min=-90, max=90
    ),
    live_photo_video_id: UUID | None = typer.Option(
        None, "--live-photo-video-id", help=r"""Live photo video ID"""
    ),
    longitude: float | None = typer.Option(
        None, "--longitude", help=r"""Longitude coordinate""", min=-180, max=180
    ),
    rating: int | None = typer.Option(
        None,
        "--rating",
        help=r"""Rating in range [1-5] (starred), -1 (rejected), or null (unrated)""",
        min=-1,
        max=5,
    ),
    visibility: str | None = typer.Option(
        None, "--visibility", help=r"""Asset visibility"""
    ),
) -> None:
    """Update an asset

    [link=https://api.immich.app/endpoints/assets/updateAsset]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    kwargs["id"] = id
    if date_time_original is not None:
        set_nested(json_data, ["date_time_original"], date_time_original)
    if description is not None:
        set_nested(json_data, ["description"], description)
    if is_favorite is not None:
        set_nested(json_data, ["is_favorite"], is_favorite.lower() == "true")
    if latitude is not None:
        set_nested(json_data, ["latitude"], latitude)
    if live_photo_video_id is not None:
        set_nested(json_data, ["live_photo_video_id"], live_photo_video_id)
    if longitude is not None:
        set_nested(json_data, ["longitude"], longitude)
    if rating is not None:
        set_nested(json_data, ["rating"], rating)
    if visibility is not None:
        set_nested(json_data, ["visibility"], visibility)
    update_asset_dto = UpdateAssetDto.model_validate(json_data)
    kwargs["update_asset_dto"] = update_asset_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client.assets.update_asset, ctx=ctx, **kwargs)
    print_response(result, ctx)


@app.command("update-asset-metadata", deprecated=False, rich_help_panel="API commands")
def update_asset_metadata(
    ctx: typer.Context,
    id: UUID = typer.Argument(..., help=r""""""),
    items: list[str] = typer.Option(
        ...,
        "--items",
        help=r"""Metadata items to upsert

As a JSON string with keys: key (string), value (object)""",
    ),
) -> None:
    """Update asset metadata

    [link=https://api.immich.app/endpoints/assets/updateAssetMetadata]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    kwargs["id"] = id
    value_items = [json.loads(i) for i in items]
    set_nested(json_data, ["items"], value_items)
    asset_metadata_upsert_dto = AssetMetadataUpsertDto.model_validate(json_data)
    kwargs["asset_metadata_upsert_dto"] = asset_metadata_upsert_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client.assets.update_asset_metadata, ctx=ctx, **kwargs)
    print_response(result, ctx)


@app.command("update-assets", deprecated=True, rich_help_panel="API commands")
def update_assets(
    ctx: typer.Context,
    date_time_original: str | None = typer.Option(
        None, "--date-time-original", help=r"""Original date and time"""
    ),
    date_time_relative: int | None = typer.Option(
        None,
        "--date-time-relative",
        help=r"""Relative time offset in minutes""",
        min=-9007199254740991,
        max=9007199254740991,
    ),
    description: str | None = typer.Option(
        None, "--description", help=r"""Asset description"""
    ),
    duplicate_id: str | None = typer.Option(
        None, "--duplicate-id", help=r"""Duplicate ID"""
    ),
    ids: list[UUID] = typer.Option(..., "--ids", help=r"""Asset IDs to update"""),
    is_favorite: Literal["true", "false"] | None = typer.Option(
        None, "--is-favorite", help=r"""Mark as favorite"""
    ),
    latitude: float | None = typer.Option(
        None, "--latitude", help=r"""Latitude coordinate""", min=-90, max=90
    ),
    longitude: float | None = typer.Option(
        None, "--longitude", help=r"""Longitude coordinate""", min=-180, max=180
    ),
    rating: int | None = typer.Option(
        None,
        "--rating",
        help=r"""Rating in range [1-5] (starred), -1 (rejected), or null (unrated)""",
        min=-1,
        max=5,
    ),
    time_zone: str | None = typer.Option(
        None, "--time-zone", help=r"""Time zone (IANA timezone)"""
    ),
    visibility: str | None = typer.Option(
        None, "--visibility", help=r"""Asset visibility"""
    ),
) -> None:
    """Update assets

    [link=https://api.immich.app/endpoints/assets/updateAssets]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    if date_time_original is not None:
        set_nested(json_data, ["date_time_original"], date_time_original)
    if date_time_relative is not None:
        set_nested(json_data, ["date_time_relative"], date_time_relative)
    if description is not None:
        set_nested(json_data, ["description"], description)
    if duplicate_id is not None:
        set_nested(json_data, ["duplicate_id"], duplicate_id)
    set_nested(json_data, ["ids"], ids)
    if is_favorite is not None:
        set_nested(json_data, ["is_favorite"], is_favorite.lower() == "true")
    if latitude is not None:
        set_nested(json_data, ["latitude"], latitude)
    if longitude is not None:
        set_nested(json_data, ["longitude"], longitude)
    if rating is not None:
        set_nested(json_data, ["rating"], rating)
    if time_zone is not None:
        set_nested(json_data, ["time_zone"], time_zone)
    if visibility is not None:
        set_nested(json_data, ["visibility"], visibility)
    asset_bulk_update_dto = AssetBulkUpdateDto.model_validate(json_data)
    kwargs["asset_bulk_update_dto"] = asset_bulk_update_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client.assets.update_assets, ctx=ctx, **kwargs)
    print_response(result, ctx)


@app.command(
    "update-bulk-asset-metadata", deprecated=False, rich_help_panel="API commands"
)
def update_bulk_asset_metadata(
    ctx: typer.Context,
    items: list[str] = typer.Option(
        ...,
        "--items",
        help=r"""Metadata items to upsert

As a JSON string with keys: assetId (string), key (string), value (object)""",
    ),
) -> None:
    """Upsert asset metadata

    [link=https://api.immich.app/endpoints/assets/updateBulkAssetMetadata]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    value_items = [json.loads(i) for i in items]
    set_nested(json_data, ["items"], value_items)
    asset_metadata_bulk_upsert_dto = AssetMetadataBulkUpsertDto.model_validate(
        json_data
    )
    kwargs["asset_metadata_bulk_upsert_dto"] = asset_metadata_bulk_upsert_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client.assets.update_bulk_asset_metadata, ctx=ctx, **kwargs)
    print_response(result, ctx)


@app.command("upload-asset", deprecated=False, rich_help_panel="API commands")
def upload_asset(
    ctx: typer.Context,
    asset_data: Path = typer.Option(
        ..., "--asset-data", help=r"""Asset file data""", exists=True
    ),
    duration: int | None = typer.Option(
        None,
        "--duration",
        help=r"""Duration in milliseconds (for videos)""",
        min=0,
        max=9007199254740991,
    ),
    file_created_at: datetime = typer.Option(
        ...,
        "--file-created-at",
        help=r"""File creation date

Example: 2024-01-01T00:00:00.000Z""",
    ),
    file_modified_at: datetime = typer.Option(
        ...,
        "--file-modified-at",
        help=r"""File modification date

Example: 2024-01-01T00:00:00.000Z""",
    ),
    filename: str | None = typer.Option(None, "--filename", help=r"""Filename"""),
    is_favorite: Literal["true", "false"] | None = typer.Option(
        None, "--is-favorite", help=r"""Mark as favorite"""
    ),
    key: str | None = typer.Option(None, "--key", help=r""""""),
    live_photo_video_id: UUID | None = typer.Option(
        None, "--live-photo-video-id", help=r"""Live photo video ID"""
    ),
    metadata: list[str] | None = typer.Option(
        None,
        "--metadata",
        help=r"""Asset metadata items

As a JSON string with keys: key (string), value (object)""",
    ),
    sidecar_data: Path | None = typer.Option(
        None, "--sidecar-data", help=r"""Sidecar file data""", exists=True
    ),
    slug: str | None = typer.Option(None, "--slug", help=r""""""),
    visibility: str | None = typer.Option(
        None, "--visibility", help=r"""Asset visibility"""
    ),
    x_immich_checksum: str | None = typer.Option(
        None,
        "--x-immich-checksum",
        help=r"""sha1 checksum that can be used for duplicate detection before the file is uploaded""",
    ),
) -> None:
    """Upload asset

    [link=https://api.immich.app/endpoints/assets/uploadAsset]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    if key is not None:
        kwargs["key"] = key
    if slug is not None:
        kwargs["slug"] = slug
    if x_immich_checksum is not None:
        kwargs["x_immich_checksum"] = x_immich_checksum
    kwargs["asset_data"] = (asset_data.name, asset_data.read_bytes())
    if duration is not None:
        set_nested(json_data, ["duration"], duration)
    set_nested(json_data, ["file_created_at"], file_created_at)
    set_nested(json_data, ["file_modified_at"], file_modified_at)
    if filename is not None:
        set_nested(json_data, ["filename"], filename)
    if is_favorite is not None:
        set_nested(json_data, ["is_favorite"], is_favorite.lower() == "true")
    if live_photo_video_id is not None:
        set_nested(json_data, ["live_photo_video_id"], live_photo_video_id)
    if metadata is not None:
        value_metadata = [json.loads(i) for i in metadata]
        set_nested(json_data, ["metadata"], value_metadata)
    if sidecar_data is not None:
        set_nested(
            json_data, ["sidecar_data"], (sidecar_data.name, sidecar_data.read_bytes())
        )
    if visibility is not None:
        set_nested(json_data, ["visibility"], visibility)
    kwargs.update(json_data)
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client.assets.upload_asset, ctx=ctx, **kwargs)
    print_response(result, ctx)


@app.command("view-asset", deprecated=False, rich_help_panel="API commands")
def view_asset(
    ctx: typer.Context,
    id: UUID = typer.Argument(..., help=r""""""),
    edited: Literal["true", "false"] | None = typer.Option(
        None, "--edited", help=r"""Return edited asset if available"""
    ),
    key: str | None = typer.Option(None, "--key", help=r""""""),
    size: AssetMediaSize | None = typer.Option(None, "--size", help=r""""""),
    slug: str | None = typer.Option(None, "--slug", help=r""""""),
) -> None:
    """View asset thumbnail

    [link=https://api.immich.app/endpoints/assets/viewAsset]Immich API documentation[/link]
    """
    kwargs = {}
    if edited is not None:
        kwargs["edited"] = edited.lower() == "true"
    kwargs["id"] = id
    if key is not None:
        kwargs["key"] = key
    if size is not None:
        kwargs["size"] = size
    if slug is not None:
        kwargs["slug"] = slug
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client.assets.view_asset, ctx=ctx, **kwargs)
    print_response(result, ctx)
