"""Generated CLI commands for Search tag (auto-generated, do not edit)."""

from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, Literal
from uuid import UUID

import typer

if TYPE_CHECKING:
    from immichpy import AsyncClient

from immichpy.cli.runtime import (
    parse_json_options,
    print_response,
    run_command,
    set_nested,
)
from immichpy.client.generated.models import (
    AssetOrder,
    AssetTypeEnum,
    AssetVisibility,
    MetadataSearchDto,
    RandomSearchDto,
    SearchOrderField,
    SearchSuggestionType,
    SmartSearchDto,
    StatisticsSearchDto,
)

app = typer.Typer(
    help="""Endpoints related to searching assets via text, smart search, optical character recognition (OCR), and other filters like person, album, and other metadata. Search endpoints usually support pagination and sorting.\n\n[link=https://api.immich.app/endpoints/search]Immich API documentation[/link]"""
)


@app.command("get-assets-by-city", deprecated=False, rich_help_panel="API commands")
def get_assets_by_city(
    ctx: typer.Context,
) -> None:
    """Retrieve assets by city

    [link=https://api.immich.app/endpoints/search/getAssetsByCity]Immich API documentation[/link]
    """
    kwargs = {}
    client: AsyncClient = ctx.obj["client"]
    result = run_command(client.search.get_assets_by_city, ctx=ctx, **kwargs)
    print_response(result, ctx=ctx)


@app.command("get-explore-data", deprecated=False, rich_help_panel="API commands")
def get_explore_data(
    ctx: typer.Context,
) -> None:
    """Retrieve explore data

    [link=https://api.immich.app/endpoints/search/getExploreData]Immich API documentation[/link]
    """
    kwargs = {}
    client: AsyncClient = ctx.obj["client"]
    result = run_command(client.search.get_explore_data, ctx=ctx, **kwargs)
    print_response(result, ctx=ctx)


@app.command("get-search-suggestions", deprecated=False, rich_help_panel="API commands")
def get_search_suggestions(
    ctx: typer.Context,
    country: str | None = typer.Option(
        None, "--country", help=r"""Filter by country"""
    ),
    include_null: Literal["true", "false"] | None = typer.Option(
        None, "--include-null", help=r"""Include null values in suggestions"""
    ),
    lens_model: str | None = typer.Option(
        None, "--lens-model", help=r"""Filter by lens model"""
    ),
    make: str | None = typer.Option(None, "--make", help=r"""Filter by camera make"""),
    model: str | None = typer.Option(
        None, "--model", help=r"""Filter by camera model"""
    ),
    state: str | None = typer.Option(
        None, "--state", help=r"""Filter by state/province"""
    ),
    type: SearchSuggestionType = typer.Option(..., "--type", help=r""""""),
) -> None:
    """Retrieve search suggestions

    [link=https://api.immich.app/endpoints/search/getSearchSuggestions]Immich API documentation[/link]
    """
    kwargs = {}
    if country is not None:
        kwargs["country"] = country
    if include_null is not None:
        kwargs["include_null"] = include_null.lower() == "true"
    if lens_model is not None:
        kwargs["lens_model"] = lens_model
    if make is not None:
        kwargs["make"] = make
    if model is not None:
        kwargs["model"] = model
    if state is not None:
        kwargs["state"] = state
    kwargs["type"] = type
    client: AsyncClient = ctx.obj["client"]
    result = run_command(client.search.get_search_suggestions, ctx=ctx, **kwargs)
    print_response(result, ctx=ctx)


@app.command(
    "search-asset-statistics", deprecated=False, rich_help_panel="API commands"
)
def search_asset_statistics(
    ctx: typer.Context,
    album_ids: list[UUID] | None = typer.Option(
        None, "--album-ids", help=r"""Filter by album IDs"""
    ),
    city: str | None = typer.Option(None, "--city", help=r"""Filter by city name"""),
    country: str | None = typer.Option(
        None, "--country", help=r"""Filter by country name"""
    ),
    created_after: datetime | None = typer.Option(
        None,
        "--created-after",
        help=r"""Filter by creation date (after)

Example: 2024-01-01T00:00:00.000Z""",
    ),
    created_before: datetime | None = typer.Option(
        None,
        "--created-before",
        help=r"""Filter by creation date (before)

Example: 2024-01-01T00:00:00.000Z""",
    ),
    description: str | None = typer.Option(
        None, "--description", help=r"""Filter by description text"""
    ),
    filter_album_ids_all: list[UUID] | None = typer.Option(
        None, "--filter-album-ids-all", help=r""""""
    ),
    filter_album_ids_any: list[UUID] | None = typer.Option(
        None, "--filter-album-ids-any", help=r""""""
    ),
    filter_album_ids_none: list[UUID] | None = typer.Option(
        None, "--filter-album-ids-none", help=r""""""
    ),
    filter_checksum_eq: str | None = typer.Option(
        None, "--filter-checksum-eq", help=r""""""
    ),
    filter_checksum_in_: list[str] | None = typer.Option(
        None, "--filter-checksum-in", help=r""""""
    ),
    filter_checksum_ne: str | None = typer.Option(
        None, "--filter-checksum-ne", help=r""""""
    ),
    filter_checksum_not_in: list[str] | None = typer.Option(
        None, "--filter-checksum-not-in", help=r""""""
    ),
    filter_city_eq: str | None = typer.Option(None, "--filter-city-eq", help=r""""""),
    filter_city_in_: list[str] | None = typer.Option(
        None, "--filter-city-in", help=r""""""
    ),
    filter_city_ne: str | None = typer.Option(None, "--filter-city-ne", help=r""""""),
    filter_city_not_in: list[str] | None = typer.Option(
        None, "--filter-city-not-in", help=r""""""
    ),
    filter_country_eq: str | None = typer.Option(
        None, "--filter-country-eq", help=r""""""
    ),
    filter_country_in_: list[str] | None = typer.Option(
        None, "--filter-country-in", help=r""""""
    ),
    filter_country_ne: str | None = typer.Option(
        None, "--filter-country-ne", help=r""""""
    ),
    filter_country_not_in: list[str] | None = typer.Option(
        None, "--filter-country-not-in", help=r""""""
    ),
    filter_created_at_eq: datetime | None = typer.Option(
        None, "--filter-created-at-eq", help=r"""Example: 2024-01-01T00:00:00.000Z"""
    ),
    filter_created_at_gt: datetime | None = typer.Option(
        None, "--filter-created-at-gt", help=r"""Example: 2024-01-01T00:00:00.000Z"""
    ),
    filter_created_at_gte: datetime | None = typer.Option(
        None, "--filter-created-at-gte", help=r"""Example: 2024-01-01T00:00:00.000Z"""
    ),
    filter_created_at_lt: datetime | None = typer.Option(
        None, "--filter-created-at-lt", help=r"""Example: 2024-01-01T00:00:00.000Z"""
    ),
    filter_created_at_lte: datetime | None = typer.Option(
        None, "--filter-created-at-lte", help=r"""Example: 2024-01-01T00:00:00.000Z"""
    ),
    filter_created_at_ne: datetime | None = typer.Option(
        None, "--filter-created-at-ne", help=r"""Example: 2024-01-01T00:00:00.000Z"""
    ),
    filter_description_ends_with: str | None = typer.Option(
        None, "--filter-description-ends-with", help=r""""""
    ),
    filter_description_eq: str | None = typer.Option(
        None, "--filter-description-eq", help=r""""""
    ),
    filter_description_in_: list[str] | None = typer.Option(
        None, "--filter-description-in", help=r""""""
    ),
    filter_description_like: str | None = typer.Option(
        None, "--filter-description-like", help=r""""""
    ),
    filter_description_ne: str | None = typer.Option(
        None, "--filter-description-ne", help=r""""""
    ),
    filter_description_not_in: list[str] | None = typer.Option(
        None, "--filter-description-not-in", help=r""""""
    ),
    filter_description_not_like: str | None = typer.Option(
        None, "--filter-description-not-like", help=r""""""
    ),
    filter_description_starts_with: str | None = typer.Option(
        None, "--filter-description-starts-with", help=r""""""
    ),
    filter_encoded_video_path_eq: str | None = typer.Option(
        None, "--filter-encoded-video-path-eq", help=r""""""
    ),
    filter_encoded_video_path_in_: list[str] | None = typer.Option(
        None, "--filter-encoded-video-path-in", help=r""""""
    ),
    filter_encoded_video_path_ne: str | None = typer.Option(
        None, "--filter-encoded-video-path-ne", help=r""""""
    ),
    filter_encoded_video_path_not_in: list[str] | None = typer.Option(
        None, "--filter-encoded-video-path-not-in", help=r""""""
    ),
    filter_file_size_in_bytes_eq: float | None = typer.Option(
        None, "--filter-file-size-in-bytes-eq", help=r""""""
    ),
    filter_file_size_in_bytes_gt: float | None = typer.Option(
        None, "--filter-file-size-in-bytes-gt", help=r""""""
    ),
    filter_file_size_in_bytes_gte: float | None = typer.Option(
        None, "--filter-file-size-in-bytes-gte", help=r""""""
    ),
    filter_file_size_in_bytes_in_: list[float] | None = typer.Option(
        None, "--filter-file-size-in-bytes-in", help=r""""""
    ),
    filter_file_size_in_bytes_lt: float | None = typer.Option(
        None, "--filter-file-size-in-bytes-lt", help=r""""""
    ),
    filter_file_size_in_bytes_lte: float | None = typer.Option(
        None, "--filter-file-size-in-bytes-lte", help=r""""""
    ),
    filter_file_size_in_bytes_ne: float | None = typer.Option(
        None, "--filter-file-size-in-bytes-ne", help=r""""""
    ),
    filter_file_size_in_bytes_not_in: list[float] | None = typer.Option(
        None, "--filter-file-size-in-bytes-not-in", help=r""""""
    ),
    filter_has_albums_eq: Literal["true", "false"] | None = typer.Option(
        None, "--filter-has-albums-eq", help=r""""""
    ),
    filter_has_people_eq: Literal["true", "false"] | None = typer.Option(
        None, "--filter-has-people-eq", help=r""""""
    ),
    filter_has_tags_eq: Literal["true", "false"] | None = typer.Option(
        None, "--filter-has-tags-eq", help=r""""""
    ),
    filter_id_eq: UUID | None = typer.Option(None, "--filter-id-eq", help=r""""""),
    filter_id_ne: UUID | None = typer.Option(None, "--filter-id-ne", help=r""""""),
    filter_is_encoded_eq: Literal["true", "false"] | None = typer.Option(
        None, "--filter-is-encoded-eq", help=r""""""
    ),
    filter_is_favorite_eq: Literal["true", "false"] | None = typer.Option(
        None, "--filter-is-favorite-eq", help=r""""""
    ),
    filter_is_motion_eq: Literal["true", "false"] | None = typer.Option(
        None, "--filter-is-motion-eq", help=r""""""
    ),
    filter_is_offline_eq: Literal["true", "false"] | None = typer.Option(
        None, "--filter-is-offline-eq", help=r""""""
    ),
    filter_lens_model_eq: str | None = typer.Option(
        None, "--filter-lens-model-eq", help=r""""""
    ),
    filter_lens_model_in_: list[str] | None = typer.Option(
        None, "--filter-lens-model-in", help=r""""""
    ),
    filter_lens_model_ne: str | None = typer.Option(
        None, "--filter-lens-model-ne", help=r""""""
    ),
    filter_lens_model_not_in: list[str] | None = typer.Option(
        None, "--filter-lens-model-not-in", help=r""""""
    ),
    filter_library_id_eq: UUID | None = typer.Option(
        None, "--filter-library-id-eq", help=r""""""
    ),
    filter_library_id_ne: UUID | None = typer.Option(
        None, "--filter-library-id-ne", help=r""""""
    ),
    filter_make_eq: str | None = typer.Option(None, "--filter-make-eq", help=r""""""),
    filter_make_in_: list[str] | None = typer.Option(
        None, "--filter-make-in", help=r""""""
    ),
    filter_make_ne: str | None = typer.Option(None, "--filter-make-ne", help=r""""""),
    filter_make_not_in: list[str] | None = typer.Option(
        None, "--filter-make-not-in", help=r""""""
    ),
    filter_model_eq: str | None = typer.Option(None, "--filter-model-eq", help=r""""""),
    filter_model_in_: list[str] | None = typer.Option(
        None, "--filter-model-in", help=r""""""
    ),
    filter_model_ne: str | None = typer.Option(None, "--filter-model-ne", help=r""""""),
    filter_model_not_in: list[str] | None = typer.Option(
        None, "--filter-model-not-in", help=r""""""
    ),
    filter_ocr_matches: str | None = typer.Option(
        None, "--filter-ocr-matches", help=r""""""
    ),
    filter_or_: list[str] | None = typer.Option(
        None,
        "--filter-or",
        help=r"""As a JSON string with keys: albumIds (object), checksum (object), city (object), country (object), createdAt (object), description (object), encodedVideoPath (object), fileSizeInBytes (object), hasAlbums (object), hasPeople (object), hasTags (object), id (object), isEncoded (object), isFavorite (object), isMotion (object), isOffline (object), lensModel (object), libraryId (object), make (object), model (object), ocr (object), originalFileName (object), originalPath (object), personIds (object), rating (object), state (object), tagIds (object), takenAt (object), trashedAt (object), type (object), updatedAt (object), visibility (object)""",
    ),
    filter_original_file_name_ends_with: str | None = typer.Option(
        None, "--filter-original-file-name-ends-with", help=r""""""
    ),
    filter_original_file_name_eq: str | None = typer.Option(
        None, "--filter-original-file-name-eq", help=r""""""
    ),
    filter_original_file_name_in_: list[str] | None = typer.Option(
        None, "--filter-original-file-name-in", help=r""""""
    ),
    filter_original_file_name_like: str | None = typer.Option(
        None, "--filter-original-file-name-like", help=r""""""
    ),
    filter_original_file_name_ne: str | None = typer.Option(
        None, "--filter-original-file-name-ne", help=r""""""
    ),
    filter_original_file_name_not_in: list[str] | None = typer.Option(
        None, "--filter-original-file-name-not-in", help=r""""""
    ),
    filter_original_file_name_not_like: str | None = typer.Option(
        None, "--filter-original-file-name-not-like", help=r""""""
    ),
    filter_original_file_name_starts_with: str | None = typer.Option(
        None, "--filter-original-file-name-starts-with", help=r""""""
    ),
    filter_original_path_ends_with: str | None = typer.Option(
        None, "--filter-original-path-ends-with", help=r""""""
    ),
    filter_original_path_eq: str | None = typer.Option(
        None, "--filter-original-path-eq", help=r""""""
    ),
    filter_original_path_in_: list[str] | None = typer.Option(
        None, "--filter-original-path-in", help=r""""""
    ),
    filter_original_path_like: str | None = typer.Option(
        None, "--filter-original-path-like", help=r""""""
    ),
    filter_original_path_ne: str | None = typer.Option(
        None, "--filter-original-path-ne", help=r""""""
    ),
    filter_original_path_not_in: list[str] | None = typer.Option(
        None, "--filter-original-path-not-in", help=r""""""
    ),
    filter_original_path_not_like: str | None = typer.Option(
        None, "--filter-original-path-not-like", help=r""""""
    ),
    filter_original_path_starts_with: str | None = typer.Option(
        None, "--filter-original-path-starts-with", help=r""""""
    ),
    filter_person_ids_all: list[UUID] | None = typer.Option(
        None, "--filter-person-ids-all", help=r""""""
    ),
    filter_person_ids_any: list[UUID] | None = typer.Option(
        None, "--filter-person-ids-any", help=r""""""
    ),
    filter_person_ids_none: list[UUID] | None = typer.Option(
        None, "--filter-person-ids-none", help=r""""""
    ),
    filter_rating_eq: float | None = typer.Option(
        None, "--filter-rating-eq", help=r""""""
    ),
    filter_rating_gt: float | None = typer.Option(
        None, "--filter-rating-gt", help=r""""""
    ),
    filter_rating_gte: float | None = typer.Option(
        None, "--filter-rating-gte", help=r""""""
    ),
    filter_rating_in_: list[float] | None = typer.Option(
        None, "--filter-rating-in", help=r""""""
    ),
    filter_rating_lt: float | None = typer.Option(
        None, "--filter-rating-lt", help=r""""""
    ),
    filter_rating_lte: float | None = typer.Option(
        None, "--filter-rating-lte", help=r""""""
    ),
    filter_rating_ne: float | None = typer.Option(
        None, "--filter-rating-ne", help=r""""""
    ),
    filter_rating_not_in: list[float] | None = typer.Option(
        None, "--filter-rating-not-in", help=r""""""
    ),
    filter_state_eq: str | None = typer.Option(None, "--filter-state-eq", help=r""""""),
    filter_state_in_: list[str] | None = typer.Option(
        None, "--filter-state-in", help=r""""""
    ),
    filter_state_ne: str | None = typer.Option(None, "--filter-state-ne", help=r""""""),
    filter_state_not_in: list[str] | None = typer.Option(
        None, "--filter-state-not-in", help=r""""""
    ),
    filter_tag_ids_all: list[UUID] | None = typer.Option(
        None, "--filter-tag-ids-all", help=r""""""
    ),
    filter_tag_ids_any: list[UUID] | None = typer.Option(
        None, "--filter-tag-ids-any", help=r""""""
    ),
    filter_tag_ids_none: list[UUID] | None = typer.Option(
        None, "--filter-tag-ids-none", help=r""""""
    ),
    filter_taken_at_eq: datetime | None = typer.Option(
        None, "--filter-taken-at-eq", help=r"""Example: 2024-01-01T00:00:00.000Z"""
    ),
    filter_taken_at_gt: datetime | None = typer.Option(
        None, "--filter-taken-at-gt", help=r"""Example: 2024-01-01T00:00:00.000Z"""
    ),
    filter_taken_at_gte: datetime | None = typer.Option(
        None, "--filter-taken-at-gte", help=r"""Example: 2024-01-01T00:00:00.000Z"""
    ),
    filter_taken_at_lt: datetime | None = typer.Option(
        None, "--filter-taken-at-lt", help=r"""Example: 2024-01-01T00:00:00.000Z"""
    ),
    filter_taken_at_lte: datetime | None = typer.Option(
        None, "--filter-taken-at-lte", help=r"""Example: 2024-01-01T00:00:00.000Z"""
    ),
    filter_taken_at_ne: datetime | None = typer.Option(
        None, "--filter-taken-at-ne", help=r"""Example: 2024-01-01T00:00:00.000Z"""
    ),
    filter_trashed_at_eq: datetime | None = typer.Option(
        None, "--filter-trashed-at-eq", help=r"""Example: 2024-01-01T00:00:00.000Z"""
    ),
    filter_trashed_at_gt: datetime | None = typer.Option(
        None, "--filter-trashed-at-gt", help=r"""Example: 2024-01-01T00:00:00.000Z"""
    ),
    filter_trashed_at_gte: datetime | None = typer.Option(
        None, "--filter-trashed-at-gte", help=r"""Example: 2024-01-01T00:00:00.000Z"""
    ),
    filter_trashed_at_lt: datetime | None = typer.Option(
        None, "--filter-trashed-at-lt", help=r"""Example: 2024-01-01T00:00:00.000Z"""
    ),
    filter_trashed_at_lte: datetime | None = typer.Option(
        None, "--filter-trashed-at-lte", help=r"""Example: 2024-01-01T00:00:00.000Z"""
    ),
    filter_trashed_at_ne: datetime | None = typer.Option(
        None, "--filter-trashed-at-ne", help=r"""Example: 2024-01-01T00:00:00.000Z"""
    ),
    filter_type_eq: AssetTypeEnum | None = typer.Option(
        None, "--filter-type-eq", help=r"""Asset type"""
    ),
    filter_type_in_: list[AssetTypeEnum] | None = typer.Option(
        None, "--filter-type-in", help=r""""""
    ),
    filter_type_ne: AssetTypeEnum | None = typer.Option(
        None, "--filter-type-ne", help=r"""Asset type"""
    ),
    filter_type_not_in: list[AssetTypeEnum] | None = typer.Option(
        None, "--filter-type-not-in", help=r""""""
    ),
    filter_updated_at_eq: datetime | None = typer.Option(
        None, "--filter-updated-at-eq", help=r"""Example: 2024-01-01T00:00:00.000Z"""
    ),
    filter_updated_at_gt: datetime | None = typer.Option(
        None, "--filter-updated-at-gt", help=r"""Example: 2024-01-01T00:00:00.000Z"""
    ),
    filter_updated_at_gte: datetime | None = typer.Option(
        None, "--filter-updated-at-gte", help=r"""Example: 2024-01-01T00:00:00.000Z"""
    ),
    filter_updated_at_lt: datetime | None = typer.Option(
        None, "--filter-updated-at-lt", help=r"""Example: 2024-01-01T00:00:00.000Z"""
    ),
    filter_updated_at_lte: datetime | None = typer.Option(
        None, "--filter-updated-at-lte", help=r"""Example: 2024-01-01T00:00:00.000Z"""
    ),
    filter_updated_at_ne: datetime | None = typer.Option(
        None, "--filter-updated-at-ne", help=r"""Example: 2024-01-01T00:00:00.000Z"""
    ),
    filter_visibility_eq: AssetVisibility | None = typer.Option(
        None, "--filter-visibility-eq", help=r"""Asset visibility"""
    ),
    filter_visibility_in_: list[AssetVisibility] | None = typer.Option(
        None, "--filter-visibility-in", help=r""""""
    ),
    filter_visibility_ne: AssetVisibility | None = typer.Option(
        None, "--filter-visibility-ne", help=r"""Asset visibility"""
    ),
    filter_visibility_not_in: list[AssetVisibility] | None = typer.Option(
        None, "--filter-visibility-not-in", help=r""""""
    ),
    is_encoded: Literal["true", "false"] | None = typer.Option(
        None, "--is-encoded", help=r"""Filter by encoded status"""
    ),
    is_favorite: Literal["true", "false"] | None = typer.Option(
        None, "--is-favorite", help=r"""Filter by favorite status"""
    ),
    is_motion: Literal["true", "false"] | None = typer.Option(
        None, "--is-motion", help=r"""Filter by motion photo status"""
    ),
    is_not_in_album: Literal["true", "false"] | None = typer.Option(
        None, "--is-not-in-album", help=r"""Filter assets not in any album"""
    ),
    is_offline: Literal["true", "false"] | None = typer.Option(
        None, "--is-offline", help=r"""Filter by offline status"""
    ),
    lens_model: str | None = typer.Option(
        None, "--lens-model", help=r"""Filter by lens model"""
    ),
    library_id: UUID | None = typer.Option(
        None, "--library-id", help=r"""Library ID to filter by"""
    ),
    make: str | None = typer.Option(None, "--make", help=r"""Filter by camera make"""),
    model: str | None = typer.Option(
        None, "--model", help=r"""Filter by camera model"""
    ),
    ocr: str | None = typer.Option(
        None, "--ocr", help=r"""Filter by OCR text content"""
    ),
    person_ids: list[UUID] | None = typer.Option(
        None, "--person-ids", help=r"""Filter by person IDs"""
    ),
    rating: int | None = typer.Option(
        None,
        "--rating",
        help=r"""Filter by rating [1-5], or null for unrated""",
        min=1,
        max=5,
    ),
    state: str | None = typer.Option(
        None, "--state", help=r"""Filter by state/province name"""
    ),
    tag_ids: list[UUID] | None = typer.Option(
        None, "--tag-ids", help=r"""Filter by tag IDs"""
    ),
    taken_after: datetime | None = typer.Option(
        None,
        "--taken-after",
        help=r"""Filter by taken date (after)

Example: 2024-01-01T00:00:00.000Z""",
    ),
    taken_before: datetime | None = typer.Option(
        None,
        "--taken-before",
        help=r"""Filter by taken date (before)

Example: 2024-01-01T00:00:00.000Z""",
    ),
    trashed_after: datetime | None = typer.Option(
        None,
        "--trashed-after",
        help=r"""Filter by trash date (after)

Example: 2024-01-01T00:00:00.000Z""",
    ),
    trashed_before: datetime | None = typer.Option(
        None,
        "--trashed-before",
        help=r"""Filter by trash date (before)

Example: 2024-01-01T00:00:00.000Z""",
    ),
    type: AssetTypeEnum | None = typer.Option(None, "--type", help=r"""Asset type"""),
    updated_after: datetime | None = typer.Option(
        None,
        "--updated-after",
        help=r"""Filter by update date (after)

Example: 2024-01-01T00:00:00.000Z""",
    ),
    updated_before: datetime | None = typer.Option(
        None,
        "--updated-before",
        help=r"""Filter by update date (before)

Example: 2024-01-01T00:00:00.000Z""",
    ),
    visibility: AssetVisibility | None = typer.Option(
        None, "--visibility", help=r"""Asset visibility"""
    ),
) -> None:
    """Search asset statistics

    [link=https://api.immich.app/endpoints/search/searchAssetStatistics]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    if album_ids is not None:
        set_nested(json_data, ["albumIds"], album_ids)
    if city is not None:
        set_nested(json_data, ["city"], city)
    if country is not None:
        set_nested(json_data, ["country"], country)
    if created_after is not None:
        set_nested(json_data, ["createdAfter"], created_after)
    if created_before is not None:
        set_nested(json_data, ["createdBefore"], created_before)
    if description is not None:
        set_nested(json_data, ["description"], description)
    if filter_album_ids_all is not None:
        set_nested(json_data, ["filter", "albumIds", "all"], filter_album_ids_all)
    if filter_album_ids_any is not None:
        set_nested(json_data, ["filter", "albumIds", "any"], filter_album_ids_any)
    if filter_album_ids_none is not None:
        set_nested(json_data, ["filter", "albumIds", "none"], filter_album_ids_none)
    if filter_checksum_eq is not None:
        set_nested(json_data, ["filter", "checksum", "eq"], filter_checksum_eq)
    if filter_checksum_in_ is not None:
        set_nested(json_data, ["filter", "checksum", "in"], filter_checksum_in_)
    if filter_checksum_ne is not None:
        set_nested(json_data, ["filter", "checksum", "ne"], filter_checksum_ne)
    if filter_checksum_not_in is not None:
        set_nested(json_data, ["filter", "checksum", "notIn"], filter_checksum_not_in)
    if filter_city_eq is not None:
        set_nested(json_data, ["filter", "city", "eq"], filter_city_eq)
    if filter_city_in_ is not None:
        set_nested(json_data, ["filter", "city", "in"], filter_city_in_)
    if filter_city_ne is not None:
        set_nested(json_data, ["filter", "city", "ne"], filter_city_ne)
    if filter_city_not_in is not None:
        set_nested(json_data, ["filter", "city", "notIn"], filter_city_not_in)
    if filter_country_eq is not None:
        set_nested(json_data, ["filter", "country", "eq"], filter_country_eq)
    if filter_country_in_ is not None:
        set_nested(json_data, ["filter", "country", "in"], filter_country_in_)
    if filter_country_ne is not None:
        set_nested(json_data, ["filter", "country", "ne"], filter_country_ne)
    if filter_country_not_in is not None:
        set_nested(json_data, ["filter", "country", "notIn"], filter_country_not_in)
    if filter_created_at_eq is not None:
        set_nested(json_data, ["filter", "createdAt", "eq"], filter_created_at_eq)
    if filter_created_at_gt is not None:
        set_nested(json_data, ["filter", "createdAt", "gt"], filter_created_at_gt)
    if filter_created_at_gte is not None:
        set_nested(json_data, ["filter", "createdAt", "gte"], filter_created_at_gte)
    if filter_created_at_lt is not None:
        set_nested(json_data, ["filter", "createdAt", "lt"], filter_created_at_lt)
    if filter_created_at_lte is not None:
        set_nested(json_data, ["filter", "createdAt", "lte"], filter_created_at_lte)
    if filter_created_at_ne is not None:
        set_nested(json_data, ["filter", "createdAt", "ne"], filter_created_at_ne)
    if filter_description_ends_with is not None:
        set_nested(
            json_data,
            ["filter", "description", "endsWith"],
            filter_description_ends_with,
        )
    if filter_description_eq is not None:
        set_nested(json_data, ["filter", "description", "eq"], filter_description_eq)
    if filter_description_in_ is not None:
        set_nested(json_data, ["filter", "description", "in"], filter_description_in_)
    if filter_description_like is not None:
        set_nested(
            json_data, ["filter", "description", "like"], filter_description_like
        )
    if filter_description_ne is not None:
        set_nested(json_data, ["filter", "description", "ne"], filter_description_ne)
    if filter_description_not_in is not None:
        set_nested(
            json_data, ["filter", "description", "notIn"], filter_description_not_in
        )
    if filter_description_not_like is not None:
        set_nested(
            json_data, ["filter", "description", "notLike"], filter_description_not_like
        )
    if filter_description_starts_with is not None:
        set_nested(
            json_data,
            ["filter", "description", "startsWith"],
            filter_description_starts_with,
        )
    if filter_encoded_video_path_eq is not None:
        set_nested(
            json_data,
            ["filter", "encodedVideoPath", "eq"],
            filter_encoded_video_path_eq,
        )
    if filter_encoded_video_path_in_ is not None:
        set_nested(
            json_data,
            ["filter", "encodedVideoPath", "in"],
            filter_encoded_video_path_in_,
        )
    if filter_encoded_video_path_ne is not None:
        set_nested(
            json_data,
            ["filter", "encodedVideoPath", "ne"],
            filter_encoded_video_path_ne,
        )
    if filter_encoded_video_path_not_in is not None:
        set_nested(
            json_data,
            ["filter", "encodedVideoPath", "notIn"],
            filter_encoded_video_path_not_in,
        )
    if filter_file_size_in_bytes_eq is not None:
        set_nested(
            json_data, ["filter", "fileSizeInBytes", "eq"], filter_file_size_in_bytes_eq
        )
    if filter_file_size_in_bytes_gt is not None:
        set_nested(
            json_data, ["filter", "fileSizeInBytes", "gt"], filter_file_size_in_bytes_gt
        )
    if filter_file_size_in_bytes_gte is not None:
        set_nested(
            json_data,
            ["filter", "fileSizeInBytes", "gte"],
            filter_file_size_in_bytes_gte,
        )
    if filter_file_size_in_bytes_in_ is not None:
        set_nested(
            json_data,
            ["filter", "fileSizeInBytes", "in"],
            filter_file_size_in_bytes_in_,
        )
    if filter_file_size_in_bytes_lt is not None:
        set_nested(
            json_data, ["filter", "fileSizeInBytes", "lt"], filter_file_size_in_bytes_lt
        )
    if filter_file_size_in_bytes_lte is not None:
        set_nested(
            json_data,
            ["filter", "fileSizeInBytes", "lte"],
            filter_file_size_in_bytes_lte,
        )
    if filter_file_size_in_bytes_ne is not None:
        set_nested(
            json_data, ["filter", "fileSizeInBytes", "ne"], filter_file_size_in_bytes_ne
        )
    if filter_file_size_in_bytes_not_in is not None:
        set_nested(
            json_data,
            ["filter", "fileSizeInBytes", "notIn"],
            filter_file_size_in_bytes_not_in,
        )
    if filter_has_albums_eq is not None:
        set_nested(
            json_data,
            ["filter", "hasAlbums", "eq"],
            filter_has_albums_eq.lower() == "true",
        )
    if filter_has_people_eq is not None:
        set_nested(
            json_data,
            ["filter", "hasPeople", "eq"],
            filter_has_people_eq.lower() == "true",
        )
    if filter_has_tags_eq is not None:
        set_nested(
            json_data, ["filter", "hasTags", "eq"], filter_has_tags_eq.lower() == "true"
        )
    if filter_id_eq is not None:
        set_nested(json_data, ["filter", "id", "eq"], filter_id_eq)
    if filter_id_ne is not None:
        set_nested(json_data, ["filter", "id", "ne"], filter_id_ne)
    if filter_is_encoded_eq is not None:
        set_nested(
            json_data,
            ["filter", "isEncoded", "eq"],
            filter_is_encoded_eq.lower() == "true",
        )
    if filter_is_favorite_eq is not None:
        set_nested(
            json_data,
            ["filter", "isFavorite", "eq"],
            filter_is_favorite_eq.lower() == "true",
        )
    if filter_is_motion_eq is not None:
        set_nested(
            json_data,
            ["filter", "isMotion", "eq"],
            filter_is_motion_eq.lower() == "true",
        )
    if filter_is_offline_eq is not None:
        set_nested(
            json_data,
            ["filter", "isOffline", "eq"],
            filter_is_offline_eq.lower() == "true",
        )
    if filter_lens_model_eq is not None:
        set_nested(json_data, ["filter", "lensModel", "eq"], filter_lens_model_eq)
    if filter_lens_model_in_ is not None:
        set_nested(json_data, ["filter", "lensModel", "in"], filter_lens_model_in_)
    if filter_lens_model_ne is not None:
        set_nested(json_data, ["filter", "lensModel", "ne"], filter_lens_model_ne)
    if filter_lens_model_not_in is not None:
        set_nested(
            json_data, ["filter", "lensModel", "notIn"], filter_lens_model_not_in
        )
    if filter_library_id_eq is not None:
        set_nested(json_data, ["filter", "libraryId", "eq"], filter_library_id_eq)
    if filter_library_id_ne is not None:
        set_nested(json_data, ["filter", "libraryId", "ne"], filter_library_id_ne)
    if filter_make_eq is not None:
        set_nested(json_data, ["filter", "make", "eq"], filter_make_eq)
    if filter_make_in_ is not None:
        set_nested(json_data, ["filter", "make", "in"], filter_make_in_)
    if filter_make_ne is not None:
        set_nested(json_data, ["filter", "make", "ne"], filter_make_ne)
    if filter_make_not_in is not None:
        set_nested(json_data, ["filter", "make", "notIn"], filter_make_not_in)
    if filter_model_eq is not None:
        set_nested(json_data, ["filter", "model", "eq"], filter_model_eq)
    if filter_model_in_ is not None:
        set_nested(json_data, ["filter", "model", "in"], filter_model_in_)
    if filter_model_ne is not None:
        set_nested(json_data, ["filter", "model", "ne"], filter_model_ne)
    if filter_model_not_in is not None:
        set_nested(json_data, ["filter", "model", "notIn"], filter_model_not_in)
    if filter_ocr_matches is not None:
        set_nested(json_data, ["filter", "ocr", "matches"], filter_ocr_matches)
    if filter_or_ is not None:
        value_filter_or_ = parse_json_options(filter_or_, "--filter-or", ctx=ctx)
        set_nested(json_data, ["filter", "or"], value_filter_or_)
    if filter_original_file_name_ends_with is not None:
        set_nested(
            json_data,
            ["filter", "originalFileName", "endsWith"],
            filter_original_file_name_ends_with,
        )
    if filter_original_file_name_eq is not None:
        set_nested(
            json_data,
            ["filter", "originalFileName", "eq"],
            filter_original_file_name_eq,
        )
    if filter_original_file_name_in_ is not None:
        set_nested(
            json_data,
            ["filter", "originalFileName", "in"],
            filter_original_file_name_in_,
        )
    if filter_original_file_name_like is not None:
        set_nested(
            json_data,
            ["filter", "originalFileName", "like"],
            filter_original_file_name_like,
        )
    if filter_original_file_name_ne is not None:
        set_nested(
            json_data,
            ["filter", "originalFileName", "ne"],
            filter_original_file_name_ne,
        )
    if filter_original_file_name_not_in is not None:
        set_nested(
            json_data,
            ["filter", "originalFileName", "notIn"],
            filter_original_file_name_not_in,
        )
    if filter_original_file_name_not_like is not None:
        set_nested(
            json_data,
            ["filter", "originalFileName", "notLike"],
            filter_original_file_name_not_like,
        )
    if filter_original_file_name_starts_with is not None:
        set_nested(
            json_data,
            ["filter", "originalFileName", "startsWith"],
            filter_original_file_name_starts_with,
        )
    if filter_original_path_ends_with is not None:
        set_nested(
            json_data,
            ["filter", "originalPath", "endsWith"],
            filter_original_path_ends_with,
        )
    if filter_original_path_eq is not None:
        set_nested(json_data, ["filter", "originalPath", "eq"], filter_original_path_eq)
    if filter_original_path_in_ is not None:
        set_nested(
            json_data, ["filter", "originalPath", "in"], filter_original_path_in_
        )
    if filter_original_path_like is not None:
        set_nested(
            json_data, ["filter", "originalPath", "like"], filter_original_path_like
        )
    if filter_original_path_ne is not None:
        set_nested(json_data, ["filter", "originalPath", "ne"], filter_original_path_ne)
    if filter_original_path_not_in is not None:
        set_nested(
            json_data, ["filter", "originalPath", "notIn"], filter_original_path_not_in
        )
    if filter_original_path_not_like is not None:
        set_nested(
            json_data,
            ["filter", "originalPath", "notLike"],
            filter_original_path_not_like,
        )
    if filter_original_path_starts_with is not None:
        set_nested(
            json_data,
            ["filter", "originalPath", "startsWith"],
            filter_original_path_starts_with,
        )
    if filter_person_ids_all is not None:
        set_nested(json_data, ["filter", "personIds", "all"], filter_person_ids_all)
    if filter_person_ids_any is not None:
        set_nested(json_data, ["filter", "personIds", "any"], filter_person_ids_any)
    if filter_person_ids_none is not None:
        set_nested(json_data, ["filter", "personIds", "none"], filter_person_ids_none)
    if filter_rating_eq is not None:
        set_nested(json_data, ["filter", "rating", "eq"], filter_rating_eq)
    if filter_rating_gt is not None:
        set_nested(json_data, ["filter", "rating", "gt"], filter_rating_gt)
    if filter_rating_gte is not None:
        set_nested(json_data, ["filter", "rating", "gte"], filter_rating_gte)
    if filter_rating_in_ is not None:
        set_nested(json_data, ["filter", "rating", "in"], filter_rating_in_)
    if filter_rating_lt is not None:
        set_nested(json_data, ["filter", "rating", "lt"], filter_rating_lt)
    if filter_rating_lte is not None:
        set_nested(json_data, ["filter", "rating", "lte"], filter_rating_lte)
    if filter_rating_ne is not None:
        set_nested(json_data, ["filter", "rating", "ne"], filter_rating_ne)
    if filter_rating_not_in is not None:
        set_nested(json_data, ["filter", "rating", "notIn"], filter_rating_not_in)
    if filter_state_eq is not None:
        set_nested(json_data, ["filter", "state", "eq"], filter_state_eq)
    if filter_state_in_ is not None:
        set_nested(json_data, ["filter", "state", "in"], filter_state_in_)
    if filter_state_ne is not None:
        set_nested(json_data, ["filter", "state", "ne"], filter_state_ne)
    if filter_state_not_in is not None:
        set_nested(json_data, ["filter", "state", "notIn"], filter_state_not_in)
    if filter_tag_ids_all is not None:
        set_nested(json_data, ["filter", "tagIds", "all"], filter_tag_ids_all)
    if filter_tag_ids_any is not None:
        set_nested(json_data, ["filter", "tagIds", "any"], filter_tag_ids_any)
    if filter_tag_ids_none is not None:
        set_nested(json_data, ["filter", "tagIds", "none"], filter_tag_ids_none)
    if filter_taken_at_eq is not None:
        set_nested(json_data, ["filter", "takenAt", "eq"], filter_taken_at_eq)
    if filter_taken_at_gt is not None:
        set_nested(json_data, ["filter", "takenAt", "gt"], filter_taken_at_gt)
    if filter_taken_at_gte is not None:
        set_nested(json_data, ["filter", "takenAt", "gte"], filter_taken_at_gte)
    if filter_taken_at_lt is not None:
        set_nested(json_data, ["filter", "takenAt", "lt"], filter_taken_at_lt)
    if filter_taken_at_lte is not None:
        set_nested(json_data, ["filter", "takenAt", "lte"], filter_taken_at_lte)
    if filter_taken_at_ne is not None:
        set_nested(json_data, ["filter", "takenAt", "ne"], filter_taken_at_ne)
    if filter_trashed_at_eq is not None:
        set_nested(json_data, ["filter", "trashedAt", "eq"], filter_trashed_at_eq)
    if filter_trashed_at_gt is not None:
        set_nested(json_data, ["filter", "trashedAt", "gt"], filter_trashed_at_gt)
    if filter_trashed_at_gte is not None:
        set_nested(json_data, ["filter", "trashedAt", "gte"], filter_trashed_at_gte)
    if filter_trashed_at_lt is not None:
        set_nested(json_data, ["filter", "trashedAt", "lt"], filter_trashed_at_lt)
    if filter_trashed_at_lte is not None:
        set_nested(json_data, ["filter", "trashedAt", "lte"], filter_trashed_at_lte)
    if filter_trashed_at_ne is not None:
        set_nested(json_data, ["filter", "trashedAt", "ne"], filter_trashed_at_ne)
    if filter_type_eq is not None:
        set_nested(json_data, ["filter", "type", "eq"], filter_type_eq)
    if filter_type_in_ is not None:
        set_nested(json_data, ["filter", "type", "in"], filter_type_in_)
    if filter_type_ne is not None:
        set_nested(json_data, ["filter", "type", "ne"], filter_type_ne)
    if filter_type_not_in is not None:
        set_nested(json_data, ["filter", "type", "notIn"], filter_type_not_in)
    if filter_updated_at_eq is not None:
        set_nested(json_data, ["filter", "updatedAt", "eq"], filter_updated_at_eq)
    if filter_updated_at_gt is not None:
        set_nested(json_data, ["filter", "updatedAt", "gt"], filter_updated_at_gt)
    if filter_updated_at_gte is not None:
        set_nested(json_data, ["filter", "updatedAt", "gte"], filter_updated_at_gte)
    if filter_updated_at_lt is not None:
        set_nested(json_data, ["filter", "updatedAt", "lt"], filter_updated_at_lt)
    if filter_updated_at_lte is not None:
        set_nested(json_data, ["filter", "updatedAt", "lte"], filter_updated_at_lte)
    if filter_updated_at_ne is not None:
        set_nested(json_data, ["filter", "updatedAt", "ne"], filter_updated_at_ne)
    if filter_visibility_eq is not None:
        set_nested(json_data, ["filter", "visibility", "eq"], filter_visibility_eq)
    if filter_visibility_in_ is not None:
        set_nested(json_data, ["filter", "visibility", "in"], filter_visibility_in_)
    if filter_visibility_ne is not None:
        set_nested(json_data, ["filter", "visibility", "ne"], filter_visibility_ne)
    if filter_visibility_not_in is not None:
        set_nested(
            json_data, ["filter", "visibility", "notIn"], filter_visibility_not_in
        )
    if is_encoded is not None:
        set_nested(json_data, ["isEncoded"], is_encoded.lower() == "true")
    if is_favorite is not None:
        set_nested(json_data, ["isFavorite"], is_favorite.lower() == "true")
    if is_motion is not None:
        set_nested(json_data, ["isMotion"], is_motion.lower() == "true")
    if is_not_in_album is not None:
        set_nested(json_data, ["isNotInAlbum"], is_not_in_album.lower() == "true")
    if is_offline is not None:
        set_nested(json_data, ["isOffline"], is_offline.lower() == "true")
    if lens_model is not None:
        set_nested(json_data, ["lensModel"], lens_model)
    if library_id is not None:
        set_nested(json_data, ["libraryId"], library_id)
    if make is not None:
        set_nested(json_data, ["make"], make)
    if model is not None:
        set_nested(json_data, ["model"], model)
    if ocr is not None:
        set_nested(json_data, ["ocr"], ocr)
    if person_ids is not None:
        set_nested(json_data, ["personIds"], person_ids)
    if rating is not None:
        set_nested(json_data, ["rating"], rating)
    if state is not None:
        set_nested(json_data, ["state"], state)
    if tag_ids is not None:
        set_nested(json_data, ["tagIds"], tag_ids)
    if taken_after is not None:
        set_nested(json_data, ["takenAfter"], taken_after)
    if taken_before is not None:
        set_nested(json_data, ["takenBefore"], taken_before)
    if trashed_after is not None:
        set_nested(json_data, ["trashedAfter"], trashed_after)
    if trashed_before is not None:
        set_nested(json_data, ["trashedBefore"], trashed_before)
    if type is not None:
        set_nested(json_data, ["type"], type)
    if updated_after is not None:
        set_nested(json_data, ["updatedAfter"], updated_after)
    if updated_before is not None:
        set_nested(json_data, ["updatedBefore"], updated_before)
    if visibility is not None:
        set_nested(json_data, ["visibility"], visibility)
    statistics_search_dto = StatisticsSearchDto.model_validate(json_data)
    kwargs["statistics_search_dto"] = statistics_search_dto
    client: AsyncClient = ctx.obj["client"]
    result = run_command(client.search.search_asset_statistics, ctx=ctx, **kwargs)
    print_response(result, ctx=ctx)


@app.command("search-assets", deprecated=False, rich_help_panel="API commands")
def search_assets(
    ctx: typer.Context,
    album_ids: list[UUID] | None = typer.Option(
        None, "--album-ids", help=r"""Filter by album IDs"""
    ),
    checksum: str | None = typer.Option(
        None, "--checksum", help=r"""Filter by file checksum"""
    ),
    city: str | None = typer.Option(None, "--city", help=r"""Filter by city name"""),
    country: str | None = typer.Option(
        None, "--country", help=r"""Filter by country name"""
    ),
    created_after: datetime | None = typer.Option(
        None,
        "--created-after",
        help=r"""Filter by creation date (after)

Example: 2024-01-01T00:00:00.000Z""",
    ),
    created_before: datetime | None = typer.Option(
        None,
        "--created-before",
        help=r"""Filter by creation date (before)

Example: 2024-01-01T00:00:00.000Z""",
    ),
    cursor: str | None = typer.Option(
        None, "--cursor", help=r"""Cursor for the next page of results"""
    ),
    description: str | None = typer.Option(
        None, "--description", help=r"""Filter by description text"""
    ),
    encoded_video_path: str | None = typer.Option(
        None, "--encoded-video-path", help=r"""Filter by encoded video file path"""
    ),
    filter_album_ids_all: list[UUID] | None = typer.Option(
        None, "--filter-album-ids-all", help=r""""""
    ),
    filter_album_ids_any: list[UUID] | None = typer.Option(
        None, "--filter-album-ids-any", help=r""""""
    ),
    filter_album_ids_none: list[UUID] | None = typer.Option(
        None, "--filter-album-ids-none", help=r""""""
    ),
    filter_checksum_eq: str | None = typer.Option(
        None, "--filter-checksum-eq", help=r""""""
    ),
    filter_checksum_in_: list[str] | None = typer.Option(
        None, "--filter-checksum-in", help=r""""""
    ),
    filter_checksum_ne: str | None = typer.Option(
        None, "--filter-checksum-ne", help=r""""""
    ),
    filter_checksum_not_in: list[str] | None = typer.Option(
        None, "--filter-checksum-not-in", help=r""""""
    ),
    filter_city_eq: str | None = typer.Option(None, "--filter-city-eq", help=r""""""),
    filter_city_in_: list[str] | None = typer.Option(
        None, "--filter-city-in", help=r""""""
    ),
    filter_city_ne: str | None = typer.Option(None, "--filter-city-ne", help=r""""""),
    filter_city_not_in: list[str] | None = typer.Option(
        None, "--filter-city-not-in", help=r""""""
    ),
    filter_country_eq: str | None = typer.Option(
        None, "--filter-country-eq", help=r""""""
    ),
    filter_country_in_: list[str] | None = typer.Option(
        None, "--filter-country-in", help=r""""""
    ),
    filter_country_ne: str | None = typer.Option(
        None, "--filter-country-ne", help=r""""""
    ),
    filter_country_not_in: list[str] | None = typer.Option(
        None, "--filter-country-not-in", help=r""""""
    ),
    filter_created_at_eq: datetime | None = typer.Option(
        None, "--filter-created-at-eq", help=r"""Example: 2024-01-01T00:00:00.000Z"""
    ),
    filter_created_at_gt: datetime | None = typer.Option(
        None, "--filter-created-at-gt", help=r"""Example: 2024-01-01T00:00:00.000Z"""
    ),
    filter_created_at_gte: datetime | None = typer.Option(
        None, "--filter-created-at-gte", help=r"""Example: 2024-01-01T00:00:00.000Z"""
    ),
    filter_created_at_lt: datetime | None = typer.Option(
        None, "--filter-created-at-lt", help=r"""Example: 2024-01-01T00:00:00.000Z"""
    ),
    filter_created_at_lte: datetime | None = typer.Option(
        None, "--filter-created-at-lte", help=r"""Example: 2024-01-01T00:00:00.000Z"""
    ),
    filter_created_at_ne: datetime | None = typer.Option(
        None, "--filter-created-at-ne", help=r"""Example: 2024-01-01T00:00:00.000Z"""
    ),
    filter_description_ends_with: str | None = typer.Option(
        None, "--filter-description-ends-with", help=r""""""
    ),
    filter_description_eq: str | None = typer.Option(
        None, "--filter-description-eq", help=r""""""
    ),
    filter_description_in_: list[str] | None = typer.Option(
        None, "--filter-description-in", help=r""""""
    ),
    filter_description_like: str | None = typer.Option(
        None, "--filter-description-like", help=r""""""
    ),
    filter_description_ne: str | None = typer.Option(
        None, "--filter-description-ne", help=r""""""
    ),
    filter_description_not_in: list[str] | None = typer.Option(
        None, "--filter-description-not-in", help=r""""""
    ),
    filter_description_not_like: str | None = typer.Option(
        None, "--filter-description-not-like", help=r""""""
    ),
    filter_description_starts_with: str | None = typer.Option(
        None, "--filter-description-starts-with", help=r""""""
    ),
    filter_encoded_video_path_eq: str | None = typer.Option(
        None, "--filter-encoded-video-path-eq", help=r""""""
    ),
    filter_encoded_video_path_in_: list[str] | None = typer.Option(
        None, "--filter-encoded-video-path-in", help=r""""""
    ),
    filter_encoded_video_path_ne: str | None = typer.Option(
        None, "--filter-encoded-video-path-ne", help=r""""""
    ),
    filter_encoded_video_path_not_in: list[str] | None = typer.Option(
        None, "--filter-encoded-video-path-not-in", help=r""""""
    ),
    filter_file_size_in_bytes_eq: float | None = typer.Option(
        None, "--filter-file-size-in-bytes-eq", help=r""""""
    ),
    filter_file_size_in_bytes_gt: float | None = typer.Option(
        None, "--filter-file-size-in-bytes-gt", help=r""""""
    ),
    filter_file_size_in_bytes_gte: float | None = typer.Option(
        None, "--filter-file-size-in-bytes-gte", help=r""""""
    ),
    filter_file_size_in_bytes_in_: list[float] | None = typer.Option(
        None, "--filter-file-size-in-bytes-in", help=r""""""
    ),
    filter_file_size_in_bytes_lt: float | None = typer.Option(
        None, "--filter-file-size-in-bytes-lt", help=r""""""
    ),
    filter_file_size_in_bytes_lte: float | None = typer.Option(
        None, "--filter-file-size-in-bytes-lte", help=r""""""
    ),
    filter_file_size_in_bytes_ne: float | None = typer.Option(
        None, "--filter-file-size-in-bytes-ne", help=r""""""
    ),
    filter_file_size_in_bytes_not_in: list[float] | None = typer.Option(
        None, "--filter-file-size-in-bytes-not-in", help=r""""""
    ),
    filter_has_albums_eq: Literal["true", "false"] | None = typer.Option(
        None, "--filter-has-albums-eq", help=r""""""
    ),
    filter_has_people_eq: Literal["true", "false"] | None = typer.Option(
        None, "--filter-has-people-eq", help=r""""""
    ),
    filter_has_tags_eq: Literal["true", "false"] | None = typer.Option(
        None, "--filter-has-tags-eq", help=r""""""
    ),
    filter_id_eq: UUID | None = typer.Option(None, "--filter-id-eq", help=r""""""),
    filter_id_ne: UUID | None = typer.Option(None, "--filter-id-ne", help=r""""""),
    filter_is_encoded_eq: Literal["true", "false"] | None = typer.Option(
        None, "--filter-is-encoded-eq", help=r""""""
    ),
    filter_is_favorite_eq: Literal["true", "false"] | None = typer.Option(
        None, "--filter-is-favorite-eq", help=r""""""
    ),
    filter_is_motion_eq: Literal["true", "false"] | None = typer.Option(
        None, "--filter-is-motion-eq", help=r""""""
    ),
    filter_is_offline_eq: Literal["true", "false"] | None = typer.Option(
        None, "--filter-is-offline-eq", help=r""""""
    ),
    filter_lens_model_eq: str | None = typer.Option(
        None, "--filter-lens-model-eq", help=r""""""
    ),
    filter_lens_model_in_: list[str] | None = typer.Option(
        None, "--filter-lens-model-in", help=r""""""
    ),
    filter_lens_model_ne: str | None = typer.Option(
        None, "--filter-lens-model-ne", help=r""""""
    ),
    filter_lens_model_not_in: list[str] | None = typer.Option(
        None, "--filter-lens-model-not-in", help=r""""""
    ),
    filter_library_id_eq: UUID | None = typer.Option(
        None, "--filter-library-id-eq", help=r""""""
    ),
    filter_library_id_ne: UUID | None = typer.Option(
        None, "--filter-library-id-ne", help=r""""""
    ),
    filter_make_eq: str | None = typer.Option(None, "--filter-make-eq", help=r""""""),
    filter_make_in_: list[str] | None = typer.Option(
        None, "--filter-make-in", help=r""""""
    ),
    filter_make_ne: str | None = typer.Option(None, "--filter-make-ne", help=r""""""),
    filter_make_not_in: list[str] | None = typer.Option(
        None, "--filter-make-not-in", help=r""""""
    ),
    filter_model_eq: str | None = typer.Option(None, "--filter-model-eq", help=r""""""),
    filter_model_in_: list[str] | None = typer.Option(
        None, "--filter-model-in", help=r""""""
    ),
    filter_model_ne: str | None = typer.Option(None, "--filter-model-ne", help=r""""""),
    filter_model_not_in: list[str] | None = typer.Option(
        None, "--filter-model-not-in", help=r""""""
    ),
    filter_ocr_matches: str | None = typer.Option(
        None, "--filter-ocr-matches", help=r""""""
    ),
    filter_or_: list[str] | None = typer.Option(
        None,
        "--filter-or",
        help=r"""As a JSON string with keys: albumIds (object), checksum (object), city (object), country (object), createdAt (object), description (object), encodedVideoPath (object), fileSizeInBytes (object), hasAlbums (object), hasPeople (object), hasTags (object), id (object), isEncoded (object), isFavorite (object), isMotion (object), isOffline (object), lensModel (object), libraryId (object), make (object), model (object), ocr (object), originalFileName (object), originalPath (object), personIds (object), rating (object), state (object), tagIds (object), takenAt (object), trashedAt (object), type (object), updatedAt (object), visibility (object)""",
    ),
    filter_original_file_name_ends_with: str | None = typer.Option(
        None, "--filter-original-file-name-ends-with", help=r""""""
    ),
    filter_original_file_name_eq: str | None = typer.Option(
        None, "--filter-original-file-name-eq", help=r""""""
    ),
    filter_original_file_name_in_: list[str] | None = typer.Option(
        None, "--filter-original-file-name-in", help=r""""""
    ),
    filter_original_file_name_like: str | None = typer.Option(
        None, "--filter-original-file-name-like", help=r""""""
    ),
    filter_original_file_name_ne: str | None = typer.Option(
        None, "--filter-original-file-name-ne", help=r""""""
    ),
    filter_original_file_name_not_in: list[str] | None = typer.Option(
        None, "--filter-original-file-name-not-in", help=r""""""
    ),
    filter_original_file_name_not_like: str | None = typer.Option(
        None, "--filter-original-file-name-not-like", help=r""""""
    ),
    filter_original_file_name_starts_with: str | None = typer.Option(
        None, "--filter-original-file-name-starts-with", help=r""""""
    ),
    filter_original_path_ends_with: str | None = typer.Option(
        None, "--filter-original-path-ends-with", help=r""""""
    ),
    filter_original_path_eq: str | None = typer.Option(
        None, "--filter-original-path-eq", help=r""""""
    ),
    filter_original_path_in_: list[str] | None = typer.Option(
        None, "--filter-original-path-in", help=r""""""
    ),
    filter_original_path_like: str | None = typer.Option(
        None, "--filter-original-path-like", help=r""""""
    ),
    filter_original_path_ne: str | None = typer.Option(
        None, "--filter-original-path-ne", help=r""""""
    ),
    filter_original_path_not_in: list[str] | None = typer.Option(
        None, "--filter-original-path-not-in", help=r""""""
    ),
    filter_original_path_not_like: str | None = typer.Option(
        None, "--filter-original-path-not-like", help=r""""""
    ),
    filter_original_path_starts_with: str | None = typer.Option(
        None, "--filter-original-path-starts-with", help=r""""""
    ),
    filter_person_ids_all: list[UUID] | None = typer.Option(
        None, "--filter-person-ids-all", help=r""""""
    ),
    filter_person_ids_any: list[UUID] | None = typer.Option(
        None, "--filter-person-ids-any", help=r""""""
    ),
    filter_person_ids_none: list[UUID] | None = typer.Option(
        None, "--filter-person-ids-none", help=r""""""
    ),
    filter_rating_eq: float | None = typer.Option(
        None, "--filter-rating-eq", help=r""""""
    ),
    filter_rating_gt: float | None = typer.Option(
        None, "--filter-rating-gt", help=r""""""
    ),
    filter_rating_gte: float | None = typer.Option(
        None, "--filter-rating-gte", help=r""""""
    ),
    filter_rating_in_: list[float] | None = typer.Option(
        None, "--filter-rating-in", help=r""""""
    ),
    filter_rating_lt: float | None = typer.Option(
        None, "--filter-rating-lt", help=r""""""
    ),
    filter_rating_lte: float | None = typer.Option(
        None, "--filter-rating-lte", help=r""""""
    ),
    filter_rating_ne: float | None = typer.Option(
        None, "--filter-rating-ne", help=r""""""
    ),
    filter_rating_not_in: list[float] | None = typer.Option(
        None, "--filter-rating-not-in", help=r""""""
    ),
    filter_state_eq: str | None = typer.Option(None, "--filter-state-eq", help=r""""""),
    filter_state_in_: list[str] | None = typer.Option(
        None, "--filter-state-in", help=r""""""
    ),
    filter_state_ne: str | None = typer.Option(None, "--filter-state-ne", help=r""""""),
    filter_state_not_in: list[str] | None = typer.Option(
        None, "--filter-state-not-in", help=r""""""
    ),
    filter_tag_ids_all: list[UUID] | None = typer.Option(
        None, "--filter-tag-ids-all", help=r""""""
    ),
    filter_tag_ids_any: list[UUID] | None = typer.Option(
        None, "--filter-tag-ids-any", help=r""""""
    ),
    filter_tag_ids_none: list[UUID] | None = typer.Option(
        None, "--filter-tag-ids-none", help=r""""""
    ),
    filter_taken_at_eq: datetime | None = typer.Option(
        None, "--filter-taken-at-eq", help=r"""Example: 2024-01-01T00:00:00.000Z"""
    ),
    filter_taken_at_gt: datetime | None = typer.Option(
        None, "--filter-taken-at-gt", help=r"""Example: 2024-01-01T00:00:00.000Z"""
    ),
    filter_taken_at_gte: datetime | None = typer.Option(
        None, "--filter-taken-at-gte", help=r"""Example: 2024-01-01T00:00:00.000Z"""
    ),
    filter_taken_at_lt: datetime | None = typer.Option(
        None, "--filter-taken-at-lt", help=r"""Example: 2024-01-01T00:00:00.000Z"""
    ),
    filter_taken_at_lte: datetime | None = typer.Option(
        None, "--filter-taken-at-lte", help=r"""Example: 2024-01-01T00:00:00.000Z"""
    ),
    filter_taken_at_ne: datetime | None = typer.Option(
        None, "--filter-taken-at-ne", help=r"""Example: 2024-01-01T00:00:00.000Z"""
    ),
    filter_trashed_at_eq: datetime | None = typer.Option(
        None, "--filter-trashed-at-eq", help=r"""Example: 2024-01-01T00:00:00.000Z"""
    ),
    filter_trashed_at_gt: datetime | None = typer.Option(
        None, "--filter-trashed-at-gt", help=r"""Example: 2024-01-01T00:00:00.000Z"""
    ),
    filter_trashed_at_gte: datetime | None = typer.Option(
        None, "--filter-trashed-at-gte", help=r"""Example: 2024-01-01T00:00:00.000Z"""
    ),
    filter_trashed_at_lt: datetime | None = typer.Option(
        None, "--filter-trashed-at-lt", help=r"""Example: 2024-01-01T00:00:00.000Z"""
    ),
    filter_trashed_at_lte: datetime | None = typer.Option(
        None, "--filter-trashed-at-lte", help=r"""Example: 2024-01-01T00:00:00.000Z"""
    ),
    filter_trashed_at_ne: datetime | None = typer.Option(
        None, "--filter-trashed-at-ne", help=r"""Example: 2024-01-01T00:00:00.000Z"""
    ),
    filter_type_eq: AssetTypeEnum | None = typer.Option(
        None, "--filter-type-eq", help=r"""Asset type"""
    ),
    filter_type_in_: list[AssetTypeEnum] | None = typer.Option(
        None, "--filter-type-in", help=r""""""
    ),
    filter_type_ne: AssetTypeEnum | None = typer.Option(
        None, "--filter-type-ne", help=r"""Asset type"""
    ),
    filter_type_not_in: list[AssetTypeEnum] | None = typer.Option(
        None, "--filter-type-not-in", help=r""""""
    ),
    filter_updated_at_eq: datetime | None = typer.Option(
        None, "--filter-updated-at-eq", help=r"""Example: 2024-01-01T00:00:00.000Z"""
    ),
    filter_updated_at_gt: datetime | None = typer.Option(
        None, "--filter-updated-at-gt", help=r"""Example: 2024-01-01T00:00:00.000Z"""
    ),
    filter_updated_at_gte: datetime | None = typer.Option(
        None, "--filter-updated-at-gte", help=r"""Example: 2024-01-01T00:00:00.000Z"""
    ),
    filter_updated_at_lt: datetime | None = typer.Option(
        None, "--filter-updated-at-lt", help=r"""Example: 2024-01-01T00:00:00.000Z"""
    ),
    filter_updated_at_lte: datetime | None = typer.Option(
        None, "--filter-updated-at-lte", help=r"""Example: 2024-01-01T00:00:00.000Z"""
    ),
    filter_updated_at_ne: datetime | None = typer.Option(
        None, "--filter-updated-at-ne", help=r"""Example: 2024-01-01T00:00:00.000Z"""
    ),
    filter_visibility_eq: AssetVisibility | None = typer.Option(
        None, "--filter-visibility-eq", help=r"""Asset visibility"""
    ),
    filter_visibility_in_: list[AssetVisibility] | None = typer.Option(
        None, "--filter-visibility-in", help=r""""""
    ),
    filter_visibility_ne: AssetVisibility | None = typer.Option(
        None, "--filter-visibility-ne", help=r"""Asset visibility"""
    ),
    filter_visibility_not_in: list[AssetVisibility] | None = typer.Option(
        None, "--filter-visibility-not-in", help=r""""""
    ),
    id: UUID | None = typer.Option(None, "--id", help=r"""Filter by asset ID"""),
    is_encoded: Literal["true", "false"] | None = typer.Option(
        None, "--is-encoded", help=r"""Filter by encoded status"""
    ),
    is_favorite: Literal["true", "false"] | None = typer.Option(
        None, "--is-favorite", help=r"""Filter by favorite status"""
    ),
    is_motion: Literal["true", "false"] | None = typer.Option(
        None, "--is-motion", help=r"""Filter by motion photo status"""
    ),
    is_not_in_album: Literal["true", "false"] | None = typer.Option(
        None, "--is-not-in-album", help=r"""Filter assets not in any album"""
    ),
    is_offline: Literal["true", "false"] | None = typer.Option(
        None, "--is-offline", help=r"""Filter by offline status"""
    ),
    key: str | None = typer.Option(None, "--key", help=r""""""),
    lens_model: str | None = typer.Option(
        None, "--lens-model", help=r"""Filter by lens model"""
    ),
    library_id: UUID | None = typer.Option(
        None, "--library-id", help=r"""Library ID to filter by"""
    ),
    make: str | None = typer.Option(None, "--make", help=r"""Filter by camera make"""),
    model: str | None = typer.Option(
        None, "--model", help=r"""Filter by camera model"""
    ),
    ocr: str | None = typer.Option(
        None, "--ocr", help=r"""Filter by OCR text content"""
    ),
    order: AssetOrder | None = typer.Option(
        None, "--order", help=r"""Asset sort order"""
    ),
    order_by_direction: AssetOrder | None = typer.Option(
        None, "--order-by-direction", help=r"""Asset sort order"""
    ),
    order_by_field: SearchOrderField | None = typer.Option(
        None, "--order-by-field", help=r""""""
    ),
    original_file_name: str | None = typer.Option(
        None, "--original-file-name", help=r"""Filter by original file name"""
    ),
    original_path: str | None = typer.Option(
        None, "--original-path", help=r"""Filter by original file path"""
    ),
    page: int | None = typer.Option(
        None, "--page", help=r"""Page number""", min=1, max=9007199254740991
    ),
    person_ids: list[UUID] | None = typer.Option(
        None, "--person-ids", help=r"""Filter by person IDs"""
    ),
    preview_path: str | None = typer.Option(
        None, "--preview-path", help=r"""Filter by preview file path"""
    ),
    rating: int | None = typer.Option(
        None,
        "--rating",
        help=r"""Filter by rating [1-5], or null for unrated""",
        min=1,
        max=5,
    ),
    size: int | None = typer.Option(
        None, "--size", help=r"""Number of results to return""", min=1, max=1000
    ),
    slug: str | None = typer.Option(None, "--slug", help=r""""""),
    state: str | None = typer.Option(
        None, "--state", help=r"""Filter by state/province name"""
    ),
    tag_ids: list[UUID] | None = typer.Option(
        None, "--tag-ids", help=r"""Filter by tag IDs"""
    ),
    taken_after: datetime | None = typer.Option(
        None,
        "--taken-after",
        help=r"""Filter by taken date (after)

Example: 2024-01-01T00:00:00.000Z""",
    ),
    taken_before: datetime | None = typer.Option(
        None,
        "--taken-before",
        help=r"""Filter by taken date (before)

Example: 2024-01-01T00:00:00.000Z""",
    ),
    thumbnail_path: str | None = typer.Option(
        None, "--thumbnail-path", help=r"""Filter by thumbnail file path"""
    ),
    trashed_after: datetime | None = typer.Option(
        None,
        "--trashed-after",
        help=r"""Filter by trash date (after)

Example: 2024-01-01T00:00:00.000Z""",
    ),
    trashed_before: datetime | None = typer.Option(
        None,
        "--trashed-before",
        help=r"""Filter by trash date (before)

Example: 2024-01-01T00:00:00.000Z""",
    ),
    type: AssetTypeEnum | None = typer.Option(None, "--type", help=r"""Asset type"""),
    updated_after: datetime | None = typer.Option(
        None,
        "--updated-after",
        help=r"""Filter by update date (after)

Example: 2024-01-01T00:00:00.000Z""",
    ),
    updated_before: datetime | None = typer.Option(
        None,
        "--updated-before",
        help=r"""Filter by update date (before)

Example: 2024-01-01T00:00:00.000Z""",
    ),
    visibility: AssetVisibility | None = typer.Option(
        None, "--visibility", help=r"""Asset visibility"""
    ),
    with_deleted: Literal["true", "false"] | None = typer.Option(
        None, "--with-deleted", help=r"""Include deleted assets"""
    ),
    with_exif: Literal["true", "false"] | None = typer.Option(
        None, "--with-exif", help=r"""Include EXIF data in response"""
    ),
    with_people: Literal["true", "false"] | None = typer.Option(
        None, "--with-people", help=r"""Include people data in response"""
    ),
    with_stacked: Literal["true", "false"] | None = typer.Option(
        None, "--with-stacked", help=r"""Include stacked assets"""
    ),
) -> None:
    """Search assets by metadata

    [link=https://api.immich.app/endpoints/search/searchAssets]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    if key is not None:
        kwargs["key"] = key
    if slug is not None:
        kwargs["slug"] = slug
    if album_ids is not None:
        set_nested(json_data, ["albumIds"], album_ids)
    if checksum is not None:
        set_nested(json_data, ["checksum"], checksum)
    if city is not None:
        set_nested(json_data, ["city"], city)
    if country is not None:
        set_nested(json_data, ["country"], country)
    if created_after is not None:
        set_nested(json_data, ["createdAfter"], created_after)
    if created_before is not None:
        set_nested(json_data, ["createdBefore"], created_before)
    if cursor is not None:
        set_nested(json_data, ["cursor"], cursor)
    if description is not None:
        set_nested(json_data, ["description"], description)
    if encoded_video_path is not None:
        set_nested(json_data, ["encodedVideoPath"], encoded_video_path)
    if filter_album_ids_all is not None:
        set_nested(json_data, ["filter", "albumIds", "all"], filter_album_ids_all)
    if filter_album_ids_any is not None:
        set_nested(json_data, ["filter", "albumIds", "any"], filter_album_ids_any)
    if filter_album_ids_none is not None:
        set_nested(json_data, ["filter", "albumIds", "none"], filter_album_ids_none)
    if filter_checksum_eq is not None:
        set_nested(json_data, ["filter", "checksum", "eq"], filter_checksum_eq)
    if filter_checksum_in_ is not None:
        set_nested(json_data, ["filter", "checksum", "in"], filter_checksum_in_)
    if filter_checksum_ne is not None:
        set_nested(json_data, ["filter", "checksum", "ne"], filter_checksum_ne)
    if filter_checksum_not_in is not None:
        set_nested(json_data, ["filter", "checksum", "notIn"], filter_checksum_not_in)
    if filter_city_eq is not None:
        set_nested(json_data, ["filter", "city", "eq"], filter_city_eq)
    if filter_city_in_ is not None:
        set_nested(json_data, ["filter", "city", "in"], filter_city_in_)
    if filter_city_ne is not None:
        set_nested(json_data, ["filter", "city", "ne"], filter_city_ne)
    if filter_city_not_in is not None:
        set_nested(json_data, ["filter", "city", "notIn"], filter_city_not_in)
    if filter_country_eq is not None:
        set_nested(json_data, ["filter", "country", "eq"], filter_country_eq)
    if filter_country_in_ is not None:
        set_nested(json_data, ["filter", "country", "in"], filter_country_in_)
    if filter_country_ne is not None:
        set_nested(json_data, ["filter", "country", "ne"], filter_country_ne)
    if filter_country_not_in is not None:
        set_nested(json_data, ["filter", "country", "notIn"], filter_country_not_in)
    if filter_created_at_eq is not None:
        set_nested(json_data, ["filter", "createdAt", "eq"], filter_created_at_eq)
    if filter_created_at_gt is not None:
        set_nested(json_data, ["filter", "createdAt", "gt"], filter_created_at_gt)
    if filter_created_at_gte is not None:
        set_nested(json_data, ["filter", "createdAt", "gte"], filter_created_at_gte)
    if filter_created_at_lt is not None:
        set_nested(json_data, ["filter", "createdAt", "lt"], filter_created_at_lt)
    if filter_created_at_lte is not None:
        set_nested(json_data, ["filter", "createdAt", "lte"], filter_created_at_lte)
    if filter_created_at_ne is not None:
        set_nested(json_data, ["filter", "createdAt", "ne"], filter_created_at_ne)
    if filter_description_ends_with is not None:
        set_nested(
            json_data,
            ["filter", "description", "endsWith"],
            filter_description_ends_with,
        )
    if filter_description_eq is not None:
        set_nested(json_data, ["filter", "description", "eq"], filter_description_eq)
    if filter_description_in_ is not None:
        set_nested(json_data, ["filter", "description", "in"], filter_description_in_)
    if filter_description_like is not None:
        set_nested(
            json_data, ["filter", "description", "like"], filter_description_like
        )
    if filter_description_ne is not None:
        set_nested(json_data, ["filter", "description", "ne"], filter_description_ne)
    if filter_description_not_in is not None:
        set_nested(
            json_data, ["filter", "description", "notIn"], filter_description_not_in
        )
    if filter_description_not_like is not None:
        set_nested(
            json_data, ["filter", "description", "notLike"], filter_description_not_like
        )
    if filter_description_starts_with is not None:
        set_nested(
            json_data,
            ["filter", "description", "startsWith"],
            filter_description_starts_with,
        )
    if filter_encoded_video_path_eq is not None:
        set_nested(
            json_data,
            ["filter", "encodedVideoPath", "eq"],
            filter_encoded_video_path_eq,
        )
    if filter_encoded_video_path_in_ is not None:
        set_nested(
            json_data,
            ["filter", "encodedVideoPath", "in"],
            filter_encoded_video_path_in_,
        )
    if filter_encoded_video_path_ne is not None:
        set_nested(
            json_data,
            ["filter", "encodedVideoPath", "ne"],
            filter_encoded_video_path_ne,
        )
    if filter_encoded_video_path_not_in is not None:
        set_nested(
            json_data,
            ["filter", "encodedVideoPath", "notIn"],
            filter_encoded_video_path_not_in,
        )
    if filter_file_size_in_bytes_eq is not None:
        set_nested(
            json_data, ["filter", "fileSizeInBytes", "eq"], filter_file_size_in_bytes_eq
        )
    if filter_file_size_in_bytes_gt is not None:
        set_nested(
            json_data, ["filter", "fileSizeInBytes", "gt"], filter_file_size_in_bytes_gt
        )
    if filter_file_size_in_bytes_gte is not None:
        set_nested(
            json_data,
            ["filter", "fileSizeInBytes", "gte"],
            filter_file_size_in_bytes_gte,
        )
    if filter_file_size_in_bytes_in_ is not None:
        set_nested(
            json_data,
            ["filter", "fileSizeInBytes", "in"],
            filter_file_size_in_bytes_in_,
        )
    if filter_file_size_in_bytes_lt is not None:
        set_nested(
            json_data, ["filter", "fileSizeInBytes", "lt"], filter_file_size_in_bytes_lt
        )
    if filter_file_size_in_bytes_lte is not None:
        set_nested(
            json_data,
            ["filter", "fileSizeInBytes", "lte"],
            filter_file_size_in_bytes_lte,
        )
    if filter_file_size_in_bytes_ne is not None:
        set_nested(
            json_data, ["filter", "fileSizeInBytes", "ne"], filter_file_size_in_bytes_ne
        )
    if filter_file_size_in_bytes_not_in is not None:
        set_nested(
            json_data,
            ["filter", "fileSizeInBytes", "notIn"],
            filter_file_size_in_bytes_not_in,
        )
    if filter_has_albums_eq is not None:
        set_nested(
            json_data,
            ["filter", "hasAlbums", "eq"],
            filter_has_albums_eq.lower() == "true",
        )
    if filter_has_people_eq is not None:
        set_nested(
            json_data,
            ["filter", "hasPeople", "eq"],
            filter_has_people_eq.lower() == "true",
        )
    if filter_has_tags_eq is not None:
        set_nested(
            json_data, ["filter", "hasTags", "eq"], filter_has_tags_eq.lower() == "true"
        )
    if filter_id_eq is not None:
        set_nested(json_data, ["filter", "id", "eq"], filter_id_eq)
    if filter_id_ne is not None:
        set_nested(json_data, ["filter", "id", "ne"], filter_id_ne)
    if filter_is_encoded_eq is not None:
        set_nested(
            json_data,
            ["filter", "isEncoded", "eq"],
            filter_is_encoded_eq.lower() == "true",
        )
    if filter_is_favorite_eq is not None:
        set_nested(
            json_data,
            ["filter", "isFavorite", "eq"],
            filter_is_favorite_eq.lower() == "true",
        )
    if filter_is_motion_eq is not None:
        set_nested(
            json_data,
            ["filter", "isMotion", "eq"],
            filter_is_motion_eq.lower() == "true",
        )
    if filter_is_offline_eq is not None:
        set_nested(
            json_data,
            ["filter", "isOffline", "eq"],
            filter_is_offline_eq.lower() == "true",
        )
    if filter_lens_model_eq is not None:
        set_nested(json_data, ["filter", "lensModel", "eq"], filter_lens_model_eq)
    if filter_lens_model_in_ is not None:
        set_nested(json_data, ["filter", "lensModel", "in"], filter_lens_model_in_)
    if filter_lens_model_ne is not None:
        set_nested(json_data, ["filter", "lensModel", "ne"], filter_lens_model_ne)
    if filter_lens_model_not_in is not None:
        set_nested(
            json_data, ["filter", "lensModel", "notIn"], filter_lens_model_not_in
        )
    if filter_library_id_eq is not None:
        set_nested(json_data, ["filter", "libraryId", "eq"], filter_library_id_eq)
    if filter_library_id_ne is not None:
        set_nested(json_data, ["filter", "libraryId", "ne"], filter_library_id_ne)
    if filter_make_eq is not None:
        set_nested(json_data, ["filter", "make", "eq"], filter_make_eq)
    if filter_make_in_ is not None:
        set_nested(json_data, ["filter", "make", "in"], filter_make_in_)
    if filter_make_ne is not None:
        set_nested(json_data, ["filter", "make", "ne"], filter_make_ne)
    if filter_make_not_in is not None:
        set_nested(json_data, ["filter", "make", "notIn"], filter_make_not_in)
    if filter_model_eq is not None:
        set_nested(json_data, ["filter", "model", "eq"], filter_model_eq)
    if filter_model_in_ is not None:
        set_nested(json_data, ["filter", "model", "in"], filter_model_in_)
    if filter_model_ne is not None:
        set_nested(json_data, ["filter", "model", "ne"], filter_model_ne)
    if filter_model_not_in is not None:
        set_nested(json_data, ["filter", "model", "notIn"], filter_model_not_in)
    if filter_ocr_matches is not None:
        set_nested(json_data, ["filter", "ocr", "matches"], filter_ocr_matches)
    if filter_or_ is not None:
        value_filter_or_ = parse_json_options(filter_or_, "--filter-or", ctx=ctx)
        set_nested(json_data, ["filter", "or"], value_filter_or_)
    if filter_original_file_name_ends_with is not None:
        set_nested(
            json_data,
            ["filter", "originalFileName", "endsWith"],
            filter_original_file_name_ends_with,
        )
    if filter_original_file_name_eq is not None:
        set_nested(
            json_data,
            ["filter", "originalFileName", "eq"],
            filter_original_file_name_eq,
        )
    if filter_original_file_name_in_ is not None:
        set_nested(
            json_data,
            ["filter", "originalFileName", "in"],
            filter_original_file_name_in_,
        )
    if filter_original_file_name_like is not None:
        set_nested(
            json_data,
            ["filter", "originalFileName", "like"],
            filter_original_file_name_like,
        )
    if filter_original_file_name_ne is not None:
        set_nested(
            json_data,
            ["filter", "originalFileName", "ne"],
            filter_original_file_name_ne,
        )
    if filter_original_file_name_not_in is not None:
        set_nested(
            json_data,
            ["filter", "originalFileName", "notIn"],
            filter_original_file_name_not_in,
        )
    if filter_original_file_name_not_like is not None:
        set_nested(
            json_data,
            ["filter", "originalFileName", "notLike"],
            filter_original_file_name_not_like,
        )
    if filter_original_file_name_starts_with is not None:
        set_nested(
            json_data,
            ["filter", "originalFileName", "startsWith"],
            filter_original_file_name_starts_with,
        )
    if filter_original_path_ends_with is not None:
        set_nested(
            json_data,
            ["filter", "originalPath", "endsWith"],
            filter_original_path_ends_with,
        )
    if filter_original_path_eq is not None:
        set_nested(json_data, ["filter", "originalPath", "eq"], filter_original_path_eq)
    if filter_original_path_in_ is not None:
        set_nested(
            json_data, ["filter", "originalPath", "in"], filter_original_path_in_
        )
    if filter_original_path_like is not None:
        set_nested(
            json_data, ["filter", "originalPath", "like"], filter_original_path_like
        )
    if filter_original_path_ne is not None:
        set_nested(json_data, ["filter", "originalPath", "ne"], filter_original_path_ne)
    if filter_original_path_not_in is not None:
        set_nested(
            json_data, ["filter", "originalPath", "notIn"], filter_original_path_not_in
        )
    if filter_original_path_not_like is not None:
        set_nested(
            json_data,
            ["filter", "originalPath", "notLike"],
            filter_original_path_not_like,
        )
    if filter_original_path_starts_with is not None:
        set_nested(
            json_data,
            ["filter", "originalPath", "startsWith"],
            filter_original_path_starts_with,
        )
    if filter_person_ids_all is not None:
        set_nested(json_data, ["filter", "personIds", "all"], filter_person_ids_all)
    if filter_person_ids_any is not None:
        set_nested(json_data, ["filter", "personIds", "any"], filter_person_ids_any)
    if filter_person_ids_none is not None:
        set_nested(json_data, ["filter", "personIds", "none"], filter_person_ids_none)
    if filter_rating_eq is not None:
        set_nested(json_data, ["filter", "rating", "eq"], filter_rating_eq)
    if filter_rating_gt is not None:
        set_nested(json_data, ["filter", "rating", "gt"], filter_rating_gt)
    if filter_rating_gte is not None:
        set_nested(json_data, ["filter", "rating", "gte"], filter_rating_gte)
    if filter_rating_in_ is not None:
        set_nested(json_data, ["filter", "rating", "in"], filter_rating_in_)
    if filter_rating_lt is not None:
        set_nested(json_data, ["filter", "rating", "lt"], filter_rating_lt)
    if filter_rating_lte is not None:
        set_nested(json_data, ["filter", "rating", "lte"], filter_rating_lte)
    if filter_rating_ne is not None:
        set_nested(json_data, ["filter", "rating", "ne"], filter_rating_ne)
    if filter_rating_not_in is not None:
        set_nested(json_data, ["filter", "rating", "notIn"], filter_rating_not_in)
    if filter_state_eq is not None:
        set_nested(json_data, ["filter", "state", "eq"], filter_state_eq)
    if filter_state_in_ is not None:
        set_nested(json_data, ["filter", "state", "in"], filter_state_in_)
    if filter_state_ne is not None:
        set_nested(json_data, ["filter", "state", "ne"], filter_state_ne)
    if filter_state_not_in is not None:
        set_nested(json_data, ["filter", "state", "notIn"], filter_state_not_in)
    if filter_tag_ids_all is not None:
        set_nested(json_data, ["filter", "tagIds", "all"], filter_tag_ids_all)
    if filter_tag_ids_any is not None:
        set_nested(json_data, ["filter", "tagIds", "any"], filter_tag_ids_any)
    if filter_tag_ids_none is not None:
        set_nested(json_data, ["filter", "tagIds", "none"], filter_tag_ids_none)
    if filter_taken_at_eq is not None:
        set_nested(json_data, ["filter", "takenAt", "eq"], filter_taken_at_eq)
    if filter_taken_at_gt is not None:
        set_nested(json_data, ["filter", "takenAt", "gt"], filter_taken_at_gt)
    if filter_taken_at_gte is not None:
        set_nested(json_data, ["filter", "takenAt", "gte"], filter_taken_at_gte)
    if filter_taken_at_lt is not None:
        set_nested(json_data, ["filter", "takenAt", "lt"], filter_taken_at_lt)
    if filter_taken_at_lte is not None:
        set_nested(json_data, ["filter", "takenAt", "lte"], filter_taken_at_lte)
    if filter_taken_at_ne is not None:
        set_nested(json_data, ["filter", "takenAt", "ne"], filter_taken_at_ne)
    if filter_trashed_at_eq is not None:
        set_nested(json_data, ["filter", "trashedAt", "eq"], filter_trashed_at_eq)
    if filter_trashed_at_gt is not None:
        set_nested(json_data, ["filter", "trashedAt", "gt"], filter_trashed_at_gt)
    if filter_trashed_at_gte is not None:
        set_nested(json_data, ["filter", "trashedAt", "gte"], filter_trashed_at_gte)
    if filter_trashed_at_lt is not None:
        set_nested(json_data, ["filter", "trashedAt", "lt"], filter_trashed_at_lt)
    if filter_trashed_at_lte is not None:
        set_nested(json_data, ["filter", "trashedAt", "lte"], filter_trashed_at_lte)
    if filter_trashed_at_ne is not None:
        set_nested(json_data, ["filter", "trashedAt", "ne"], filter_trashed_at_ne)
    if filter_type_eq is not None:
        set_nested(json_data, ["filter", "type", "eq"], filter_type_eq)
    if filter_type_in_ is not None:
        set_nested(json_data, ["filter", "type", "in"], filter_type_in_)
    if filter_type_ne is not None:
        set_nested(json_data, ["filter", "type", "ne"], filter_type_ne)
    if filter_type_not_in is not None:
        set_nested(json_data, ["filter", "type", "notIn"], filter_type_not_in)
    if filter_updated_at_eq is not None:
        set_nested(json_data, ["filter", "updatedAt", "eq"], filter_updated_at_eq)
    if filter_updated_at_gt is not None:
        set_nested(json_data, ["filter", "updatedAt", "gt"], filter_updated_at_gt)
    if filter_updated_at_gte is not None:
        set_nested(json_data, ["filter", "updatedAt", "gte"], filter_updated_at_gte)
    if filter_updated_at_lt is not None:
        set_nested(json_data, ["filter", "updatedAt", "lt"], filter_updated_at_lt)
    if filter_updated_at_lte is not None:
        set_nested(json_data, ["filter", "updatedAt", "lte"], filter_updated_at_lte)
    if filter_updated_at_ne is not None:
        set_nested(json_data, ["filter", "updatedAt", "ne"], filter_updated_at_ne)
    if filter_visibility_eq is not None:
        set_nested(json_data, ["filter", "visibility", "eq"], filter_visibility_eq)
    if filter_visibility_in_ is not None:
        set_nested(json_data, ["filter", "visibility", "in"], filter_visibility_in_)
    if filter_visibility_ne is not None:
        set_nested(json_data, ["filter", "visibility", "ne"], filter_visibility_ne)
    if filter_visibility_not_in is not None:
        set_nested(
            json_data, ["filter", "visibility", "notIn"], filter_visibility_not_in
        )
    if id is not None:
        set_nested(json_data, ["id"], id)
    if is_encoded is not None:
        set_nested(json_data, ["isEncoded"], is_encoded.lower() == "true")
    if is_favorite is not None:
        set_nested(json_data, ["isFavorite"], is_favorite.lower() == "true")
    if is_motion is not None:
        set_nested(json_data, ["isMotion"], is_motion.lower() == "true")
    if is_not_in_album is not None:
        set_nested(json_data, ["isNotInAlbum"], is_not_in_album.lower() == "true")
    if is_offline is not None:
        set_nested(json_data, ["isOffline"], is_offline.lower() == "true")
    if lens_model is not None:
        set_nested(json_data, ["lensModel"], lens_model)
    if library_id is not None:
        set_nested(json_data, ["libraryId"], library_id)
    if make is not None:
        set_nested(json_data, ["make"], make)
    if model is not None:
        set_nested(json_data, ["model"], model)
    if ocr is not None:
        set_nested(json_data, ["ocr"], ocr)
    if order is not None:
        set_nested(json_data, ["order"], order)
    if order_by_direction is not None:
        set_nested(json_data, ["orderBy", "direction"], order_by_direction)
    if order_by_field is not None:
        set_nested(json_data, ["orderBy", "field"], order_by_field)
    if original_file_name is not None:
        set_nested(json_data, ["originalFileName"], original_file_name)
    if original_path is not None:
        set_nested(json_data, ["originalPath"], original_path)
    if page is not None:
        set_nested(json_data, ["page"], page)
    if person_ids is not None:
        set_nested(json_data, ["personIds"], person_ids)
    if preview_path is not None:
        set_nested(json_data, ["previewPath"], preview_path)
    if rating is not None:
        set_nested(json_data, ["rating"], rating)
    if size is not None:
        set_nested(json_data, ["size"], size)
    if state is not None:
        set_nested(json_data, ["state"], state)
    if tag_ids is not None:
        set_nested(json_data, ["tagIds"], tag_ids)
    if taken_after is not None:
        set_nested(json_data, ["takenAfter"], taken_after)
    if taken_before is not None:
        set_nested(json_data, ["takenBefore"], taken_before)
    if thumbnail_path is not None:
        set_nested(json_data, ["thumbnailPath"], thumbnail_path)
    if trashed_after is not None:
        set_nested(json_data, ["trashedAfter"], trashed_after)
    if trashed_before is not None:
        set_nested(json_data, ["trashedBefore"], trashed_before)
    if type is not None:
        set_nested(json_data, ["type"], type)
    if updated_after is not None:
        set_nested(json_data, ["updatedAfter"], updated_after)
    if updated_before is not None:
        set_nested(json_data, ["updatedBefore"], updated_before)
    if visibility is not None:
        set_nested(json_data, ["visibility"], visibility)
    if with_deleted is not None:
        set_nested(json_data, ["withDeleted"], with_deleted.lower() == "true")
    if with_exif is not None:
        set_nested(json_data, ["withExif"], with_exif.lower() == "true")
    if with_people is not None:
        set_nested(json_data, ["withPeople"], with_people.lower() == "true")
    if with_stacked is not None:
        set_nested(json_data, ["withStacked"], with_stacked.lower() == "true")
    metadata_search_dto = MetadataSearchDto.model_validate(json_data)
    kwargs["metadata_search_dto"] = metadata_search_dto
    client: AsyncClient = ctx.obj["client"]
    result = run_command(client.search.search_assets, ctx=ctx, **kwargs)
    print_response(result, ctx=ctx)


@app.command("search-large-assets", deprecated=True, rich_help_panel="API commands")
def search_large_assets(
    ctx: typer.Context,
    album_ids: list[UUID] | None = typer.Option(
        None, "--album-ids", help=r"""Filter by album IDs"""
    ),
    city: str | None = typer.Option(None, "--city", help=r"""Filter by city name"""),
    country: str | None = typer.Option(
        None, "--country", help=r"""Filter by country name"""
    ),
    created_after: datetime | None = typer.Option(
        None,
        "--created-after",
        help=r"""Filter by creation date (after)

Example: 2024-01-01T00:00:00.000Z""",
    ),
    created_before: datetime | None = typer.Option(
        None,
        "--created-before",
        help=r"""Filter by creation date (before)

Example: 2024-01-01T00:00:00.000Z""",
    ),
    is_encoded: Literal["true", "false"] | None = typer.Option(
        None, "--is-encoded", help=r"""Filter by encoded status"""
    ),
    is_favorite: Literal["true", "false"] | None = typer.Option(
        None, "--is-favorite", help=r"""Filter by favorite status"""
    ),
    is_motion: Literal["true", "false"] | None = typer.Option(
        None, "--is-motion", help=r"""Filter by motion photo status"""
    ),
    is_not_in_album: Literal["true", "false"] | None = typer.Option(
        None, "--is-not-in-album", help=r"""Filter assets not in any album"""
    ),
    is_offline: Literal["true", "false"] | None = typer.Option(
        None, "--is-offline", help=r"""Filter by offline status"""
    ),
    lens_model: str | None = typer.Option(
        None, "--lens-model", help=r"""Filter by lens model"""
    ),
    library_id: UUID | None = typer.Option(
        None, "--library-id", help=r"""Library ID to filter by"""
    ),
    make: str | None = typer.Option(None, "--make", help=r"""Filter by camera make"""),
    min_file_size: int | None = typer.Option(
        None,
        "--min-file-size",
        help=r"""Minimum file size in bytes""",
        min=0,
        max=9007199254740991,
    ),
    model: str | None = typer.Option(
        None, "--model", help=r"""Filter by camera model"""
    ),
    ocr: str | None = typer.Option(
        None, "--ocr", help=r"""Filter by OCR text content"""
    ),
    person_ids: list[UUID] | None = typer.Option(
        None, "--person-ids", help=r"""Filter by person IDs"""
    ),
    rating: int | None = typer.Option(
        None,
        "--rating",
        help=r"""Filter by rating [1-5], or null for unrated""",
        min=1,
        max=5,
    ),
    size: int | None = typer.Option(
        None, "--size", help=r"""Number of results to return""", min=1, max=1000
    ),
    state: str | None = typer.Option(
        None, "--state", help=r"""Filter by state/province name"""
    ),
    tag_ids: list[UUID] | None = typer.Option(
        None, "--tag-ids", help=r"""Filter by tag IDs"""
    ),
    taken_after: datetime | None = typer.Option(
        None,
        "--taken-after",
        help=r"""Filter by taken date (after)

Example: 2024-01-01T00:00:00.000Z""",
    ),
    taken_before: datetime | None = typer.Option(
        None,
        "--taken-before",
        help=r"""Filter by taken date (before)

Example: 2024-01-01T00:00:00.000Z""",
    ),
    trashed_after: datetime | None = typer.Option(
        None,
        "--trashed-after",
        help=r"""Filter by trash date (after)

Example: 2024-01-01T00:00:00.000Z""",
    ),
    trashed_before: datetime | None = typer.Option(
        None,
        "--trashed-before",
        help=r"""Filter by trash date (before)

Example: 2024-01-01T00:00:00.000Z""",
    ),
    type: AssetTypeEnum | None = typer.Option(None, "--type", help=r""""""),
    updated_after: datetime | None = typer.Option(
        None,
        "--updated-after",
        help=r"""Filter by update date (after)

Example: 2024-01-01T00:00:00.000Z""",
    ),
    updated_before: datetime | None = typer.Option(
        None,
        "--updated-before",
        help=r"""Filter by update date (before)

Example: 2024-01-01T00:00:00.000Z""",
    ),
    visibility: AssetVisibility | None = typer.Option(
        None, "--visibility", help=r""""""
    ),
    with_deleted: Literal["true", "false"] | None = typer.Option(
        None, "--with-deleted", help=r"""Include deleted assets"""
    ),
    with_exif: Literal["true", "false"] | None = typer.Option(
        None, "--with-exif", help=r"""Include EXIF data in response"""
    ),
) -> None:
    """Search large assets

    [link=https://api.immich.app/endpoints/search/searchLargeAssets]Immich API documentation[/link]
    """
    kwargs = {}
    if album_ids is not None:
        kwargs["album_ids"] = album_ids
    if city is not None:
        kwargs["city"] = city
    if country is not None:
        kwargs["country"] = country
    if created_after is not None:
        kwargs["created_after"] = created_after
    if created_before is not None:
        kwargs["created_before"] = created_before
    if is_encoded is not None:
        kwargs["is_encoded"] = is_encoded.lower() == "true"
    if is_favorite is not None:
        kwargs["is_favorite"] = is_favorite.lower() == "true"
    if is_motion is not None:
        kwargs["is_motion"] = is_motion.lower() == "true"
    if is_not_in_album is not None:
        kwargs["is_not_in_album"] = is_not_in_album.lower() == "true"
    if is_offline is not None:
        kwargs["is_offline"] = is_offline.lower() == "true"
    if lens_model is not None:
        kwargs["lens_model"] = lens_model
    if library_id is not None:
        kwargs["library_id"] = library_id
    if make is not None:
        kwargs["make"] = make
    if min_file_size is not None:
        kwargs["min_file_size"] = min_file_size
    if model is not None:
        kwargs["model"] = model
    if ocr is not None:
        kwargs["ocr"] = ocr
    if person_ids is not None:
        kwargs["person_ids"] = person_ids
    if rating is not None:
        kwargs["rating"] = rating
    if size is not None:
        kwargs["size"] = size
    if state is not None:
        kwargs["state"] = state
    if tag_ids is not None:
        kwargs["tag_ids"] = tag_ids
    if taken_after is not None:
        kwargs["taken_after"] = taken_after
    if taken_before is not None:
        kwargs["taken_before"] = taken_before
    if trashed_after is not None:
        kwargs["trashed_after"] = trashed_after
    if trashed_before is not None:
        kwargs["trashed_before"] = trashed_before
    if type is not None:
        kwargs["type"] = type
    if updated_after is not None:
        kwargs["updated_after"] = updated_after
    if updated_before is not None:
        kwargs["updated_before"] = updated_before
    if visibility is not None:
        kwargs["visibility"] = visibility
    if with_deleted is not None:
        kwargs["with_deleted"] = with_deleted.lower() == "true"
    if with_exif is not None:
        kwargs["with_exif"] = with_exif.lower() == "true"
    client: AsyncClient = ctx.obj["client"]
    result = run_command(client.search.search_large_assets, ctx=ctx, **kwargs)
    print_response(result, ctx=ctx)


@app.command("search-person", deprecated=False, rich_help_panel="API commands")
def search_person(
    ctx: typer.Context,
    name: str = typer.Option(..., "--name", help=r"""Person name to search for"""),
    with_hidden: Literal["true", "false"] | None = typer.Option(
        None, "--with-hidden", help=r"""Include hidden people"""
    ),
) -> None:
    """Search people

    [link=https://api.immich.app/endpoints/search/searchPerson]Immich API documentation[/link]
    """
    kwargs = {}
    kwargs["name"] = name
    if with_hidden is not None:
        kwargs["with_hidden"] = with_hidden.lower() == "true"
    client: AsyncClient = ctx.obj["client"]
    result = run_command(client.search.search_person, ctx=ctx, **kwargs)
    print_response(result, ctx=ctx)


@app.command("search-places", deprecated=False, rich_help_panel="API commands")
def search_places(
    ctx: typer.Context,
    name: str = typer.Option(..., "--name", help=r"""Place name to search for"""),
) -> None:
    """Search places

    [link=https://api.immich.app/endpoints/search/searchPlaces]Immich API documentation[/link]
    """
    kwargs = {}
    kwargs["name"] = name
    client: AsyncClient = ctx.obj["client"]
    result = run_command(client.search.search_places, ctx=ctx, **kwargs)
    print_response(result, ctx=ctx)


@app.command("search-random", deprecated=False, rich_help_panel="API commands")
def search_random(
    ctx: typer.Context,
    album_ids: list[UUID] | None = typer.Option(
        None, "--album-ids", help=r"""Filter by album IDs"""
    ),
    city: str | None = typer.Option(None, "--city", help=r"""Filter by city name"""),
    country: str | None = typer.Option(
        None, "--country", help=r"""Filter by country name"""
    ),
    created_after: datetime | None = typer.Option(
        None,
        "--created-after",
        help=r"""Filter by creation date (after)

Example: 2024-01-01T00:00:00.000Z""",
    ),
    created_before: datetime | None = typer.Option(
        None,
        "--created-before",
        help=r"""Filter by creation date (before)

Example: 2024-01-01T00:00:00.000Z""",
    ),
    filter_album_ids_all: list[UUID] | None = typer.Option(
        None, "--filter-album-ids-all", help=r""""""
    ),
    filter_album_ids_any: list[UUID] | None = typer.Option(
        None, "--filter-album-ids-any", help=r""""""
    ),
    filter_album_ids_none: list[UUID] | None = typer.Option(
        None, "--filter-album-ids-none", help=r""""""
    ),
    filter_checksum_eq: str | None = typer.Option(
        None, "--filter-checksum-eq", help=r""""""
    ),
    filter_checksum_in_: list[str] | None = typer.Option(
        None, "--filter-checksum-in", help=r""""""
    ),
    filter_checksum_ne: str | None = typer.Option(
        None, "--filter-checksum-ne", help=r""""""
    ),
    filter_checksum_not_in: list[str] | None = typer.Option(
        None, "--filter-checksum-not-in", help=r""""""
    ),
    filter_city_eq: str | None = typer.Option(None, "--filter-city-eq", help=r""""""),
    filter_city_in_: list[str] | None = typer.Option(
        None, "--filter-city-in", help=r""""""
    ),
    filter_city_ne: str | None = typer.Option(None, "--filter-city-ne", help=r""""""),
    filter_city_not_in: list[str] | None = typer.Option(
        None, "--filter-city-not-in", help=r""""""
    ),
    filter_country_eq: str | None = typer.Option(
        None, "--filter-country-eq", help=r""""""
    ),
    filter_country_in_: list[str] | None = typer.Option(
        None, "--filter-country-in", help=r""""""
    ),
    filter_country_ne: str | None = typer.Option(
        None, "--filter-country-ne", help=r""""""
    ),
    filter_country_not_in: list[str] | None = typer.Option(
        None, "--filter-country-not-in", help=r""""""
    ),
    filter_created_at_eq: datetime | None = typer.Option(
        None, "--filter-created-at-eq", help=r"""Example: 2024-01-01T00:00:00.000Z"""
    ),
    filter_created_at_gt: datetime | None = typer.Option(
        None, "--filter-created-at-gt", help=r"""Example: 2024-01-01T00:00:00.000Z"""
    ),
    filter_created_at_gte: datetime | None = typer.Option(
        None, "--filter-created-at-gte", help=r"""Example: 2024-01-01T00:00:00.000Z"""
    ),
    filter_created_at_lt: datetime | None = typer.Option(
        None, "--filter-created-at-lt", help=r"""Example: 2024-01-01T00:00:00.000Z"""
    ),
    filter_created_at_lte: datetime | None = typer.Option(
        None, "--filter-created-at-lte", help=r"""Example: 2024-01-01T00:00:00.000Z"""
    ),
    filter_created_at_ne: datetime | None = typer.Option(
        None, "--filter-created-at-ne", help=r"""Example: 2024-01-01T00:00:00.000Z"""
    ),
    filter_description_ends_with: str | None = typer.Option(
        None, "--filter-description-ends-with", help=r""""""
    ),
    filter_description_eq: str | None = typer.Option(
        None, "--filter-description-eq", help=r""""""
    ),
    filter_description_in_: list[str] | None = typer.Option(
        None, "--filter-description-in", help=r""""""
    ),
    filter_description_like: str | None = typer.Option(
        None, "--filter-description-like", help=r""""""
    ),
    filter_description_ne: str | None = typer.Option(
        None, "--filter-description-ne", help=r""""""
    ),
    filter_description_not_in: list[str] | None = typer.Option(
        None, "--filter-description-not-in", help=r""""""
    ),
    filter_description_not_like: str | None = typer.Option(
        None, "--filter-description-not-like", help=r""""""
    ),
    filter_description_starts_with: str | None = typer.Option(
        None, "--filter-description-starts-with", help=r""""""
    ),
    filter_encoded_video_path_eq: str | None = typer.Option(
        None, "--filter-encoded-video-path-eq", help=r""""""
    ),
    filter_encoded_video_path_in_: list[str] | None = typer.Option(
        None, "--filter-encoded-video-path-in", help=r""""""
    ),
    filter_encoded_video_path_ne: str | None = typer.Option(
        None, "--filter-encoded-video-path-ne", help=r""""""
    ),
    filter_encoded_video_path_not_in: list[str] | None = typer.Option(
        None, "--filter-encoded-video-path-not-in", help=r""""""
    ),
    filter_file_size_in_bytes_eq: float | None = typer.Option(
        None, "--filter-file-size-in-bytes-eq", help=r""""""
    ),
    filter_file_size_in_bytes_gt: float | None = typer.Option(
        None, "--filter-file-size-in-bytes-gt", help=r""""""
    ),
    filter_file_size_in_bytes_gte: float | None = typer.Option(
        None, "--filter-file-size-in-bytes-gte", help=r""""""
    ),
    filter_file_size_in_bytes_in_: list[float] | None = typer.Option(
        None, "--filter-file-size-in-bytes-in", help=r""""""
    ),
    filter_file_size_in_bytes_lt: float | None = typer.Option(
        None, "--filter-file-size-in-bytes-lt", help=r""""""
    ),
    filter_file_size_in_bytes_lte: float | None = typer.Option(
        None, "--filter-file-size-in-bytes-lte", help=r""""""
    ),
    filter_file_size_in_bytes_ne: float | None = typer.Option(
        None, "--filter-file-size-in-bytes-ne", help=r""""""
    ),
    filter_file_size_in_bytes_not_in: list[float] | None = typer.Option(
        None, "--filter-file-size-in-bytes-not-in", help=r""""""
    ),
    filter_has_albums_eq: Literal["true", "false"] | None = typer.Option(
        None, "--filter-has-albums-eq", help=r""""""
    ),
    filter_has_people_eq: Literal["true", "false"] | None = typer.Option(
        None, "--filter-has-people-eq", help=r""""""
    ),
    filter_has_tags_eq: Literal["true", "false"] | None = typer.Option(
        None, "--filter-has-tags-eq", help=r""""""
    ),
    filter_id_eq: UUID | None = typer.Option(None, "--filter-id-eq", help=r""""""),
    filter_id_ne: UUID | None = typer.Option(None, "--filter-id-ne", help=r""""""),
    filter_is_encoded_eq: Literal["true", "false"] | None = typer.Option(
        None, "--filter-is-encoded-eq", help=r""""""
    ),
    filter_is_favorite_eq: Literal["true", "false"] | None = typer.Option(
        None, "--filter-is-favorite-eq", help=r""""""
    ),
    filter_is_motion_eq: Literal["true", "false"] | None = typer.Option(
        None, "--filter-is-motion-eq", help=r""""""
    ),
    filter_is_offline_eq: Literal["true", "false"] | None = typer.Option(
        None, "--filter-is-offline-eq", help=r""""""
    ),
    filter_lens_model_eq: str | None = typer.Option(
        None, "--filter-lens-model-eq", help=r""""""
    ),
    filter_lens_model_in_: list[str] | None = typer.Option(
        None, "--filter-lens-model-in", help=r""""""
    ),
    filter_lens_model_ne: str | None = typer.Option(
        None, "--filter-lens-model-ne", help=r""""""
    ),
    filter_lens_model_not_in: list[str] | None = typer.Option(
        None, "--filter-lens-model-not-in", help=r""""""
    ),
    filter_library_id_eq: UUID | None = typer.Option(
        None, "--filter-library-id-eq", help=r""""""
    ),
    filter_library_id_ne: UUID | None = typer.Option(
        None, "--filter-library-id-ne", help=r""""""
    ),
    filter_make_eq: str | None = typer.Option(None, "--filter-make-eq", help=r""""""),
    filter_make_in_: list[str] | None = typer.Option(
        None, "--filter-make-in", help=r""""""
    ),
    filter_make_ne: str | None = typer.Option(None, "--filter-make-ne", help=r""""""),
    filter_make_not_in: list[str] | None = typer.Option(
        None, "--filter-make-not-in", help=r""""""
    ),
    filter_model_eq: str | None = typer.Option(None, "--filter-model-eq", help=r""""""),
    filter_model_in_: list[str] | None = typer.Option(
        None, "--filter-model-in", help=r""""""
    ),
    filter_model_ne: str | None = typer.Option(None, "--filter-model-ne", help=r""""""),
    filter_model_not_in: list[str] | None = typer.Option(
        None, "--filter-model-not-in", help=r""""""
    ),
    filter_ocr_matches: str | None = typer.Option(
        None, "--filter-ocr-matches", help=r""""""
    ),
    filter_or_: list[str] | None = typer.Option(
        None,
        "--filter-or",
        help=r"""As a JSON string with keys: albumIds (object), checksum (object), city (object), country (object), createdAt (object), description (object), encodedVideoPath (object), fileSizeInBytes (object), hasAlbums (object), hasPeople (object), hasTags (object), id (object), isEncoded (object), isFavorite (object), isMotion (object), isOffline (object), lensModel (object), libraryId (object), make (object), model (object), ocr (object), originalFileName (object), originalPath (object), personIds (object), rating (object), state (object), tagIds (object), takenAt (object), trashedAt (object), type (object), updatedAt (object), visibility (object)""",
    ),
    filter_original_file_name_ends_with: str | None = typer.Option(
        None, "--filter-original-file-name-ends-with", help=r""""""
    ),
    filter_original_file_name_eq: str | None = typer.Option(
        None, "--filter-original-file-name-eq", help=r""""""
    ),
    filter_original_file_name_in_: list[str] | None = typer.Option(
        None, "--filter-original-file-name-in", help=r""""""
    ),
    filter_original_file_name_like: str | None = typer.Option(
        None, "--filter-original-file-name-like", help=r""""""
    ),
    filter_original_file_name_ne: str | None = typer.Option(
        None, "--filter-original-file-name-ne", help=r""""""
    ),
    filter_original_file_name_not_in: list[str] | None = typer.Option(
        None, "--filter-original-file-name-not-in", help=r""""""
    ),
    filter_original_file_name_not_like: str | None = typer.Option(
        None, "--filter-original-file-name-not-like", help=r""""""
    ),
    filter_original_file_name_starts_with: str | None = typer.Option(
        None, "--filter-original-file-name-starts-with", help=r""""""
    ),
    filter_original_path_ends_with: str | None = typer.Option(
        None, "--filter-original-path-ends-with", help=r""""""
    ),
    filter_original_path_eq: str | None = typer.Option(
        None, "--filter-original-path-eq", help=r""""""
    ),
    filter_original_path_in_: list[str] | None = typer.Option(
        None, "--filter-original-path-in", help=r""""""
    ),
    filter_original_path_like: str | None = typer.Option(
        None, "--filter-original-path-like", help=r""""""
    ),
    filter_original_path_ne: str | None = typer.Option(
        None, "--filter-original-path-ne", help=r""""""
    ),
    filter_original_path_not_in: list[str] | None = typer.Option(
        None, "--filter-original-path-not-in", help=r""""""
    ),
    filter_original_path_not_like: str | None = typer.Option(
        None, "--filter-original-path-not-like", help=r""""""
    ),
    filter_original_path_starts_with: str | None = typer.Option(
        None, "--filter-original-path-starts-with", help=r""""""
    ),
    filter_person_ids_all: list[UUID] | None = typer.Option(
        None, "--filter-person-ids-all", help=r""""""
    ),
    filter_person_ids_any: list[UUID] | None = typer.Option(
        None, "--filter-person-ids-any", help=r""""""
    ),
    filter_person_ids_none: list[UUID] | None = typer.Option(
        None, "--filter-person-ids-none", help=r""""""
    ),
    filter_rating_eq: float | None = typer.Option(
        None, "--filter-rating-eq", help=r""""""
    ),
    filter_rating_gt: float | None = typer.Option(
        None, "--filter-rating-gt", help=r""""""
    ),
    filter_rating_gte: float | None = typer.Option(
        None, "--filter-rating-gte", help=r""""""
    ),
    filter_rating_in_: list[float] | None = typer.Option(
        None, "--filter-rating-in", help=r""""""
    ),
    filter_rating_lt: float | None = typer.Option(
        None, "--filter-rating-lt", help=r""""""
    ),
    filter_rating_lte: float | None = typer.Option(
        None, "--filter-rating-lte", help=r""""""
    ),
    filter_rating_ne: float | None = typer.Option(
        None, "--filter-rating-ne", help=r""""""
    ),
    filter_rating_not_in: list[float] | None = typer.Option(
        None, "--filter-rating-not-in", help=r""""""
    ),
    filter_state_eq: str | None = typer.Option(None, "--filter-state-eq", help=r""""""),
    filter_state_in_: list[str] | None = typer.Option(
        None, "--filter-state-in", help=r""""""
    ),
    filter_state_ne: str | None = typer.Option(None, "--filter-state-ne", help=r""""""),
    filter_state_not_in: list[str] | None = typer.Option(
        None, "--filter-state-not-in", help=r""""""
    ),
    filter_tag_ids_all: list[UUID] | None = typer.Option(
        None, "--filter-tag-ids-all", help=r""""""
    ),
    filter_tag_ids_any: list[UUID] | None = typer.Option(
        None, "--filter-tag-ids-any", help=r""""""
    ),
    filter_tag_ids_none: list[UUID] | None = typer.Option(
        None, "--filter-tag-ids-none", help=r""""""
    ),
    filter_taken_at_eq: datetime | None = typer.Option(
        None, "--filter-taken-at-eq", help=r"""Example: 2024-01-01T00:00:00.000Z"""
    ),
    filter_taken_at_gt: datetime | None = typer.Option(
        None, "--filter-taken-at-gt", help=r"""Example: 2024-01-01T00:00:00.000Z"""
    ),
    filter_taken_at_gte: datetime | None = typer.Option(
        None, "--filter-taken-at-gte", help=r"""Example: 2024-01-01T00:00:00.000Z"""
    ),
    filter_taken_at_lt: datetime | None = typer.Option(
        None, "--filter-taken-at-lt", help=r"""Example: 2024-01-01T00:00:00.000Z"""
    ),
    filter_taken_at_lte: datetime | None = typer.Option(
        None, "--filter-taken-at-lte", help=r"""Example: 2024-01-01T00:00:00.000Z"""
    ),
    filter_taken_at_ne: datetime | None = typer.Option(
        None, "--filter-taken-at-ne", help=r"""Example: 2024-01-01T00:00:00.000Z"""
    ),
    filter_trashed_at_eq: datetime | None = typer.Option(
        None, "--filter-trashed-at-eq", help=r"""Example: 2024-01-01T00:00:00.000Z"""
    ),
    filter_trashed_at_gt: datetime | None = typer.Option(
        None, "--filter-trashed-at-gt", help=r"""Example: 2024-01-01T00:00:00.000Z"""
    ),
    filter_trashed_at_gte: datetime | None = typer.Option(
        None, "--filter-trashed-at-gte", help=r"""Example: 2024-01-01T00:00:00.000Z"""
    ),
    filter_trashed_at_lt: datetime | None = typer.Option(
        None, "--filter-trashed-at-lt", help=r"""Example: 2024-01-01T00:00:00.000Z"""
    ),
    filter_trashed_at_lte: datetime | None = typer.Option(
        None, "--filter-trashed-at-lte", help=r"""Example: 2024-01-01T00:00:00.000Z"""
    ),
    filter_trashed_at_ne: datetime | None = typer.Option(
        None, "--filter-trashed-at-ne", help=r"""Example: 2024-01-01T00:00:00.000Z"""
    ),
    filter_type_eq: AssetTypeEnum | None = typer.Option(
        None, "--filter-type-eq", help=r"""Asset type"""
    ),
    filter_type_in_: list[AssetTypeEnum] | None = typer.Option(
        None, "--filter-type-in", help=r""""""
    ),
    filter_type_ne: AssetTypeEnum | None = typer.Option(
        None, "--filter-type-ne", help=r"""Asset type"""
    ),
    filter_type_not_in: list[AssetTypeEnum] | None = typer.Option(
        None, "--filter-type-not-in", help=r""""""
    ),
    filter_updated_at_eq: datetime | None = typer.Option(
        None, "--filter-updated-at-eq", help=r"""Example: 2024-01-01T00:00:00.000Z"""
    ),
    filter_updated_at_gt: datetime | None = typer.Option(
        None, "--filter-updated-at-gt", help=r"""Example: 2024-01-01T00:00:00.000Z"""
    ),
    filter_updated_at_gte: datetime | None = typer.Option(
        None, "--filter-updated-at-gte", help=r"""Example: 2024-01-01T00:00:00.000Z"""
    ),
    filter_updated_at_lt: datetime | None = typer.Option(
        None, "--filter-updated-at-lt", help=r"""Example: 2024-01-01T00:00:00.000Z"""
    ),
    filter_updated_at_lte: datetime | None = typer.Option(
        None, "--filter-updated-at-lte", help=r"""Example: 2024-01-01T00:00:00.000Z"""
    ),
    filter_updated_at_ne: datetime | None = typer.Option(
        None, "--filter-updated-at-ne", help=r"""Example: 2024-01-01T00:00:00.000Z"""
    ),
    filter_visibility_eq: AssetVisibility | None = typer.Option(
        None, "--filter-visibility-eq", help=r"""Asset visibility"""
    ),
    filter_visibility_in_: list[AssetVisibility] | None = typer.Option(
        None, "--filter-visibility-in", help=r""""""
    ),
    filter_visibility_ne: AssetVisibility | None = typer.Option(
        None, "--filter-visibility-ne", help=r"""Asset visibility"""
    ),
    filter_visibility_not_in: list[AssetVisibility] | None = typer.Option(
        None, "--filter-visibility-not-in", help=r""""""
    ),
    is_encoded: Literal["true", "false"] | None = typer.Option(
        None, "--is-encoded", help=r"""Filter by encoded status"""
    ),
    is_favorite: Literal["true", "false"] | None = typer.Option(
        None, "--is-favorite", help=r"""Filter by favorite status"""
    ),
    is_motion: Literal["true", "false"] | None = typer.Option(
        None, "--is-motion", help=r"""Filter by motion photo status"""
    ),
    is_not_in_album: Literal["true", "false"] | None = typer.Option(
        None, "--is-not-in-album", help=r"""Filter assets not in any album"""
    ),
    is_offline: Literal["true", "false"] | None = typer.Option(
        None, "--is-offline", help=r"""Filter by offline status"""
    ),
    lens_model: str | None = typer.Option(
        None, "--lens-model", help=r"""Filter by lens model"""
    ),
    library_id: UUID | None = typer.Option(
        None, "--library-id", help=r"""Library ID to filter by"""
    ),
    make: str | None = typer.Option(None, "--make", help=r"""Filter by camera make"""),
    model: str | None = typer.Option(
        None, "--model", help=r"""Filter by camera model"""
    ),
    ocr: str | None = typer.Option(
        None, "--ocr", help=r"""Filter by OCR text content"""
    ),
    person_ids: list[UUID] | None = typer.Option(
        None, "--person-ids", help=r"""Filter by person IDs"""
    ),
    rating: int | None = typer.Option(
        None,
        "--rating",
        help=r"""Filter by rating [1-5], or null for unrated""",
        min=1,
        max=5,
    ),
    size: int | None = typer.Option(
        None, "--size", help=r"""Number of results to return""", min=1, max=1000
    ),
    state: str | None = typer.Option(
        None, "--state", help=r"""Filter by state/province name"""
    ),
    tag_ids: list[UUID] | None = typer.Option(
        None, "--tag-ids", help=r"""Filter by tag IDs"""
    ),
    taken_after: datetime | None = typer.Option(
        None,
        "--taken-after",
        help=r"""Filter by taken date (after)

Example: 2024-01-01T00:00:00.000Z""",
    ),
    taken_before: datetime | None = typer.Option(
        None,
        "--taken-before",
        help=r"""Filter by taken date (before)

Example: 2024-01-01T00:00:00.000Z""",
    ),
    trashed_after: datetime | None = typer.Option(
        None,
        "--trashed-after",
        help=r"""Filter by trash date (after)

Example: 2024-01-01T00:00:00.000Z""",
    ),
    trashed_before: datetime | None = typer.Option(
        None,
        "--trashed-before",
        help=r"""Filter by trash date (before)

Example: 2024-01-01T00:00:00.000Z""",
    ),
    type: AssetTypeEnum | None = typer.Option(None, "--type", help=r"""Asset type"""),
    updated_after: datetime | None = typer.Option(
        None,
        "--updated-after",
        help=r"""Filter by update date (after)

Example: 2024-01-01T00:00:00.000Z""",
    ),
    updated_before: datetime | None = typer.Option(
        None,
        "--updated-before",
        help=r"""Filter by update date (before)

Example: 2024-01-01T00:00:00.000Z""",
    ),
    visibility: AssetVisibility | None = typer.Option(
        None, "--visibility", help=r"""Asset visibility"""
    ),
    with_deleted: Literal["true", "false"] | None = typer.Option(
        None, "--with-deleted", help=r"""Include deleted assets"""
    ),
    with_exif: Literal["true", "false"] | None = typer.Option(
        None, "--with-exif", help=r"""Include EXIF data in response"""
    ),
    with_people: Literal["true", "false"] | None = typer.Option(
        None, "--with-people", help=r"""Include people data in response"""
    ),
    with_stacked: Literal["true", "false"] | None = typer.Option(
        None, "--with-stacked", help=r"""Include stacked assets"""
    ),
) -> None:
    """Search random assets

    [link=https://api.immich.app/endpoints/search/searchRandom]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    if album_ids is not None:
        set_nested(json_data, ["albumIds"], album_ids)
    if city is not None:
        set_nested(json_data, ["city"], city)
    if country is not None:
        set_nested(json_data, ["country"], country)
    if created_after is not None:
        set_nested(json_data, ["createdAfter"], created_after)
    if created_before is not None:
        set_nested(json_data, ["createdBefore"], created_before)
    if filter_album_ids_all is not None:
        set_nested(json_data, ["filter", "albumIds", "all"], filter_album_ids_all)
    if filter_album_ids_any is not None:
        set_nested(json_data, ["filter", "albumIds", "any"], filter_album_ids_any)
    if filter_album_ids_none is not None:
        set_nested(json_data, ["filter", "albumIds", "none"], filter_album_ids_none)
    if filter_checksum_eq is not None:
        set_nested(json_data, ["filter", "checksum", "eq"], filter_checksum_eq)
    if filter_checksum_in_ is not None:
        set_nested(json_data, ["filter", "checksum", "in"], filter_checksum_in_)
    if filter_checksum_ne is not None:
        set_nested(json_data, ["filter", "checksum", "ne"], filter_checksum_ne)
    if filter_checksum_not_in is not None:
        set_nested(json_data, ["filter", "checksum", "notIn"], filter_checksum_not_in)
    if filter_city_eq is not None:
        set_nested(json_data, ["filter", "city", "eq"], filter_city_eq)
    if filter_city_in_ is not None:
        set_nested(json_data, ["filter", "city", "in"], filter_city_in_)
    if filter_city_ne is not None:
        set_nested(json_data, ["filter", "city", "ne"], filter_city_ne)
    if filter_city_not_in is not None:
        set_nested(json_data, ["filter", "city", "notIn"], filter_city_not_in)
    if filter_country_eq is not None:
        set_nested(json_data, ["filter", "country", "eq"], filter_country_eq)
    if filter_country_in_ is not None:
        set_nested(json_data, ["filter", "country", "in"], filter_country_in_)
    if filter_country_ne is not None:
        set_nested(json_data, ["filter", "country", "ne"], filter_country_ne)
    if filter_country_not_in is not None:
        set_nested(json_data, ["filter", "country", "notIn"], filter_country_not_in)
    if filter_created_at_eq is not None:
        set_nested(json_data, ["filter", "createdAt", "eq"], filter_created_at_eq)
    if filter_created_at_gt is not None:
        set_nested(json_data, ["filter", "createdAt", "gt"], filter_created_at_gt)
    if filter_created_at_gte is not None:
        set_nested(json_data, ["filter", "createdAt", "gte"], filter_created_at_gte)
    if filter_created_at_lt is not None:
        set_nested(json_data, ["filter", "createdAt", "lt"], filter_created_at_lt)
    if filter_created_at_lte is not None:
        set_nested(json_data, ["filter", "createdAt", "lte"], filter_created_at_lte)
    if filter_created_at_ne is not None:
        set_nested(json_data, ["filter", "createdAt", "ne"], filter_created_at_ne)
    if filter_description_ends_with is not None:
        set_nested(
            json_data,
            ["filter", "description", "endsWith"],
            filter_description_ends_with,
        )
    if filter_description_eq is not None:
        set_nested(json_data, ["filter", "description", "eq"], filter_description_eq)
    if filter_description_in_ is not None:
        set_nested(json_data, ["filter", "description", "in"], filter_description_in_)
    if filter_description_like is not None:
        set_nested(
            json_data, ["filter", "description", "like"], filter_description_like
        )
    if filter_description_ne is not None:
        set_nested(json_data, ["filter", "description", "ne"], filter_description_ne)
    if filter_description_not_in is not None:
        set_nested(
            json_data, ["filter", "description", "notIn"], filter_description_not_in
        )
    if filter_description_not_like is not None:
        set_nested(
            json_data, ["filter", "description", "notLike"], filter_description_not_like
        )
    if filter_description_starts_with is not None:
        set_nested(
            json_data,
            ["filter", "description", "startsWith"],
            filter_description_starts_with,
        )
    if filter_encoded_video_path_eq is not None:
        set_nested(
            json_data,
            ["filter", "encodedVideoPath", "eq"],
            filter_encoded_video_path_eq,
        )
    if filter_encoded_video_path_in_ is not None:
        set_nested(
            json_data,
            ["filter", "encodedVideoPath", "in"],
            filter_encoded_video_path_in_,
        )
    if filter_encoded_video_path_ne is not None:
        set_nested(
            json_data,
            ["filter", "encodedVideoPath", "ne"],
            filter_encoded_video_path_ne,
        )
    if filter_encoded_video_path_not_in is not None:
        set_nested(
            json_data,
            ["filter", "encodedVideoPath", "notIn"],
            filter_encoded_video_path_not_in,
        )
    if filter_file_size_in_bytes_eq is not None:
        set_nested(
            json_data, ["filter", "fileSizeInBytes", "eq"], filter_file_size_in_bytes_eq
        )
    if filter_file_size_in_bytes_gt is not None:
        set_nested(
            json_data, ["filter", "fileSizeInBytes", "gt"], filter_file_size_in_bytes_gt
        )
    if filter_file_size_in_bytes_gte is not None:
        set_nested(
            json_data,
            ["filter", "fileSizeInBytes", "gte"],
            filter_file_size_in_bytes_gte,
        )
    if filter_file_size_in_bytes_in_ is not None:
        set_nested(
            json_data,
            ["filter", "fileSizeInBytes", "in"],
            filter_file_size_in_bytes_in_,
        )
    if filter_file_size_in_bytes_lt is not None:
        set_nested(
            json_data, ["filter", "fileSizeInBytes", "lt"], filter_file_size_in_bytes_lt
        )
    if filter_file_size_in_bytes_lte is not None:
        set_nested(
            json_data,
            ["filter", "fileSizeInBytes", "lte"],
            filter_file_size_in_bytes_lte,
        )
    if filter_file_size_in_bytes_ne is not None:
        set_nested(
            json_data, ["filter", "fileSizeInBytes", "ne"], filter_file_size_in_bytes_ne
        )
    if filter_file_size_in_bytes_not_in is not None:
        set_nested(
            json_data,
            ["filter", "fileSizeInBytes", "notIn"],
            filter_file_size_in_bytes_not_in,
        )
    if filter_has_albums_eq is not None:
        set_nested(
            json_data,
            ["filter", "hasAlbums", "eq"],
            filter_has_albums_eq.lower() == "true",
        )
    if filter_has_people_eq is not None:
        set_nested(
            json_data,
            ["filter", "hasPeople", "eq"],
            filter_has_people_eq.lower() == "true",
        )
    if filter_has_tags_eq is not None:
        set_nested(
            json_data, ["filter", "hasTags", "eq"], filter_has_tags_eq.lower() == "true"
        )
    if filter_id_eq is not None:
        set_nested(json_data, ["filter", "id", "eq"], filter_id_eq)
    if filter_id_ne is not None:
        set_nested(json_data, ["filter", "id", "ne"], filter_id_ne)
    if filter_is_encoded_eq is not None:
        set_nested(
            json_data,
            ["filter", "isEncoded", "eq"],
            filter_is_encoded_eq.lower() == "true",
        )
    if filter_is_favorite_eq is not None:
        set_nested(
            json_data,
            ["filter", "isFavorite", "eq"],
            filter_is_favorite_eq.lower() == "true",
        )
    if filter_is_motion_eq is not None:
        set_nested(
            json_data,
            ["filter", "isMotion", "eq"],
            filter_is_motion_eq.lower() == "true",
        )
    if filter_is_offline_eq is not None:
        set_nested(
            json_data,
            ["filter", "isOffline", "eq"],
            filter_is_offline_eq.lower() == "true",
        )
    if filter_lens_model_eq is not None:
        set_nested(json_data, ["filter", "lensModel", "eq"], filter_lens_model_eq)
    if filter_lens_model_in_ is not None:
        set_nested(json_data, ["filter", "lensModel", "in"], filter_lens_model_in_)
    if filter_lens_model_ne is not None:
        set_nested(json_data, ["filter", "lensModel", "ne"], filter_lens_model_ne)
    if filter_lens_model_not_in is not None:
        set_nested(
            json_data, ["filter", "lensModel", "notIn"], filter_lens_model_not_in
        )
    if filter_library_id_eq is not None:
        set_nested(json_data, ["filter", "libraryId", "eq"], filter_library_id_eq)
    if filter_library_id_ne is not None:
        set_nested(json_data, ["filter", "libraryId", "ne"], filter_library_id_ne)
    if filter_make_eq is not None:
        set_nested(json_data, ["filter", "make", "eq"], filter_make_eq)
    if filter_make_in_ is not None:
        set_nested(json_data, ["filter", "make", "in"], filter_make_in_)
    if filter_make_ne is not None:
        set_nested(json_data, ["filter", "make", "ne"], filter_make_ne)
    if filter_make_not_in is not None:
        set_nested(json_data, ["filter", "make", "notIn"], filter_make_not_in)
    if filter_model_eq is not None:
        set_nested(json_data, ["filter", "model", "eq"], filter_model_eq)
    if filter_model_in_ is not None:
        set_nested(json_data, ["filter", "model", "in"], filter_model_in_)
    if filter_model_ne is not None:
        set_nested(json_data, ["filter", "model", "ne"], filter_model_ne)
    if filter_model_not_in is not None:
        set_nested(json_data, ["filter", "model", "notIn"], filter_model_not_in)
    if filter_ocr_matches is not None:
        set_nested(json_data, ["filter", "ocr", "matches"], filter_ocr_matches)
    if filter_or_ is not None:
        value_filter_or_ = parse_json_options(filter_or_, "--filter-or", ctx=ctx)
        set_nested(json_data, ["filter", "or"], value_filter_or_)
    if filter_original_file_name_ends_with is not None:
        set_nested(
            json_data,
            ["filter", "originalFileName", "endsWith"],
            filter_original_file_name_ends_with,
        )
    if filter_original_file_name_eq is not None:
        set_nested(
            json_data,
            ["filter", "originalFileName", "eq"],
            filter_original_file_name_eq,
        )
    if filter_original_file_name_in_ is not None:
        set_nested(
            json_data,
            ["filter", "originalFileName", "in"],
            filter_original_file_name_in_,
        )
    if filter_original_file_name_like is not None:
        set_nested(
            json_data,
            ["filter", "originalFileName", "like"],
            filter_original_file_name_like,
        )
    if filter_original_file_name_ne is not None:
        set_nested(
            json_data,
            ["filter", "originalFileName", "ne"],
            filter_original_file_name_ne,
        )
    if filter_original_file_name_not_in is not None:
        set_nested(
            json_data,
            ["filter", "originalFileName", "notIn"],
            filter_original_file_name_not_in,
        )
    if filter_original_file_name_not_like is not None:
        set_nested(
            json_data,
            ["filter", "originalFileName", "notLike"],
            filter_original_file_name_not_like,
        )
    if filter_original_file_name_starts_with is not None:
        set_nested(
            json_data,
            ["filter", "originalFileName", "startsWith"],
            filter_original_file_name_starts_with,
        )
    if filter_original_path_ends_with is not None:
        set_nested(
            json_data,
            ["filter", "originalPath", "endsWith"],
            filter_original_path_ends_with,
        )
    if filter_original_path_eq is not None:
        set_nested(json_data, ["filter", "originalPath", "eq"], filter_original_path_eq)
    if filter_original_path_in_ is not None:
        set_nested(
            json_data, ["filter", "originalPath", "in"], filter_original_path_in_
        )
    if filter_original_path_like is not None:
        set_nested(
            json_data, ["filter", "originalPath", "like"], filter_original_path_like
        )
    if filter_original_path_ne is not None:
        set_nested(json_data, ["filter", "originalPath", "ne"], filter_original_path_ne)
    if filter_original_path_not_in is not None:
        set_nested(
            json_data, ["filter", "originalPath", "notIn"], filter_original_path_not_in
        )
    if filter_original_path_not_like is not None:
        set_nested(
            json_data,
            ["filter", "originalPath", "notLike"],
            filter_original_path_not_like,
        )
    if filter_original_path_starts_with is not None:
        set_nested(
            json_data,
            ["filter", "originalPath", "startsWith"],
            filter_original_path_starts_with,
        )
    if filter_person_ids_all is not None:
        set_nested(json_data, ["filter", "personIds", "all"], filter_person_ids_all)
    if filter_person_ids_any is not None:
        set_nested(json_data, ["filter", "personIds", "any"], filter_person_ids_any)
    if filter_person_ids_none is not None:
        set_nested(json_data, ["filter", "personIds", "none"], filter_person_ids_none)
    if filter_rating_eq is not None:
        set_nested(json_data, ["filter", "rating", "eq"], filter_rating_eq)
    if filter_rating_gt is not None:
        set_nested(json_data, ["filter", "rating", "gt"], filter_rating_gt)
    if filter_rating_gte is not None:
        set_nested(json_data, ["filter", "rating", "gte"], filter_rating_gte)
    if filter_rating_in_ is not None:
        set_nested(json_data, ["filter", "rating", "in"], filter_rating_in_)
    if filter_rating_lt is not None:
        set_nested(json_data, ["filter", "rating", "lt"], filter_rating_lt)
    if filter_rating_lte is not None:
        set_nested(json_data, ["filter", "rating", "lte"], filter_rating_lte)
    if filter_rating_ne is not None:
        set_nested(json_data, ["filter", "rating", "ne"], filter_rating_ne)
    if filter_rating_not_in is not None:
        set_nested(json_data, ["filter", "rating", "notIn"], filter_rating_not_in)
    if filter_state_eq is not None:
        set_nested(json_data, ["filter", "state", "eq"], filter_state_eq)
    if filter_state_in_ is not None:
        set_nested(json_data, ["filter", "state", "in"], filter_state_in_)
    if filter_state_ne is not None:
        set_nested(json_data, ["filter", "state", "ne"], filter_state_ne)
    if filter_state_not_in is not None:
        set_nested(json_data, ["filter", "state", "notIn"], filter_state_not_in)
    if filter_tag_ids_all is not None:
        set_nested(json_data, ["filter", "tagIds", "all"], filter_tag_ids_all)
    if filter_tag_ids_any is not None:
        set_nested(json_data, ["filter", "tagIds", "any"], filter_tag_ids_any)
    if filter_tag_ids_none is not None:
        set_nested(json_data, ["filter", "tagIds", "none"], filter_tag_ids_none)
    if filter_taken_at_eq is not None:
        set_nested(json_data, ["filter", "takenAt", "eq"], filter_taken_at_eq)
    if filter_taken_at_gt is not None:
        set_nested(json_data, ["filter", "takenAt", "gt"], filter_taken_at_gt)
    if filter_taken_at_gte is not None:
        set_nested(json_data, ["filter", "takenAt", "gte"], filter_taken_at_gte)
    if filter_taken_at_lt is not None:
        set_nested(json_data, ["filter", "takenAt", "lt"], filter_taken_at_lt)
    if filter_taken_at_lte is not None:
        set_nested(json_data, ["filter", "takenAt", "lte"], filter_taken_at_lte)
    if filter_taken_at_ne is not None:
        set_nested(json_data, ["filter", "takenAt", "ne"], filter_taken_at_ne)
    if filter_trashed_at_eq is not None:
        set_nested(json_data, ["filter", "trashedAt", "eq"], filter_trashed_at_eq)
    if filter_trashed_at_gt is not None:
        set_nested(json_data, ["filter", "trashedAt", "gt"], filter_trashed_at_gt)
    if filter_trashed_at_gte is not None:
        set_nested(json_data, ["filter", "trashedAt", "gte"], filter_trashed_at_gte)
    if filter_trashed_at_lt is not None:
        set_nested(json_data, ["filter", "trashedAt", "lt"], filter_trashed_at_lt)
    if filter_trashed_at_lte is not None:
        set_nested(json_data, ["filter", "trashedAt", "lte"], filter_trashed_at_lte)
    if filter_trashed_at_ne is not None:
        set_nested(json_data, ["filter", "trashedAt", "ne"], filter_trashed_at_ne)
    if filter_type_eq is not None:
        set_nested(json_data, ["filter", "type", "eq"], filter_type_eq)
    if filter_type_in_ is not None:
        set_nested(json_data, ["filter", "type", "in"], filter_type_in_)
    if filter_type_ne is not None:
        set_nested(json_data, ["filter", "type", "ne"], filter_type_ne)
    if filter_type_not_in is not None:
        set_nested(json_data, ["filter", "type", "notIn"], filter_type_not_in)
    if filter_updated_at_eq is not None:
        set_nested(json_data, ["filter", "updatedAt", "eq"], filter_updated_at_eq)
    if filter_updated_at_gt is not None:
        set_nested(json_data, ["filter", "updatedAt", "gt"], filter_updated_at_gt)
    if filter_updated_at_gte is not None:
        set_nested(json_data, ["filter", "updatedAt", "gte"], filter_updated_at_gte)
    if filter_updated_at_lt is not None:
        set_nested(json_data, ["filter", "updatedAt", "lt"], filter_updated_at_lt)
    if filter_updated_at_lte is not None:
        set_nested(json_data, ["filter", "updatedAt", "lte"], filter_updated_at_lte)
    if filter_updated_at_ne is not None:
        set_nested(json_data, ["filter", "updatedAt", "ne"], filter_updated_at_ne)
    if filter_visibility_eq is not None:
        set_nested(json_data, ["filter", "visibility", "eq"], filter_visibility_eq)
    if filter_visibility_in_ is not None:
        set_nested(json_data, ["filter", "visibility", "in"], filter_visibility_in_)
    if filter_visibility_ne is not None:
        set_nested(json_data, ["filter", "visibility", "ne"], filter_visibility_ne)
    if filter_visibility_not_in is not None:
        set_nested(
            json_data, ["filter", "visibility", "notIn"], filter_visibility_not_in
        )
    if is_encoded is not None:
        set_nested(json_data, ["isEncoded"], is_encoded.lower() == "true")
    if is_favorite is not None:
        set_nested(json_data, ["isFavorite"], is_favorite.lower() == "true")
    if is_motion is not None:
        set_nested(json_data, ["isMotion"], is_motion.lower() == "true")
    if is_not_in_album is not None:
        set_nested(json_data, ["isNotInAlbum"], is_not_in_album.lower() == "true")
    if is_offline is not None:
        set_nested(json_data, ["isOffline"], is_offline.lower() == "true")
    if lens_model is not None:
        set_nested(json_data, ["lensModel"], lens_model)
    if library_id is not None:
        set_nested(json_data, ["libraryId"], library_id)
    if make is not None:
        set_nested(json_data, ["make"], make)
    if model is not None:
        set_nested(json_data, ["model"], model)
    if ocr is not None:
        set_nested(json_data, ["ocr"], ocr)
    if person_ids is not None:
        set_nested(json_data, ["personIds"], person_ids)
    if rating is not None:
        set_nested(json_data, ["rating"], rating)
    if size is not None:
        set_nested(json_data, ["size"], size)
    if state is not None:
        set_nested(json_data, ["state"], state)
    if tag_ids is not None:
        set_nested(json_data, ["tagIds"], tag_ids)
    if taken_after is not None:
        set_nested(json_data, ["takenAfter"], taken_after)
    if taken_before is not None:
        set_nested(json_data, ["takenBefore"], taken_before)
    if trashed_after is not None:
        set_nested(json_data, ["trashedAfter"], trashed_after)
    if trashed_before is not None:
        set_nested(json_data, ["trashedBefore"], trashed_before)
    if type is not None:
        set_nested(json_data, ["type"], type)
    if updated_after is not None:
        set_nested(json_data, ["updatedAfter"], updated_after)
    if updated_before is not None:
        set_nested(json_data, ["updatedBefore"], updated_before)
    if visibility is not None:
        set_nested(json_data, ["visibility"], visibility)
    if with_deleted is not None:
        set_nested(json_data, ["withDeleted"], with_deleted.lower() == "true")
    if with_exif is not None:
        set_nested(json_data, ["withExif"], with_exif.lower() == "true")
    if with_people is not None:
        set_nested(json_data, ["withPeople"], with_people.lower() == "true")
    if with_stacked is not None:
        set_nested(json_data, ["withStacked"], with_stacked.lower() == "true")
    random_search_dto = RandomSearchDto.model_validate(json_data)
    kwargs["random_search_dto"] = random_search_dto
    client: AsyncClient = ctx.obj["client"]
    result = run_command(client.search.search_random, ctx=ctx, **kwargs)
    print_response(result, ctx=ctx)


@app.command("search-smart", deprecated=False, rich_help_panel="API commands")
def search_smart(
    ctx: typer.Context,
    album_ids: list[UUID] | None = typer.Option(
        None, "--album-ids", help=r"""Filter by album IDs"""
    ),
    city: str | None = typer.Option(None, "--city", help=r"""Filter by city name"""),
    country: str | None = typer.Option(
        None, "--country", help=r"""Filter by country name"""
    ),
    created_after: datetime | None = typer.Option(
        None,
        "--created-after",
        help=r"""Filter by creation date (after)

Example: 2024-01-01T00:00:00.000Z""",
    ),
    created_before: datetime | None = typer.Option(
        None,
        "--created-before",
        help=r"""Filter by creation date (before)

Example: 2024-01-01T00:00:00.000Z""",
    ),
    filter_album_ids_all: list[UUID] | None = typer.Option(
        None, "--filter-album-ids-all", help=r""""""
    ),
    filter_album_ids_any: list[UUID] | None = typer.Option(
        None, "--filter-album-ids-any", help=r""""""
    ),
    filter_album_ids_none: list[UUID] | None = typer.Option(
        None, "--filter-album-ids-none", help=r""""""
    ),
    filter_checksum_eq: str | None = typer.Option(
        None, "--filter-checksum-eq", help=r""""""
    ),
    filter_checksum_in_: list[str] | None = typer.Option(
        None, "--filter-checksum-in", help=r""""""
    ),
    filter_checksum_ne: str | None = typer.Option(
        None, "--filter-checksum-ne", help=r""""""
    ),
    filter_checksum_not_in: list[str] | None = typer.Option(
        None, "--filter-checksum-not-in", help=r""""""
    ),
    filter_city_eq: str | None = typer.Option(None, "--filter-city-eq", help=r""""""),
    filter_city_in_: list[str] | None = typer.Option(
        None, "--filter-city-in", help=r""""""
    ),
    filter_city_ne: str | None = typer.Option(None, "--filter-city-ne", help=r""""""),
    filter_city_not_in: list[str] | None = typer.Option(
        None, "--filter-city-not-in", help=r""""""
    ),
    filter_country_eq: str | None = typer.Option(
        None, "--filter-country-eq", help=r""""""
    ),
    filter_country_in_: list[str] | None = typer.Option(
        None, "--filter-country-in", help=r""""""
    ),
    filter_country_ne: str | None = typer.Option(
        None, "--filter-country-ne", help=r""""""
    ),
    filter_country_not_in: list[str] | None = typer.Option(
        None, "--filter-country-not-in", help=r""""""
    ),
    filter_created_at_eq: datetime | None = typer.Option(
        None, "--filter-created-at-eq", help=r"""Example: 2024-01-01T00:00:00.000Z"""
    ),
    filter_created_at_gt: datetime | None = typer.Option(
        None, "--filter-created-at-gt", help=r"""Example: 2024-01-01T00:00:00.000Z"""
    ),
    filter_created_at_gte: datetime | None = typer.Option(
        None, "--filter-created-at-gte", help=r"""Example: 2024-01-01T00:00:00.000Z"""
    ),
    filter_created_at_lt: datetime | None = typer.Option(
        None, "--filter-created-at-lt", help=r"""Example: 2024-01-01T00:00:00.000Z"""
    ),
    filter_created_at_lte: datetime | None = typer.Option(
        None, "--filter-created-at-lte", help=r"""Example: 2024-01-01T00:00:00.000Z"""
    ),
    filter_created_at_ne: datetime | None = typer.Option(
        None, "--filter-created-at-ne", help=r"""Example: 2024-01-01T00:00:00.000Z"""
    ),
    filter_description_ends_with: str | None = typer.Option(
        None, "--filter-description-ends-with", help=r""""""
    ),
    filter_description_eq: str | None = typer.Option(
        None, "--filter-description-eq", help=r""""""
    ),
    filter_description_in_: list[str] | None = typer.Option(
        None, "--filter-description-in", help=r""""""
    ),
    filter_description_like: str | None = typer.Option(
        None, "--filter-description-like", help=r""""""
    ),
    filter_description_ne: str | None = typer.Option(
        None, "--filter-description-ne", help=r""""""
    ),
    filter_description_not_in: list[str] | None = typer.Option(
        None, "--filter-description-not-in", help=r""""""
    ),
    filter_description_not_like: str | None = typer.Option(
        None, "--filter-description-not-like", help=r""""""
    ),
    filter_description_starts_with: str | None = typer.Option(
        None, "--filter-description-starts-with", help=r""""""
    ),
    filter_encoded_video_path_eq: str | None = typer.Option(
        None, "--filter-encoded-video-path-eq", help=r""""""
    ),
    filter_encoded_video_path_in_: list[str] | None = typer.Option(
        None, "--filter-encoded-video-path-in", help=r""""""
    ),
    filter_encoded_video_path_ne: str | None = typer.Option(
        None, "--filter-encoded-video-path-ne", help=r""""""
    ),
    filter_encoded_video_path_not_in: list[str] | None = typer.Option(
        None, "--filter-encoded-video-path-not-in", help=r""""""
    ),
    filter_file_size_in_bytes_eq: float | None = typer.Option(
        None, "--filter-file-size-in-bytes-eq", help=r""""""
    ),
    filter_file_size_in_bytes_gt: float | None = typer.Option(
        None, "--filter-file-size-in-bytes-gt", help=r""""""
    ),
    filter_file_size_in_bytes_gte: float | None = typer.Option(
        None, "--filter-file-size-in-bytes-gte", help=r""""""
    ),
    filter_file_size_in_bytes_in_: list[float] | None = typer.Option(
        None, "--filter-file-size-in-bytes-in", help=r""""""
    ),
    filter_file_size_in_bytes_lt: float | None = typer.Option(
        None, "--filter-file-size-in-bytes-lt", help=r""""""
    ),
    filter_file_size_in_bytes_lte: float | None = typer.Option(
        None, "--filter-file-size-in-bytes-lte", help=r""""""
    ),
    filter_file_size_in_bytes_ne: float | None = typer.Option(
        None, "--filter-file-size-in-bytes-ne", help=r""""""
    ),
    filter_file_size_in_bytes_not_in: list[float] | None = typer.Option(
        None, "--filter-file-size-in-bytes-not-in", help=r""""""
    ),
    filter_has_albums_eq: Literal["true", "false"] | None = typer.Option(
        None, "--filter-has-albums-eq", help=r""""""
    ),
    filter_has_people_eq: Literal["true", "false"] | None = typer.Option(
        None, "--filter-has-people-eq", help=r""""""
    ),
    filter_has_tags_eq: Literal["true", "false"] | None = typer.Option(
        None, "--filter-has-tags-eq", help=r""""""
    ),
    filter_id_eq: UUID | None = typer.Option(None, "--filter-id-eq", help=r""""""),
    filter_id_ne: UUID | None = typer.Option(None, "--filter-id-ne", help=r""""""),
    filter_is_encoded_eq: Literal["true", "false"] | None = typer.Option(
        None, "--filter-is-encoded-eq", help=r""""""
    ),
    filter_is_favorite_eq: Literal["true", "false"] | None = typer.Option(
        None, "--filter-is-favorite-eq", help=r""""""
    ),
    filter_is_motion_eq: Literal["true", "false"] | None = typer.Option(
        None, "--filter-is-motion-eq", help=r""""""
    ),
    filter_is_offline_eq: Literal["true", "false"] | None = typer.Option(
        None, "--filter-is-offline-eq", help=r""""""
    ),
    filter_lens_model_eq: str | None = typer.Option(
        None, "--filter-lens-model-eq", help=r""""""
    ),
    filter_lens_model_in_: list[str] | None = typer.Option(
        None, "--filter-lens-model-in", help=r""""""
    ),
    filter_lens_model_ne: str | None = typer.Option(
        None, "--filter-lens-model-ne", help=r""""""
    ),
    filter_lens_model_not_in: list[str] | None = typer.Option(
        None, "--filter-lens-model-not-in", help=r""""""
    ),
    filter_library_id_eq: UUID | None = typer.Option(
        None, "--filter-library-id-eq", help=r""""""
    ),
    filter_library_id_ne: UUID | None = typer.Option(
        None, "--filter-library-id-ne", help=r""""""
    ),
    filter_make_eq: str | None = typer.Option(None, "--filter-make-eq", help=r""""""),
    filter_make_in_: list[str] | None = typer.Option(
        None, "--filter-make-in", help=r""""""
    ),
    filter_make_ne: str | None = typer.Option(None, "--filter-make-ne", help=r""""""),
    filter_make_not_in: list[str] | None = typer.Option(
        None, "--filter-make-not-in", help=r""""""
    ),
    filter_model_eq: str | None = typer.Option(None, "--filter-model-eq", help=r""""""),
    filter_model_in_: list[str] | None = typer.Option(
        None, "--filter-model-in", help=r""""""
    ),
    filter_model_ne: str | None = typer.Option(None, "--filter-model-ne", help=r""""""),
    filter_model_not_in: list[str] | None = typer.Option(
        None, "--filter-model-not-in", help=r""""""
    ),
    filter_ocr_matches: str | None = typer.Option(
        None, "--filter-ocr-matches", help=r""""""
    ),
    filter_or_: list[str] | None = typer.Option(
        None,
        "--filter-or",
        help=r"""As a JSON string with keys: albumIds (object), checksum (object), city (object), country (object), createdAt (object), description (object), encodedVideoPath (object), fileSizeInBytes (object), hasAlbums (object), hasPeople (object), hasTags (object), id (object), isEncoded (object), isFavorite (object), isMotion (object), isOffline (object), lensModel (object), libraryId (object), make (object), model (object), ocr (object), originalFileName (object), originalPath (object), personIds (object), rating (object), state (object), tagIds (object), takenAt (object), trashedAt (object), type (object), updatedAt (object), visibility (object)""",
    ),
    filter_original_file_name_ends_with: str | None = typer.Option(
        None, "--filter-original-file-name-ends-with", help=r""""""
    ),
    filter_original_file_name_eq: str | None = typer.Option(
        None, "--filter-original-file-name-eq", help=r""""""
    ),
    filter_original_file_name_in_: list[str] | None = typer.Option(
        None, "--filter-original-file-name-in", help=r""""""
    ),
    filter_original_file_name_like: str | None = typer.Option(
        None, "--filter-original-file-name-like", help=r""""""
    ),
    filter_original_file_name_ne: str | None = typer.Option(
        None, "--filter-original-file-name-ne", help=r""""""
    ),
    filter_original_file_name_not_in: list[str] | None = typer.Option(
        None, "--filter-original-file-name-not-in", help=r""""""
    ),
    filter_original_file_name_not_like: str | None = typer.Option(
        None, "--filter-original-file-name-not-like", help=r""""""
    ),
    filter_original_file_name_starts_with: str | None = typer.Option(
        None, "--filter-original-file-name-starts-with", help=r""""""
    ),
    filter_original_path_ends_with: str | None = typer.Option(
        None, "--filter-original-path-ends-with", help=r""""""
    ),
    filter_original_path_eq: str | None = typer.Option(
        None, "--filter-original-path-eq", help=r""""""
    ),
    filter_original_path_in_: list[str] | None = typer.Option(
        None, "--filter-original-path-in", help=r""""""
    ),
    filter_original_path_like: str | None = typer.Option(
        None, "--filter-original-path-like", help=r""""""
    ),
    filter_original_path_ne: str | None = typer.Option(
        None, "--filter-original-path-ne", help=r""""""
    ),
    filter_original_path_not_in: list[str] | None = typer.Option(
        None, "--filter-original-path-not-in", help=r""""""
    ),
    filter_original_path_not_like: str | None = typer.Option(
        None, "--filter-original-path-not-like", help=r""""""
    ),
    filter_original_path_starts_with: str | None = typer.Option(
        None, "--filter-original-path-starts-with", help=r""""""
    ),
    filter_person_ids_all: list[UUID] | None = typer.Option(
        None, "--filter-person-ids-all", help=r""""""
    ),
    filter_person_ids_any: list[UUID] | None = typer.Option(
        None, "--filter-person-ids-any", help=r""""""
    ),
    filter_person_ids_none: list[UUID] | None = typer.Option(
        None, "--filter-person-ids-none", help=r""""""
    ),
    filter_rating_eq: float | None = typer.Option(
        None, "--filter-rating-eq", help=r""""""
    ),
    filter_rating_gt: float | None = typer.Option(
        None, "--filter-rating-gt", help=r""""""
    ),
    filter_rating_gte: float | None = typer.Option(
        None, "--filter-rating-gte", help=r""""""
    ),
    filter_rating_in_: list[float] | None = typer.Option(
        None, "--filter-rating-in", help=r""""""
    ),
    filter_rating_lt: float | None = typer.Option(
        None, "--filter-rating-lt", help=r""""""
    ),
    filter_rating_lte: float | None = typer.Option(
        None, "--filter-rating-lte", help=r""""""
    ),
    filter_rating_ne: float | None = typer.Option(
        None, "--filter-rating-ne", help=r""""""
    ),
    filter_rating_not_in: list[float] | None = typer.Option(
        None, "--filter-rating-not-in", help=r""""""
    ),
    filter_state_eq: str | None = typer.Option(None, "--filter-state-eq", help=r""""""),
    filter_state_in_: list[str] | None = typer.Option(
        None, "--filter-state-in", help=r""""""
    ),
    filter_state_ne: str | None = typer.Option(None, "--filter-state-ne", help=r""""""),
    filter_state_not_in: list[str] | None = typer.Option(
        None, "--filter-state-not-in", help=r""""""
    ),
    filter_tag_ids_all: list[UUID] | None = typer.Option(
        None, "--filter-tag-ids-all", help=r""""""
    ),
    filter_tag_ids_any: list[UUID] | None = typer.Option(
        None, "--filter-tag-ids-any", help=r""""""
    ),
    filter_tag_ids_none: list[UUID] | None = typer.Option(
        None, "--filter-tag-ids-none", help=r""""""
    ),
    filter_taken_at_eq: datetime | None = typer.Option(
        None, "--filter-taken-at-eq", help=r"""Example: 2024-01-01T00:00:00.000Z"""
    ),
    filter_taken_at_gt: datetime | None = typer.Option(
        None, "--filter-taken-at-gt", help=r"""Example: 2024-01-01T00:00:00.000Z"""
    ),
    filter_taken_at_gte: datetime | None = typer.Option(
        None, "--filter-taken-at-gte", help=r"""Example: 2024-01-01T00:00:00.000Z"""
    ),
    filter_taken_at_lt: datetime | None = typer.Option(
        None, "--filter-taken-at-lt", help=r"""Example: 2024-01-01T00:00:00.000Z"""
    ),
    filter_taken_at_lte: datetime | None = typer.Option(
        None, "--filter-taken-at-lte", help=r"""Example: 2024-01-01T00:00:00.000Z"""
    ),
    filter_taken_at_ne: datetime | None = typer.Option(
        None, "--filter-taken-at-ne", help=r"""Example: 2024-01-01T00:00:00.000Z"""
    ),
    filter_trashed_at_eq: datetime | None = typer.Option(
        None, "--filter-trashed-at-eq", help=r"""Example: 2024-01-01T00:00:00.000Z"""
    ),
    filter_trashed_at_gt: datetime | None = typer.Option(
        None, "--filter-trashed-at-gt", help=r"""Example: 2024-01-01T00:00:00.000Z"""
    ),
    filter_trashed_at_gte: datetime | None = typer.Option(
        None, "--filter-trashed-at-gte", help=r"""Example: 2024-01-01T00:00:00.000Z"""
    ),
    filter_trashed_at_lt: datetime | None = typer.Option(
        None, "--filter-trashed-at-lt", help=r"""Example: 2024-01-01T00:00:00.000Z"""
    ),
    filter_trashed_at_lte: datetime | None = typer.Option(
        None, "--filter-trashed-at-lte", help=r"""Example: 2024-01-01T00:00:00.000Z"""
    ),
    filter_trashed_at_ne: datetime | None = typer.Option(
        None, "--filter-trashed-at-ne", help=r"""Example: 2024-01-01T00:00:00.000Z"""
    ),
    filter_type_eq: AssetTypeEnum | None = typer.Option(
        None, "--filter-type-eq", help=r"""Asset type"""
    ),
    filter_type_in_: list[AssetTypeEnum] | None = typer.Option(
        None, "--filter-type-in", help=r""""""
    ),
    filter_type_ne: AssetTypeEnum | None = typer.Option(
        None, "--filter-type-ne", help=r"""Asset type"""
    ),
    filter_type_not_in: list[AssetTypeEnum] | None = typer.Option(
        None, "--filter-type-not-in", help=r""""""
    ),
    filter_updated_at_eq: datetime | None = typer.Option(
        None, "--filter-updated-at-eq", help=r"""Example: 2024-01-01T00:00:00.000Z"""
    ),
    filter_updated_at_gt: datetime | None = typer.Option(
        None, "--filter-updated-at-gt", help=r"""Example: 2024-01-01T00:00:00.000Z"""
    ),
    filter_updated_at_gte: datetime | None = typer.Option(
        None, "--filter-updated-at-gte", help=r"""Example: 2024-01-01T00:00:00.000Z"""
    ),
    filter_updated_at_lt: datetime | None = typer.Option(
        None, "--filter-updated-at-lt", help=r"""Example: 2024-01-01T00:00:00.000Z"""
    ),
    filter_updated_at_lte: datetime | None = typer.Option(
        None, "--filter-updated-at-lte", help=r"""Example: 2024-01-01T00:00:00.000Z"""
    ),
    filter_updated_at_ne: datetime | None = typer.Option(
        None, "--filter-updated-at-ne", help=r"""Example: 2024-01-01T00:00:00.000Z"""
    ),
    filter_visibility_eq: AssetVisibility | None = typer.Option(
        None, "--filter-visibility-eq", help=r"""Asset visibility"""
    ),
    filter_visibility_in_: list[AssetVisibility] | None = typer.Option(
        None, "--filter-visibility-in", help=r""""""
    ),
    filter_visibility_ne: AssetVisibility | None = typer.Option(
        None, "--filter-visibility-ne", help=r"""Asset visibility"""
    ),
    filter_visibility_not_in: list[AssetVisibility] | None = typer.Option(
        None, "--filter-visibility-not-in", help=r""""""
    ),
    is_encoded: Literal["true", "false"] | None = typer.Option(
        None, "--is-encoded", help=r"""Filter by encoded status"""
    ),
    is_favorite: Literal["true", "false"] | None = typer.Option(
        None, "--is-favorite", help=r"""Filter by favorite status"""
    ),
    is_motion: Literal["true", "false"] | None = typer.Option(
        None, "--is-motion", help=r"""Filter by motion photo status"""
    ),
    is_not_in_album: Literal["true", "false"] | None = typer.Option(
        None, "--is-not-in-album", help=r"""Filter assets not in any album"""
    ),
    is_offline: Literal["true", "false"] | None = typer.Option(
        None, "--is-offline", help=r"""Filter by offline status"""
    ),
    language: str | None = typer.Option(
        None, "--language", help=r"""Search language code"""
    ),
    lens_model: str | None = typer.Option(
        None, "--lens-model", help=r"""Filter by lens model"""
    ),
    library_id: UUID | None = typer.Option(
        None, "--library-id", help=r"""Library ID to filter by"""
    ),
    make: str | None = typer.Option(None, "--make", help=r"""Filter by camera make"""),
    model: str | None = typer.Option(
        None, "--model", help=r"""Filter by camera model"""
    ),
    ocr: str | None = typer.Option(
        None, "--ocr", help=r"""Filter by OCR text content"""
    ),
    page: int | None = typer.Option(
        None, "--page", help=r"""Page number""", min=1, max=9007199254740991
    ),
    person_ids: list[UUID] | None = typer.Option(
        None, "--person-ids", help=r"""Filter by person IDs"""
    ),
    query: str | None = typer.Option(
        None, "--query", help=r"""Natural language search query"""
    ),
    query_asset_id: UUID | None = typer.Option(
        None, "--query-asset-id", help=r"""Asset ID to use as search reference"""
    ),
    rating: int | None = typer.Option(
        None,
        "--rating",
        help=r"""Filter by rating [1-5], or null for unrated""",
        min=1,
        max=5,
    ),
    size: int | None = typer.Option(
        None, "--size", help=r"""Number of results to return""", min=1, max=1000
    ),
    state: str | None = typer.Option(
        None, "--state", help=r"""Filter by state/province name"""
    ),
    tag_ids: list[UUID] | None = typer.Option(
        None, "--tag-ids", help=r"""Filter by tag IDs"""
    ),
    taken_after: datetime | None = typer.Option(
        None,
        "--taken-after",
        help=r"""Filter by taken date (after)

Example: 2024-01-01T00:00:00.000Z""",
    ),
    taken_before: datetime | None = typer.Option(
        None,
        "--taken-before",
        help=r"""Filter by taken date (before)

Example: 2024-01-01T00:00:00.000Z""",
    ),
    trashed_after: datetime | None = typer.Option(
        None,
        "--trashed-after",
        help=r"""Filter by trash date (after)

Example: 2024-01-01T00:00:00.000Z""",
    ),
    trashed_before: datetime | None = typer.Option(
        None,
        "--trashed-before",
        help=r"""Filter by trash date (before)

Example: 2024-01-01T00:00:00.000Z""",
    ),
    type: AssetTypeEnum | None = typer.Option(None, "--type", help=r"""Asset type"""),
    updated_after: datetime | None = typer.Option(
        None,
        "--updated-after",
        help=r"""Filter by update date (after)

Example: 2024-01-01T00:00:00.000Z""",
    ),
    updated_before: datetime | None = typer.Option(
        None,
        "--updated-before",
        help=r"""Filter by update date (before)

Example: 2024-01-01T00:00:00.000Z""",
    ),
    visibility: AssetVisibility | None = typer.Option(
        None, "--visibility", help=r"""Asset visibility"""
    ),
    with_deleted: Literal["true", "false"] | None = typer.Option(
        None, "--with-deleted", help=r"""Include deleted assets"""
    ),
    with_exif: Literal["true", "false"] | None = typer.Option(
        None, "--with-exif", help=r"""Include EXIF data in response"""
    ),
) -> None:
    """Smart asset search

    [link=https://api.immich.app/endpoints/search/searchSmart]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    if album_ids is not None:
        set_nested(json_data, ["albumIds"], album_ids)
    if city is not None:
        set_nested(json_data, ["city"], city)
    if country is not None:
        set_nested(json_data, ["country"], country)
    if created_after is not None:
        set_nested(json_data, ["createdAfter"], created_after)
    if created_before is not None:
        set_nested(json_data, ["createdBefore"], created_before)
    if filter_album_ids_all is not None:
        set_nested(json_data, ["filter", "albumIds", "all"], filter_album_ids_all)
    if filter_album_ids_any is not None:
        set_nested(json_data, ["filter", "albumIds", "any"], filter_album_ids_any)
    if filter_album_ids_none is not None:
        set_nested(json_data, ["filter", "albumIds", "none"], filter_album_ids_none)
    if filter_checksum_eq is not None:
        set_nested(json_data, ["filter", "checksum", "eq"], filter_checksum_eq)
    if filter_checksum_in_ is not None:
        set_nested(json_data, ["filter", "checksum", "in"], filter_checksum_in_)
    if filter_checksum_ne is not None:
        set_nested(json_data, ["filter", "checksum", "ne"], filter_checksum_ne)
    if filter_checksum_not_in is not None:
        set_nested(json_data, ["filter", "checksum", "notIn"], filter_checksum_not_in)
    if filter_city_eq is not None:
        set_nested(json_data, ["filter", "city", "eq"], filter_city_eq)
    if filter_city_in_ is not None:
        set_nested(json_data, ["filter", "city", "in"], filter_city_in_)
    if filter_city_ne is not None:
        set_nested(json_data, ["filter", "city", "ne"], filter_city_ne)
    if filter_city_not_in is not None:
        set_nested(json_data, ["filter", "city", "notIn"], filter_city_not_in)
    if filter_country_eq is not None:
        set_nested(json_data, ["filter", "country", "eq"], filter_country_eq)
    if filter_country_in_ is not None:
        set_nested(json_data, ["filter", "country", "in"], filter_country_in_)
    if filter_country_ne is not None:
        set_nested(json_data, ["filter", "country", "ne"], filter_country_ne)
    if filter_country_not_in is not None:
        set_nested(json_data, ["filter", "country", "notIn"], filter_country_not_in)
    if filter_created_at_eq is not None:
        set_nested(json_data, ["filter", "createdAt", "eq"], filter_created_at_eq)
    if filter_created_at_gt is not None:
        set_nested(json_data, ["filter", "createdAt", "gt"], filter_created_at_gt)
    if filter_created_at_gte is not None:
        set_nested(json_data, ["filter", "createdAt", "gte"], filter_created_at_gte)
    if filter_created_at_lt is not None:
        set_nested(json_data, ["filter", "createdAt", "lt"], filter_created_at_lt)
    if filter_created_at_lte is not None:
        set_nested(json_data, ["filter", "createdAt", "lte"], filter_created_at_lte)
    if filter_created_at_ne is not None:
        set_nested(json_data, ["filter", "createdAt", "ne"], filter_created_at_ne)
    if filter_description_ends_with is not None:
        set_nested(
            json_data,
            ["filter", "description", "endsWith"],
            filter_description_ends_with,
        )
    if filter_description_eq is not None:
        set_nested(json_data, ["filter", "description", "eq"], filter_description_eq)
    if filter_description_in_ is not None:
        set_nested(json_data, ["filter", "description", "in"], filter_description_in_)
    if filter_description_like is not None:
        set_nested(
            json_data, ["filter", "description", "like"], filter_description_like
        )
    if filter_description_ne is not None:
        set_nested(json_data, ["filter", "description", "ne"], filter_description_ne)
    if filter_description_not_in is not None:
        set_nested(
            json_data, ["filter", "description", "notIn"], filter_description_not_in
        )
    if filter_description_not_like is not None:
        set_nested(
            json_data, ["filter", "description", "notLike"], filter_description_not_like
        )
    if filter_description_starts_with is not None:
        set_nested(
            json_data,
            ["filter", "description", "startsWith"],
            filter_description_starts_with,
        )
    if filter_encoded_video_path_eq is not None:
        set_nested(
            json_data,
            ["filter", "encodedVideoPath", "eq"],
            filter_encoded_video_path_eq,
        )
    if filter_encoded_video_path_in_ is not None:
        set_nested(
            json_data,
            ["filter", "encodedVideoPath", "in"],
            filter_encoded_video_path_in_,
        )
    if filter_encoded_video_path_ne is not None:
        set_nested(
            json_data,
            ["filter", "encodedVideoPath", "ne"],
            filter_encoded_video_path_ne,
        )
    if filter_encoded_video_path_not_in is not None:
        set_nested(
            json_data,
            ["filter", "encodedVideoPath", "notIn"],
            filter_encoded_video_path_not_in,
        )
    if filter_file_size_in_bytes_eq is not None:
        set_nested(
            json_data, ["filter", "fileSizeInBytes", "eq"], filter_file_size_in_bytes_eq
        )
    if filter_file_size_in_bytes_gt is not None:
        set_nested(
            json_data, ["filter", "fileSizeInBytes", "gt"], filter_file_size_in_bytes_gt
        )
    if filter_file_size_in_bytes_gte is not None:
        set_nested(
            json_data,
            ["filter", "fileSizeInBytes", "gte"],
            filter_file_size_in_bytes_gte,
        )
    if filter_file_size_in_bytes_in_ is not None:
        set_nested(
            json_data,
            ["filter", "fileSizeInBytes", "in"],
            filter_file_size_in_bytes_in_,
        )
    if filter_file_size_in_bytes_lt is not None:
        set_nested(
            json_data, ["filter", "fileSizeInBytes", "lt"], filter_file_size_in_bytes_lt
        )
    if filter_file_size_in_bytes_lte is not None:
        set_nested(
            json_data,
            ["filter", "fileSizeInBytes", "lte"],
            filter_file_size_in_bytes_lte,
        )
    if filter_file_size_in_bytes_ne is not None:
        set_nested(
            json_data, ["filter", "fileSizeInBytes", "ne"], filter_file_size_in_bytes_ne
        )
    if filter_file_size_in_bytes_not_in is not None:
        set_nested(
            json_data,
            ["filter", "fileSizeInBytes", "notIn"],
            filter_file_size_in_bytes_not_in,
        )
    if filter_has_albums_eq is not None:
        set_nested(
            json_data,
            ["filter", "hasAlbums", "eq"],
            filter_has_albums_eq.lower() == "true",
        )
    if filter_has_people_eq is not None:
        set_nested(
            json_data,
            ["filter", "hasPeople", "eq"],
            filter_has_people_eq.lower() == "true",
        )
    if filter_has_tags_eq is not None:
        set_nested(
            json_data, ["filter", "hasTags", "eq"], filter_has_tags_eq.lower() == "true"
        )
    if filter_id_eq is not None:
        set_nested(json_data, ["filter", "id", "eq"], filter_id_eq)
    if filter_id_ne is not None:
        set_nested(json_data, ["filter", "id", "ne"], filter_id_ne)
    if filter_is_encoded_eq is not None:
        set_nested(
            json_data,
            ["filter", "isEncoded", "eq"],
            filter_is_encoded_eq.lower() == "true",
        )
    if filter_is_favorite_eq is not None:
        set_nested(
            json_data,
            ["filter", "isFavorite", "eq"],
            filter_is_favorite_eq.lower() == "true",
        )
    if filter_is_motion_eq is not None:
        set_nested(
            json_data,
            ["filter", "isMotion", "eq"],
            filter_is_motion_eq.lower() == "true",
        )
    if filter_is_offline_eq is not None:
        set_nested(
            json_data,
            ["filter", "isOffline", "eq"],
            filter_is_offline_eq.lower() == "true",
        )
    if filter_lens_model_eq is not None:
        set_nested(json_data, ["filter", "lensModel", "eq"], filter_lens_model_eq)
    if filter_lens_model_in_ is not None:
        set_nested(json_data, ["filter", "lensModel", "in"], filter_lens_model_in_)
    if filter_lens_model_ne is not None:
        set_nested(json_data, ["filter", "lensModel", "ne"], filter_lens_model_ne)
    if filter_lens_model_not_in is not None:
        set_nested(
            json_data, ["filter", "lensModel", "notIn"], filter_lens_model_not_in
        )
    if filter_library_id_eq is not None:
        set_nested(json_data, ["filter", "libraryId", "eq"], filter_library_id_eq)
    if filter_library_id_ne is not None:
        set_nested(json_data, ["filter", "libraryId", "ne"], filter_library_id_ne)
    if filter_make_eq is not None:
        set_nested(json_data, ["filter", "make", "eq"], filter_make_eq)
    if filter_make_in_ is not None:
        set_nested(json_data, ["filter", "make", "in"], filter_make_in_)
    if filter_make_ne is not None:
        set_nested(json_data, ["filter", "make", "ne"], filter_make_ne)
    if filter_make_not_in is not None:
        set_nested(json_data, ["filter", "make", "notIn"], filter_make_not_in)
    if filter_model_eq is not None:
        set_nested(json_data, ["filter", "model", "eq"], filter_model_eq)
    if filter_model_in_ is not None:
        set_nested(json_data, ["filter", "model", "in"], filter_model_in_)
    if filter_model_ne is not None:
        set_nested(json_data, ["filter", "model", "ne"], filter_model_ne)
    if filter_model_not_in is not None:
        set_nested(json_data, ["filter", "model", "notIn"], filter_model_not_in)
    if filter_ocr_matches is not None:
        set_nested(json_data, ["filter", "ocr", "matches"], filter_ocr_matches)
    if filter_or_ is not None:
        value_filter_or_ = parse_json_options(filter_or_, "--filter-or", ctx=ctx)
        set_nested(json_data, ["filter", "or"], value_filter_or_)
    if filter_original_file_name_ends_with is not None:
        set_nested(
            json_data,
            ["filter", "originalFileName", "endsWith"],
            filter_original_file_name_ends_with,
        )
    if filter_original_file_name_eq is not None:
        set_nested(
            json_data,
            ["filter", "originalFileName", "eq"],
            filter_original_file_name_eq,
        )
    if filter_original_file_name_in_ is not None:
        set_nested(
            json_data,
            ["filter", "originalFileName", "in"],
            filter_original_file_name_in_,
        )
    if filter_original_file_name_like is not None:
        set_nested(
            json_data,
            ["filter", "originalFileName", "like"],
            filter_original_file_name_like,
        )
    if filter_original_file_name_ne is not None:
        set_nested(
            json_data,
            ["filter", "originalFileName", "ne"],
            filter_original_file_name_ne,
        )
    if filter_original_file_name_not_in is not None:
        set_nested(
            json_data,
            ["filter", "originalFileName", "notIn"],
            filter_original_file_name_not_in,
        )
    if filter_original_file_name_not_like is not None:
        set_nested(
            json_data,
            ["filter", "originalFileName", "notLike"],
            filter_original_file_name_not_like,
        )
    if filter_original_file_name_starts_with is not None:
        set_nested(
            json_data,
            ["filter", "originalFileName", "startsWith"],
            filter_original_file_name_starts_with,
        )
    if filter_original_path_ends_with is not None:
        set_nested(
            json_data,
            ["filter", "originalPath", "endsWith"],
            filter_original_path_ends_with,
        )
    if filter_original_path_eq is not None:
        set_nested(json_data, ["filter", "originalPath", "eq"], filter_original_path_eq)
    if filter_original_path_in_ is not None:
        set_nested(
            json_data, ["filter", "originalPath", "in"], filter_original_path_in_
        )
    if filter_original_path_like is not None:
        set_nested(
            json_data, ["filter", "originalPath", "like"], filter_original_path_like
        )
    if filter_original_path_ne is not None:
        set_nested(json_data, ["filter", "originalPath", "ne"], filter_original_path_ne)
    if filter_original_path_not_in is not None:
        set_nested(
            json_data, ["filter", "originalPath", "notIn"], filter_original_path_not_in
        )
    if filter_original_path_not_like is not None:
        set_nested(
            json_data,
            ["filter", "originalPath", "notLike"],
            filter_original_path_not_like,
        )
    if filter_original_path_starts_with is not None:
        set_nested(
            json_data,
            ["filter", "originalPath", "startsWith"],
            filter_original_path_starts_with,
        )
    if filter_person_ids_all is not None:
        set_nested(json_data, ["filter", "personIds", "all"], filter_person_ids_all)
    if filter_person_ids_any is not None:
        set_nested(json_data, ["filter", "personIds", "any"], filter_person_ids_any)
    if filter_person_ids_none is not None:
        set_nested(json_data, ["filter", "personIds", "none"], filter_person_ids_none)
    if filter_rating_eq is not None:
        set_nested(json_data, ["filter", "rating", "eq"], filter_rating_eq)
    if filter_rating_gt is not None:
        set_nested(json_data, ["filter", "rating", "gt"], filter_rating_gt)
    if filter_rating_gte is not None:
        set_nested(json_data, ["filter", "rating", "gte"], filter_rating_gte)
    if filter_rating_in_ is not None:
        set_nested(json_data, ["filter", "rating", "in"], filter_rating_in_)
    if filter_rating_lt is not None:
        set_nested(json_data, ["filter", "rating", "lt"], filter_rating_lt)
    if filter_rating_lte is not None:
        set_nested(json_data, ["filter", "rating", "lte"], filter_rating_lte)
    if filter_rating_ne is not None:
        set_nested(json_data, ["filter", "rating", "ne"], filter_rating_ne)
    if filter_rating_not_in is not None:
        set_nested(json_data, ["filter", "rating", "notIn"], filter_rating_not_in)
    if filter_state_eq is not None:
        set_nested(json_data, ["filter", "state", "eq"], filter_state_eq)
    if filter_state_in_ is not None:
        set_nested(json_data, ["filter", "state", "in"], filter_state_in_)
    if filter_state_ne is not None:
        set_nested(json_data, ["filter", "state", "ne"], filter_state_ne)
    if filter_state_not_in is not None:
        set_nested(json_data, ["filter", "state", "notIn"], filter_state_not_in)
    if filter_tag_ids_all is not None:
        set_nested(json_data, ["filter", "tagIds", "all"], filter_tag_ids_all)
    if filter_tag_ids_any is not None:
        set_nested(json_data, ["filter", "tagIds", "any"], filter_tag_ids_any)
    if filter_tag_ids_none is not None:
        set_nested(json_data, ["filter", "tagIds", "none"], filter_tag_ids_none)
    if filter_taken_at_eq is not None:
        set_nested(json_data, ["filter", "takenAt", "eq"], filter_taken_at_eq)
    if filter_taken_at_gt is not None:
        set_nested(json_data, ["filter", "takenAt", "gt"], filter_taken_at_gt)
    if filter_taken_at_gte is not None:
        set_nested(json_data, ["filter", "takenAt", "gte"], filter_taken_at_gte)
    if filter_taken_at_lt is not None:
        set_nested(json_data, ["filter", "takenAt", "lt"], filter_taken_at_lt)
    if filter_taken_at_lte is not None:
        set_nested(json_data, ["filter", "takenAt", "lte"], filter_taken_at_lte)
    if filter_taken_at_ne is not None:
        set_nested(json_data, ["filter", "takenAt", "ne"], filter_taken_at_ne)
    if filter_trashed_at_eq is not None:
        set_nested(json_data, ["filter", "trashedAt", "eq"], filter_trashed_at_eq)
    if filter_trashed_at_gt is not None:
        set_nested(json_data, ["filter", "trashedAt", "gt"], filter_trashed_at_gt)
    if filter_trashed_at_gte is not None:
        set_nested(json_data, ["filter", "trashedAt", "gte"], filter_trashed_at_gte)
    if filter_trashed_at_lt is not None:
        set_nested(json_data, ["filter", "trashedAt", "lt"], filter_trashed_at_lt)
    if filter_trashed_at_lte is not None:
        set_nested(json_data, ["filter", "trashedAt", "lte"], filter_trashed_at_lte)
    if filter_trashed_at_ne is not None:
        set_nested(json_data, ["filter", "trashedAt", "ne"], filter_trashed_at_ne)
    if filter_type_eq is not None:
        set_nested(json_data, ["filter", "type", "eq"], filter_type_eq)
    if filter_type_in_ is not None:
        set_nested(json_data, ["filter", "type", "in"], filter_type_in_)
    if filter_type_ne is not None:
        set_nested(json_data, ["filter", "type", "ne"], filter_type_ne)
    if filter_type_not_in is not None:
        set_nested(json_data, ["filter", "type", "notIn"], filter_type_not_in)
    if filter_updated_at_eq is not None:
        set_nested(json_data, ["filter", "updatedAt", "eq"], filter_updated_at_eq)
    if filter_updated_at_gt is not None:
        set_nested(json_data, ["filter", "updatedAt", "gt"], filter_updated_at_gt)
    if filter_updated_at_gte is not None:
        set_nested(json_data, ["filter", "updatedAt", "gte"], filter_updated_at_gte)
    if filter_updated_at_lt is not None:
        set_nested(json_data, ["filter", "updatedAt", "lt"], filter_updated_at_lt)
    if filter_updated_at_lte is not None:
        set_nested(json_data, ["filter", "updatedAt", "lte"], filter_updated_at_lte)
    if filter_updated_at_ne is not None:
        set_nested(json_data, ["filter", "updatedAt", "ne"], filter_updated_at_ne)
    if filter_visibility_eq is not None:
        set_nested(json_data, ["filter", "visibility", "eq"], filter_visibility_eq)
    if filter_visibility_in_ is not None:
        set_nested(json_data, ["filter", "visibility", "in"], filter_visibility_in_)
    if filter_visibility_ne is not None:
        set_nested(json_data, ["filter", "visibility", "ne"], filter_visibility_ne)
    if filter_visibility_not_in is not None:
        set_nested(
            json_data, ["filter", "visibility", "notIn"], filter_visibility_not_in
        )
    if is_encoded is not None:
        set_nested(json_data, ["isEncoded"], is_encoded.lower() == "true")
    if is_favorite is not None:
        set_nested(json_data, ["isFavorite"], is_favorite.lower() == "true")
    if is_motion is not None:
        set_nested(json_data, ["isMotion"], is_motion.lower() == "true")
    if is_not_in_album is not None:
        set_nested(json_data, ["isNotInAlbum"], is_not_in_album.lower() == "true")
    if is_offline is not None:
        set_nested(json_data, ["isOffline"], is_offline.lower() == "true")
    if language is not None:
        set_nested(json_data, ["language"], language)
    if lens_model is not None:
        set_nested(json_data, ["lensModel"], lens_model)
    if library_id is not None:
        set_nested(json_data, ["libraryId"], library_id)
    if make is not None:
        set_nested(json_data, ["make"], make)
    if model is not None:
        set_nested(json_data, ["model"], model)
    if ocr is not None:
        set_nested(json_data, ["ocr"], ocr)
    if page is not None:
        set_nested(json_data, ["page"], page)
    if person_ids is not None:
        set_nested(json_data, ["personIds"], person_ids)
    if query is not None:
        set_nested(json_data, ["query"], query)
    if query_asset_id is not None:
        set_nested(json_data, ["queryAssetId"], query_asset_id)
    if rating is not None:
        set_nested(json_data, ["rating"], rating)
    if size is not None:
        set_nested(json_data, ["size"], size)
    if state is not None:
        set_nested(json_data, ["state"], state)
    if tag_ids is not None:
        set_nested(json_data, ["tagIds"], tag_ids)
    if taken_after is not None:
        set_nested(json_data, ["takenAfter"], taken_after)
    if taken_before is not None:
        set_nested(json_data, ["takenBefore"], taken_before)
    if trashed_after is not None:
        set_nested(json_data, ["trashedAfter"], trashed_after)
    if trashed_before is not None:
        set_nested(json_data, ["trashedBefore"], trashed_before)
    if type is not None:
        set_nested(json_data, ["type"], type)
    if updated_after is not None:
        set_nested(json_data, ["updatedAfter"], updated_after)
    if updated_before is not None:
        set_nested(json_data, ["updatedBefore"], updated_before)
    if visibility is not None:
        set_nested(json_data, ["visibility"], visibility)
    if with_deleted is not None:
        set_nested(json_data, ["withDeleted"], with_deleted.lower() == "true")
    if with_exif is not None:
        set_nested(json_data, ["withExif"], with_exif.lower() == "true")
    smart_search_dto = SmartSearchDto.model_validate(json_data)
    kwargs["smart_search_dto"] = smart_search_dto
    client: AsyncClient = ctx.obj["client"]
    result = run_command(client.search.search_smart, ctx=ctx, **kwargs)
    print_response(result, ctx=ctx)
