# Examples

Every Immich API endpoint is a command, and every command prints JSON. Combine them with [jq](https://jqlang.org/) or a shell script to automate your library.

## Ideas

Not sure where to start? Pick a goal and explore the commands in the [reference](reference.md):

| Goal | Commands to start with |
|---|---|
| Upload a folder or SD card into an album | [`assets upload`](reference.md#immichpy-assets-upload) |
| Share an album with people without an account | [`shared-links create-shared-link`](reference.md#immichpy-shared-links-create-shared-link) |
| Find assets by camera, place, date or file path | [`search search-assets`](reference.md#immichpy-search-search-assets), [`search search-asset-statistics`](reference.md#immichpy-search-search-asset-statistics) |
| Fix the date or location of many assets at once | [`assets update-assets`](reference.md#immichpy-assets-update-assets) |
| Tag or sort assets in bulk | [`tags bulk-tag-assets`](reference.md#immichpy-tags-bulk-tag-assets), [`albums add-assets-to-album`](reference.md#immichpy-albums-add-assets-to-album) |
| Clean up duplicates | [`duplicates get-asset-duplicates`](reference.md#immichpy-duplicates-get-asset-duplicates), [`duplicates resolve-duplicates`](reference.md#immichpy-duplicates-resolve-duplicates) |
| Onboard family members | [`users-admin create-user-admin`](reference.md#immichpy-users-admin-create-user-admin), [`partners create-partner`](reference.md#immichpy-partners-create-partner) |
| Monitor storage per user | [`server get-server-statistics`](reference.md#immichpy-server-get-server-statistics) |
| Pause machine learning during a large import | [`queues update-queue`](reference.md#immichpy-queues-update-queue), [`libraries scan-library`](reference.md#immichpy-libraries-scan-library) |

## List all albums

See [`albums get-all-albums`](reference.md#immichpy-albums-get-all-albums).

<!-- termynal -->

```console
$ immichpy albums get-all-albums | jq -r '.[] | "\(.album_name) \(.id)"'
Animal Portraits ff09c49f-525d-4216-bc5a-8ff070bca149
Vacation 2023 851c8f67-9bf3-48f5-8130-59da9ab17c06
```

## Upload a folder into an album

See [`assets upload`](reference.md#immichpy-assets-upload).

<!-- termynal -->

```console
$ immichpy assets upload /Volumes/SD/DCIM/ --album-name "Paris 2025" --show-progress

---> 100%
```

## Share an album with a link

See [`shared-links create-shared-link`](reference.md#immichpy-shared-links-create-shared-link). The link is `<your server>/share/<key>`.

<!-- termynal -->

```console
$ immichpy shared-links create-shared-link --type ALBUM \
  --album-id 851c8f67-9bf3-48f5-8130-59da9ab17c06 --password s3cret | jq -r .key
5CCZJL7zI2QW6NVCkE6aX1_HRWiX0TGY620sjVFfiZWxpYvYf886SNy6vcwOt2FciBQ
```

## Share an album with multiple users

See [`albums add-users-to-album`](reference.md#immichpy-albums-add-users-to-album).

<!-- termynal -->

```console
$ immichpy albums add-users-to-album 851c8f67-9bf3-48f5-8130-59da9ab17c06 \
  --album-users '{"userId":"0025cccf-27ca-4973-9be1-ffb549b10441","role":"viewer"}' \
  --album-users '{"userId":"033dda4c-5009-4475-afa5-dcc8ed2e5885","role":"viewer"}'
```

## Download an album

See [`download download-archive-to-file`](reference.md#immichpy-download-download-archive-to-file).

<!-- termynal -->

```console
$ immichpy download download-archive-to-file out-dir/ \
  --album-id 851c8f67-9bf3-48f5-8130-59da9ab17c06 --show-progress

---> 100%
```

## Count assets from a camera

See [`search search-asset-statistics`](reference.md#immichpy-search-search-asset-statistics) and [`search get-search-suggestions`](reference.md#immichpy-search-get-search-suggestions) for the camera makes.

<!-- termynal -->

```console
$ immichpy search search-asset-statistics --make GoPro
{
  "total": 15
}
```

## Show storage usage per user

See [`server get-server-statistics`](reference.md#immichpy-server-get-server-statistics).

<!-- termynal -->

```console
$ immichpy server get-server-statistics | jq -r '.usage_by_user[] | "\(.user_name) \(.photos) photos"'
Jane Doe 32566 photos
Jason 26 photos
```

## Use another profile

See the global options in the [reference](reference.md) and [Authentication](authentication.md).

<!-- termynal -->

```console
$ immichpy -p family albums get-all-albums | jq length
12
```
