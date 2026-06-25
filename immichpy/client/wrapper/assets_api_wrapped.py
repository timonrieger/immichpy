from __future__ import annotations

from collections.abc import AsyncIterator
from pathlib import Path
from typing import Any, cast
from uuid import UUID

from pydantic import StrictStr

from immichpy.client.generated.api.albums_api import AlbumsApi
from immichpy.client.generated.api.assets_api import AssetsApi
from immichpy.client.generated.api.server_api import ServerApi
from immichpy.client.generated.models.asset_media_response_dto import (
    AssetMediaResponseDto,
)
from immichpy.client.generated.models.asset_media_size import AssetMediaSize
from immichpy.client.utils.upload import (
    check_duplicates as check_dupes,
    delete_files,
    scan_files,
    stream_uploads,
    update_albums,
)
from immichpy.client.utils.download import download_file, resolve_output_filename
from immichpy.client.types import (
    FailedEntry,
    HeadersType,
    RejectedEntry,
    UploadedEntry,
    UploadEvent,
    UploadResult,
    UploadStats,
)


class AssetsApiWrapped(AssetsApi):
    """Wrapper for the AssetsApi that provides convenience methods."""

    async def download_asset_to_file(
        self,
        id: UUID,
        out_dir: Path,
        key: StrictStr | None = None,
        slug: StrictStr | None = None,
        filename: str | None = None,
        show_progress: bool = False,
        **kwargs: Any,
    ) -> Path:
        """
        Download an asset to a file.

        :param id: The asset ID.
        :param out_dir: The directory to write the asset to.
        :param key: Public share key (the last path segment of a public share URL, i.e. `/share/<key>`). When provided, the asset can be accessed via the public share link without an API key. Typically you pass either `key` or `slug`.
        :param slug: Public share slug for custom share URLs (the last path segment of `/s/<slug>`). Allows access without authentication. Typically you pass either `slug` or `key`.
        :param filename: The filename to use. If not provided, we use the original filename from the headers or default to "orig-" + asset_id.
        :param show_progress: Whether to show a progress bar while downloading.
        :param kwargs: Additional arguments to pass to the `download_asset_without_preload_content` method.
        :return: The path to the downloaded file.

        For exact request/response behavior, inspect `AssetsApi.download_asset_without_preload_content`
        in the generated client.
        """
        out_dir.mkdir(parents=True, exist_ok=True)

        def make_request(extra_headers: HeadersType | None):
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
        key: StrictStr | None = None,
        slug: StrictStr | None = None,
        filename: str | None = None,
        show_progress: bool = False,
        **kwargs: Any,
    ) -> Path:
        """
        Save an asset's video stream to a file.

        :param id: The asset ID.
        :param out_dir: The directory to write the video to.
        :param key: Public share key (the last path segment of a public share URL, i.e. `/share/<key>`). When provided, the asset can be accessed via the public share link without an API key. Typically you pass either `key` or `slug`.
        :param slug: Public share slug for custom share URLs (the last path segment of `/s/<slug>`). Allows access without authentication. Typically you pass either `slug` or `key`.
        :param filename: The filename to use. If not provided, we use the original filename from the headers or default to "video-" + asset_id.
        :param show_progress: Whether to show a progress bar while downloading.
        :param kwargs: Additional arguments to pass to the [AssetsApi.play_asset_video_without_preload_content][] method.
        :return: The path to the downloaded file.
        """
        out_dir.mkdir(parents=True, exist_ok=True)

        def make_request(extra_headers: HeadersType | None):
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
        key: StrictStr | None = None,
        size: AssetMediaSize | None = None,
        slug: StrictStr | None = None,
        filename: str | None = None,
        show_progress: bool = False,
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
        :param show_progress: Whether to show a progress bar while downloading.
        :param kwargs: Additional arguments to pass to the [AssetsApi.view_asset_without_preload_content][] method.
        :return: The path to the downloaded file.
        """
        out_dir.mkdir(parents=True, exist_ok=True)

        def make_request(extra_headers: HeadersType | None):
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

    async def iter_upload(
        self,
        paths: Path | list[Path] | str | list[str],
        *,
        ignore_pattern: str | None = None,
        include_hidden: bool = False,
        skip_duplicates: bool = False,
        concurrency: int = 5,
        show_progress: bool = False,
        dry_run: bool = False,
    ) -> AsyncIterator[UploadEvent]:
        """
        Upload assets, yielding each file's outcome as soon as it is known.

        Streaming counterpart to :meth:`upload`. It performs the same scan,
        duplicate check, and concurrent upload, but yields a per-file
        :class:`UploadEvent` instead of collecting everything into an
        :class:`UploadResult`. Useful for large batches where you want to act on
        outcomes incrementally (logging, manifests, custom album/tag logic).

        Album management and local file deletion are not performed; compose them
        from the yielded events if needed. Outcomes are yielded in completion
        order, not input order.

        :param paths: File or directory paths to upload. Can be a single path or list of paths. Directories are automatically walked recursively. To ignore subdirectories, use the `ignore_pattern` parameter.
        :param ignore_pattern: Wildcard pattern to ignore files (uses `fnmatch` stdlib module, not regex). Examples: "*.tmp" (ignore all .tmp files), "*/subdir/*" (ignore files in subdir at any level).
        :param include_hidden: Whether to include hidden files (starting with ".").
        :param skip_duplicates: Whether to skip duplicate checking (might still get rejected on the server).
        :param concurrency: Number of concurrent uploads. Defaults to 5. A higher number may increase upload speed, but also increases the risk of rate limiting or other issues.
        :param show_progress: Whether to show progress bars.
        :param dry_run: Simulate uploads without actually uploading.
        :return: Async iterator of per-file :class:`UploadEvent` outcomes.
        """
        if concurrency < 1:
            raise ValueError("concurrency must be >= 1")
        server_api = ServerApi(self.api_client)

        _paths = [paths] if isinstance(paths, (str, Path)) else paths
        _paths = [Path(p) for p in _paths]

        files = await scan_files(_paths, server_api, ignore_pattern, include_hidden)
        if not files:
            return

        new_files, checked_rejected = await check_dupes(
            files=files,
            assets_api=self,
            skip_duplicates=skip_duplicates,
            show_progress=show_progress,
            dry_run=dry_run,
        )

        for entry in checked_rejected:
            yield UploadEvent(
                filepath=entry.filepath,
                outcome="rejected",
                asset_id=entry.asset_id,
                reason=entry.reason,
            )

        async for event in stream_uploads(
            new_files,
            self,
            concurrency=concurrency,
            show_progress=show_progress,
            dry_run=dry_run,
        ):
            yield event

    async def upload(
        self,
        paths: Path | list[Path] | str | list[str],
        *,
        ignore_pattern: str | None = None,
        include_hidden: bool = False,
        skip_duplicates: bool = False,
        concurrency: int = 5,
        show_progress: bool = False,
        album_name: str | None = None,
        delete_uploads: bool = False,
        delete_duplicates: bool = False,
        dry_run: bool = False,
    ) -> UploadResult:
        """
        Upload assets with smart features (duplicate detection, album management, sidecar support, dry run).

        Collects the per-file outcomes from :meth:`iter_upload` and additionally
        handles album assignment and local deletion. Use :meth:`iter_upload`
        directly to stream outcomes for large batches.

        :param paths: File or directory paths to upload. Can be a single path or list of paths. Directories are automatically walked recursively. To ignore subdirectories, use the `ignore_pattern` parameter.
        :param ignore_pattern: Wildcard pattern to ignore files (uses `fnmatch` stdlib module, not regex). Examples: "*.tmp" (ignore all .tmp files), "*/subdir/*" (ignore files in subdir at any level).
        :param include_hidden: Whether to include hidden files (starting with ".").
        :param skip_duplicates: Whether to skip duplicate checking (might still get rejected on the server).
        :param concurrency: Number of concurrent uploads. Defaults to 5. A higher number may increase upload speed, but also increases the risk of rate limiting or other issues.
        :param show_progress: Whether to show progress bars.
        :param album_name: Album name to create or use. If None, no album operations are performed.
        :param delete_uploads: Whether to delete successfully uploaded files locally.
        :param delete_duplicates: Whether to delete duplicate files locally.
        :param dry_run: Simulate uploads without actually uploading.
        :return: UploadResult with uploaded assets, rejected files, failures, and statistics.
        """
        albums_api = AlbumsApi(self.api_client)

        uploaded: list[UploadedEntry] = []
        rejected: list[RejectedEntry] = []
        failed: list[FailedEntry] = []

        async for event in self.iter_upload(
            paths,
            ignore_pattern=ignore_pattern,
            include_hidden=include_hidden,
            skip_duplicates=skip_duplicates,
            concurrency=concurrency,
            show_progress=show_progress,
            dry_run=dry_run,
        ):
            if event.outcome == "uploaded":
                uploaded.append(
                    UploadedEntry(
                        asset=cast(AssetMediaResponseDto, event.asset),
                        filepath=event.filepath,
                    )
                )
            elif event.outcome == "rejected":
                rejected.append(
                    RejectedEntry(
                        filepath=event.filepath,
                        asset_id=event.asset_id,
                        reason=event.reason,
                    )
                )
            else:
                failed.append(
                    FailedEntry(filepath=event.filepath, error=cast(str, event.error))
                )

        if album_name and not dry_run:
            uploaded_ids = [ent.asset.id for ent in uploaded]
            duplicate_ids = [
                ent.asset_id
                for ent in rejected
                if ent.asset_id is not None and ent.reason == "duplicate"
            ]
            await update_albums(
                asset_ids=uploaded_ids + duplicate_ids,
                album_name=album_name,
                albums_api=albums_api,
            )

        await delete_files(
            uploaded=uploaded,
            rejected=rejected,
            delete_uploads=delete_uploads,
            delete_duplicates=delete_duplicates,
            dry_run=dry_run,
        )

        return UploadResult(
            uploaded=uploaded,
            rejected=rejected,
            failed=failed,
            stats=UploadStats(
                total=len(uploaded) + len(rejected) + len(failed),
                uploaded=len(uploaded),
                rejected=len(rejected),
                failed=len(failed),
            ),
        )
