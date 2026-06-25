# Features

immichpy's core is a thin, schema-driven layer over the Immich API. On top of that core, a small set of hand-written convenience features cover common operations that are awkward to do with the raw endpoints. These are **preferred** over the auto-generated equivalents for the operations they cover.

## Upload

Upload files or directories with a single call, with recursive scanning, SHA1 duplicate detection, album assignment, sidecar support, and a dry-run mode. ([CLI](../cli/reference.md#immichpy-assets-upload), [Client](../client/reference/custom/assets_api_wrapped.md#immichpy.client.wrapper.assets_api_wrapped.AssetsApiWrapped.upload))

!!! tip "Choosing the right tool"
    immichpy's upload is built for **scripted ingestion from Python**. For **migrating** Google Photos or iCloud takeouts — with metadata preservation, stacking, and folder-derived albums — use [immich-go](https://github.com/simulot/immich-go). The two are complementary: automation versus migration.

## Downloads

- Download an asset (original file) directly to disk. ([CLI](../cli/reference.md#immichpy-assets-download-asset-to-file), [Client](../client/reference/custom/assets_api_wrapped.md#immichpy.client.wrapper.assets_api_wrapped.AssetsApiWrapped.download_asset_to_file))
- Download an asset thumbnail directly to disk. ([CLI](../cli/reference.md#immichpy-assets-view-asset-to-file), [Client](../client/reference/custom/assets_api_wrapped.md#immichpy.client.wrapper.assets_api_wrapped.AssetsApiWrapped.view_asset_to_file))
- Download an asset video stream directly to disk. ([CLI](../cli/reference.md#immichpy-assets-play-asset-video-to-file), [Client](../client/reference/custom/assets_api_wrapped.md#immichpy.client.wrapper.assets_api_wrapped.AssetsApiWrapped.play_asset_video_to_file))
- Download asset archives (ZIP files) directly to disk. You can download whole albums or user-specified assets in a single request. ([CLI](../cli/reference.md#immichpy-download-download-archive-to-file), [Client](../client/reference/custom/download_api_wrapped.md#immichpy.client.wrapper.download_api_wrapped.DownloadApiWrapped.download_archive_to_file))
- Download a user's profile image directly to disk. ([CLI](../cli/reference.md#immichpy-users-get-profile-image-to-file), [Client](../client/reference/custom/users_api_wrapped.md#immichpy.client.wrapper.users_api_wrapped.UsersApiWrapped.get_profile_image_to_file))

!!! info "Resumable Downloads"
    All of the asset download methods support automatic resumable downloads. Archive downloads (ZIP files) do not, due to the nature of streaming archives.
