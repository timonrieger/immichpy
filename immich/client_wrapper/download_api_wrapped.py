from __future__ import annotations

import uuid
from pathlib import Path
from typing import Any, Optional

import tqdm
from pydantic import StrictStr

from immich.client.api.download_api import DownloadApi
from immich.client.models.asset_ids_dto import AssetIdsDto
from immich.client.models.download_info_dto import DownloadInfoDto


class DownloadApiWrapped(DownloadApi):
    async def download_archive_to_file(
        self,
        download_info: DownloadInfoDto,
        out_dir: Path,
        key: Optional[StrictStr] = None,
        slug: Optional[StrictStr] = None,
        show_progress_bars: bool = True,
        **kwargs: Any,
    ) -> list[Path]:
        """
        Download one or more asset archives and save them to ZIP files.

        Note: This method intentionally downloads archives **sequentially** (not in parallel) by default.
        Immich has to build ZIP archives server-side; parallelizing many archive requests can put significant
        CPU/disk load on the Immich server and may lead to timeouts or degraded performance for other users.
        If you choose to parallelize, keep concurrency low and do so at your own risk.

        :param download_info: The download info (two-step flow; downloads all archives returned by `get_download_info`).
        :param out_dir: The directory to write the ZIP archive to.
        :param key: Public share key (the last path segment of a public share URL, i.e. `/share/<key>`). Allows access without authentication. Typically you pass either `key` or `slug`.
        :param slug: Public share slug for custom share URLs (the last path segment of `/s/<slug>`). Allows access without authentication. Typically you pass either `slug` or `key`.
        :param show_progress_bars: Whether to show tqdm progress bars (per-archive bytes + overall archive count).
        :param kwargs: Additional arguments to pass to the underlying SDK calls.

        :return: The list of paths to the downloaded archives.

        For exact request/response behavior, inspect `DownloadApi.download_archive_without_preload_content`
        in the generated client.
        """
        out_dir.mkdir(parents=True, exist_ok=True)

        # Normalize to a list of archive requests.
        info = await super().get_download_info(
            download_info, key=key, slug=slug, **kwargs
        )
        archive_requests: list[tuple[AssetIdsDto, int]] = [
            (AssetIdsDto(asset_ids=archive.asset_ids), int(archive.size))
            for archive in info.archives
        ]

        out_paths: list[Path] = []

        archives_pbar = tqdm.tqdm(
            total=len(archive_requests),
            desc="archives",
            unit="archive",
            position=0,
            leave=True,
            dynamic_ncols=True,
            disable=not show_progress_bars,
        )
        try:
            for asset_ids_dto, expected_size in archive_requests:
                resp = await super().download_archive_without_preload_content(
                    asset_ids_dto=asset_ids_dto,
                    key=key,
                    slug=slug,
                    **kwargs,
                )

                out_path = out_dir / f"archive-{uuid.uuid4()}.zip"
                temp_path = out_path.with_suffix(out_path.suffix + ".part")

                bytes_pbar = tqdm.tqdm(
                    total=expected_size or None,
                    unit="B",
                    unit_scale=True,
                    desc=str(out_path.name),
                    position=1,
                    leave=False,
                    dynamic_ncols=True,
                    disable=not show_progress_bars,
                )
                try:
                    async with resp:
                        with temp_path.open("wb") as f:
                            async for chunk in resp.content.iter_chunked(1024 * 1024):
                                if not chunk:
                                    continue
                                f.write(chunk)
                                bytes_pbar.update(len(chunk))
                finally:
                    bytes_pbar.close()

                temp_path.replace(out_path)
                out_paths.append(out_path)
                archives_pbar.update(1)
        finally:
            archives_pbar.close()

        return out_paths
