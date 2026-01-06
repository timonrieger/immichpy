from __future__ import annotations

from pathlib import Path
from typing import Any, Optional
from uuid import UUID

from pydantic import StrictStr

from immich.client.api.assets_api import AssetsApi
from immich.client.models.asset_media_size import AssetMediaSize
from immich.utils import filename_from_headers


class AssetsApiWrapped(AssetsApi):
    async def download_asset_to_file(
        self,
        id: UUID,
        out_dir: Path,
        key: Optional[StrictStr] = None,
        slug: Optional[StrictStr] = None,
        fallback_base: Optional[str] = None,
        **kwargs: Any,
    ) -> Path:
        """
        Download an asset to a file.

        :param id: The asset ID.
        :param out_dir: The directory to write the asset to.
        :param key: Public share key (the last path segment of a public share URL, i.e. `/share/<key>`). When provided, the asset can be accessed via the public share link without an API key. Typically you pass either `key` or `slug`.
        :param slug: Public share slug for custom share URLs (the last path segment of `/s/<slug>`). Allows access without authentication. Typically you pass either `slug` or `key`.
        :param fallback_base: The fallback base for the filename. We try to derive the original filename from the headers, but if we fail, we use this base. For example, you could use "video-" + asset_id as a prefix. Defaults to "orig-" + asset_id.
        :param kwargs: Additional arguments to pass to the `download_asset_with_http_info` method.

        For exact request/response behavior, inspect `AssetsApi.download_asset_with_http_info`
        in the generated client.
        """
        resp = await super().download_asset_with_http_info(
            id=id, key=key, slug=slug, **kwargs
        )
        name = filename_from_headers(
            resp.headers,
            fallback_base=fallback_base or f"orig-{id}",
        )
        if not name:
            raise ValueError(f"Cannot derive filename from headers={resp.headers!r}")

        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / name
        out_path.write_bytes(bytes(resp.data))
        return out_path

    async def view_asset_to_file(
        self,
        id: UUID,
        out_dir: Path,
        key: Optional[StrictStr] = None,
        size: Optional[AssetMediaSize] = None,
        slug: Optional[StrictStr] = None,
        fallback_base: Optional[str] = None,
        **kwargs: Any,
    ) -> Path:
        """
        Save an asset's thumbnail to a file.

        :param id: The asset ID.
        :param out_dir: The directory to write the asset to.
        :param key: Public share key (the last path segment of a public share URL, i.e. `/share/<key>`). When provided, the thumbnail can be fetched via the public share link without an API key. Typically you pass either `key` or `slug`.
        :param size: Thumbnail size.
        :param slug: Public share slug for custom share URLs (the last path segment of `/s/<slug>`). Allows access without authentication. Typically you pass either `slug` or `key`.
        :param fallback_base: The fallback base for the filename. We try to derive the original filename from the headers, but if we fail, we use this base. For example, you could use "video-" + asset_id as a prefix. Defaults to "orig-" + asset_id.
        :param kwargs: Additional arguments to pass to the `view_asset_with_http_info` method.

        For exact request/response behavior, inspect `AssetsApi.view_asset_with_http_info`
        in the generated client.
        """
        resp = await super().view_asset_with_http_info(
            id=id, key=key, size=size, slug=slug, **kwargs
        )
        name = filename_from_headers(
            resp.headers,
            fallback_base=fallback_base or f"thumb-{id}",
        )
        if not name:
            raise ValueError(f"Cannot derive filename from headers={resp.headers!r}")

        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / name
        out_path.write_bytes(bytes(resp.data))
        return out_path
