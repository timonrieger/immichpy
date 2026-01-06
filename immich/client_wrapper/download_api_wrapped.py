from __future__ import annotations

import uuid
from pathlib import Path
from typing import Any, Optional

from pydantic import StrictStr

from immich.client.api.download_api import DownloadApi
from immich.client.models.asset_ids_dto import AssetIdsDto
from immich.utils import resolve_output_filename


class DownloadApiWrapped(DownloadApi):
    async def download_archive_to_file(
        self,
        asset_ids_dto: AssetIdsDto,
        out_dir: Path,
        filename: Optional[str] = None,
        key: Optional[StrictStr] = None,
        slug: Optional[StrictStr] = None,
        **kwargs: Any,
    ) -> Path:
        """
        Download an asset archive and save it to a ZIP file.

        :param asset_ids_dto: The archive asset IDs (must be obtained via `get_download_info` first).
        :param out_dir: The directory to write the ZIP archive to.
        :param filename: Output filename (without extension; any extension is stripped). If omitted, defaults to `archive-<uuid>.zip`.
        :param key: Public share key (the last path segment of a public share URL, i.e. `/share/<key>`). Allows access without authentication. Typically you pass either `key` or `slug`.
        :param slug: Public share slug for custom share URLs (the last path segment of `/s/<slug>`). Allows access without authentication. Typically you pass either `slug` or `key`.
        :param kwargs: Additional arguments to pass to the `download_archive_with_http_info` method.

        For exact request/response behavior, inspect `DownloadApi.download_archive_with_http_info`
        in the generated client.
        """
        resp = await super().download_archive_with_http_info(
            asset_ids_dto=asset_ids_dto, key=key, slug=slug, **kwargs
        )

        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / resolve_output_filename(
            resp.headers,
            name=filename,
            default_base=f"archive-{uuid.uuid4()}",
            default_ext=".zip",
        )
        out_path.write_bytes(bytes(resp.data))
        return out_path
