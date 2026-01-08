from __future__ import annotations

from pathlib import Path
from typing import Any, Optional
from uuid import UUID

from pydantic import StrictStr

from immich.client.api.albums_api import AlbumsApi
from immich.client.api.assets_api import AssetsApi
from immich.client.api.server_api import ServerApi
from immich.client.models.asset_media_size import AssetMediaSize
from immich.upload import (
    UploadResult,
    UploadStats,
    check_duplicates as check_dupes,
    delete_files,
    scan_files,
    update_albums,
    upload_files,
)
from immich.utils import download_file, resolve_output_filename


class AssetsApiWrapped(AssetsApi):
    async def download_asset_to_file(
        self,
        id: UUID,
        out_dir: Path,
        key: Optional[StrictStr] = None,
        slug: Optional[StrictStr] = None,
        filename: Optional[str] = None,
        show_progress: bool = True,
        **kwargs: Any,
    ) -> Path:
        """
        Download an asset to a file.

        :param id: The asset ID.
        :param out_dir: The directory to write the asset to.
        :param key: Public share key (the last path segment of a public share URL, i.e. `/share/<key>`). When provided, the asset can be accessed via the public share link without an API key. Typically you pass either `key` or `slug`.
        :param slug: Public share slug for custom share URLs (the last path segment of `/s/<slug>`). Allows access without authentication. Typically you pass either `slug` or `key`.
        :param filename: The filename to use. If not provided, we use the original filename from the headers or default to "orig-" + asset_id.
        :param show_progress: Whether to show a tqdm progress bar while downloading.
        :param kwargs: Additional arguments to pass to the `download_asset_without_preload_content` method.

        For exact request/response behavior, inspect `AssetsApi.download_asset_without_preload_content`
        in the generated client.
        """
        out_dir.mkdir(parents=True, exist_ok=True)

        def make_request(extra_headers: Optional[dict[str, str]]):
            return self.download_asset_without_preload_content(
                id=id,
                key=key,
                slug=slug,
                _headers=kwargs.get("_headers", {}) | (extra_headers or {}),
                **kwargs,
            )

        return await download_file(
            make_request=make_request,
            out_dir=out_dir,
            resolve_filename=lambda headers: resolve_output_filename(
                headers,
                name=filename,
                default_base=f"orig-{id}",
            ),
            show_progress=show_progress,
        )

    async def play_asset_video_to_file(
        self,
        id: UUID,
        out_dir: Path,
        key: Optional[StrictStr] = None,
        slug: Optional[StrictStr] = None,
        filename: Optional[str] = None,
        show_progress: bool = True,
        **kwargs: Any,
    ) -> Path:
        """
        Save an asset's video stream to a file.

        :param id: The asset ID.
        :param out_dir: The directory to write the video to.
        :param key: Public share key (the last path segment of a public share URL, i.e. `/share/<key>`). When provided, the asset can be accessed via the public share link without an API key. Typically you pass either `key` or `slug`.
        :param slug: Public share slug for custom share URLs (the last path segment of `/s/<slug>`). Allows access without authentication. Typically you pass either `slug` or `key`.
        :param filename: The filename to use. If not provided, we use the original filename from the headers or default to "video-" + asset_id.
        :param show_progress: Whether to show a tqdm progress bar while downloading.
        :param kwargs: Additional arguments to pass to the `play_asset_video_without_preload_content` method.

        For exact request/response behavior, inspect `AssetsApi.play_asset_video_without_preload_content`
        in the generated client.
        """
        out_dir.mkdir(parents=True, exist_ok=True)

        def make_request(extra_headers: Optional[dict[str, str]]):
            return self.play_asset_video_without_preload_content(
                id=id,
                key=key,
                slug=slug,
                _headers=kwargs.get("_headers", {}) | (extra_headers or {}),
                **kwargs,
            )

        return await download_file(
            make_request=make_request,
            out_dir=out_dir,
            resolve_filename=lambda headers: resolve_output_filename(
                headers,
                name=filename,
                default_base=f"video-{id}",
            ),
            show_progress=show_progress,
        )

    async def view_asset_to_file(
        self,
        id: UUID,
        out_dir: Path,
        key: Optional[StrictStr] = None,
        size: Optional[AssetMediaSize] = None,
        slug: Optional[StrictStr] = None,
        filename: Optional[str] = None,
        show_progress: bool = True,
        **kwargs: Any,
    ) -> Path:
        """
        Save an asset's thumbnail to a file.

        :param id: The asset ID.
        :param out_dir: The directory to write the asset to.
        :param key: Public share key (the last path segment of a public share URL, i.e. `/share/<key>`). When provided, the thumbnail can be fetched via the public share link without an API key. Typically you pass either `key` or `slug`.
        :param size: Thumbnail size.
        :param slug: Public share slug for custom share URLs (the last path segment of `/s/<slug>`). Allows access without authentication. Typically you pass either `slug` or `key`.
        :param filename: The filename to use. If not provided, we use the original filename from the headers or default to "thumb-" + asset_id.
        :param show_progress: Whether to show a tqdm progress bar while downloading.
        :param kwargs: Additional arguments to pass to the `view_asset_without_preload_content` method.

        For exact request/response behavior, inspect `AssetsApi.view_asset_without_preload_content`
        in the generated client.
        """
        out_dir.mkdir(parents=True, exist_ok=True)

        def make_request(extra_headers: Optional[dict[str, str]]):
            return self.view_asset_without_preload_content(
                id=id,
                key=key,
                size=size,
                slug=slug,
                _headers=kwargs.get("_headers", {}) | (extra_headers or {}),
                **kwargs,
            )

        return await download_file(
            make_request=make_request,
            out_dir=out_dir,
            resolve_filename=lambda headers: resolve_output_filename(
                headers,
                name=filename,
                default_base=f"thumb-{id}",
            ),
            show_progress=show_progress,
        )

    async def upload(
        self,
        paths: Path | list[Path] | str | list[str],
        *,
        ignore_pattern: Optional[str] = None,
        include_hidden: bool = False,
        check_duplicates: bool = True,
        concurrency: int = 5,
        show_progress: bool = True,
        include_sidecars: bool = True,
        album_name: Optional[str] = None,
        delete_after_upload: bool = False,
        delete_duplicates: bool = False,
        dry_run: bool = False,
    ) -> UploadResult:
        """
        Upload files from the given paths with duplicate detection, optional album assignment, sidecar handling, and configurable deletion or dry-run behavior.
        
        Parameters:
            paths: A Path, string, or list of those pointing to files and/or directories to upload. Directories are scanned recursively.
            ignore_pattern: Wildcard pattern (fnmatch) to exclude matching files.
            include_hidden: Include files and directories whose names start with '.'.
            check_duplicates: If true, skip files already present on the server by comparing SHA1 hashes.
            concurrency: Maximum number of concurrent uploads.
            show_progress: Display progress indicators during scanning and uploading.
            include_sidecars: Detect and upload XMP sidecar files alongside their primary files.
            album_name: If provided, add uploaded assets to this album (create it if necessary).
            delete_after_upload: Remove successfully uploaded files from local disk.
            delete_duplicates: Remove locally detected duplicate files.
            dry_run: Simulate the entire workflow without performing uploads or deletions.
        
        Returns:
            UploadResult: Lists of uploaded asset identifiers, duplicates, failed uploads, and an UploadStats summary.
        """
        server_api = ServerApi(self.api_client)
        albums_api = AlbumsApi(self.api_client)

        files = await scan_files(paths, server_api, ignore_pattern, include_hidden)
        if not files:
            return UploadResult(
                uploaded=[],
                duplicates=[],
                failed=[],
                stats=UploadStats(total=0, uploaded=0, duplicates=0, failed=0),
            )

        new_files, duplicates = await check_dupes(
            files=files,
            assets_api=self,
            check_duplicates=check_duplicates,
            show_progress=show_progress,
        )

        uploaded, failed = await upload_files(
            files=new_files,
            assets_api=self,
            concurrency=concurrency,
            show_progress=show_progress,
            include_sidecars=include_sidecars,
            dry_run=dry_run,
        )

        await update_albums(
            uploaded=uploaded, album_name=album_name, albums_api=albums_api
        )

        await delete_files(
            uploaded=uploaded,
            duplicates=duplicates,
            delete_after_upload=delete_after_upload,
            delete_duplicates=delete_duplicates,
            include_sidecars=include_sidecars,
            dry_run=dry_run,
        )

        return UploadResult(
            uploaded=[asset for asset, _ in uploaded],
            duplicates=duplicates,
            failed=failed,
            stats=UploadStats(
                total=len(files),
                uploaded=len(uploaded),
                duplicates=len(duplicates),
                failed=len(failed),
            ),
        )