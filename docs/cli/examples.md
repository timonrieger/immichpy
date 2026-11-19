# Examples

This page contains practical examples of using the immichpy CLI for common tasks, from first steps to automation.
> Have an example? You’re welcome to suggest it on [GitHub issues](https://github.com/timonrieger/immichpy/issues).

Most examples pipe JSON output into [jq](https://jqlang.org/). Commands that take a list repeat their flag (`--ids a --ids b`), so a jq filter like `"--ids \(.id)"` turns search results into arguments for the next command.

## First steps

### List all albums and parse with jq

Get all albums and their name and ID:

<!-- termynal -->

```console
$ immichpy albums get-all-albums | jq -r '.[] | "\(.album_name) \(.id)"'
Animal Portraits ff09c49f-525d-4216-bc5a-8ff070bca149
Vacation 2023 851c8f67-9bf3-48f5-8130-59da9ab17c06
Selfies c980670b-69d1-42ee-b4a5-86947f169d99
```

### List all users

Get all users in a table format:

<!-- termynal -->

```console
$ immichpy --format table users search-users
┏━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Key                ┃ Value                                ┃
┡━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ avatar_color       │ green                                │
│ email              │ admin@immich.cloud                   │
│ id                 │ f1c0dc5f-a938-4480-a27f-dcb127c421c6 │
│ name               │ admin                                │
│ profile_changed_at │ 2026-01-09 00:03:59.798000+00:00     │
│ profile_image_path │                                      │
└────────────────────┴──────────────────────────────────────┘

┏━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Key                ┃ Value                                ┃
┡━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ avatar_color       │ primary                              │
│ email              │ demo@immich.app                      │
│ id                 │ 6733f307-4f31-43b0-906c-95ea45d4680e │
│ name               │ demo                                 │
│ profile_changed_at │ 2025-11-11 16:45:16.871000+00:00     │
│ profile_image_path │                                      │
└────────────────────┴──────────────────────────────────────┘
```

### List all people with names

Get all people and filter to only show those with names:

<!-- termynal -->

```console
$ immichpy people get-all-people | jq '.people[] | select(.name != "")'
{
  "birth_date": null,
  "color": null,
  "id": "6130d2d5-5f96-4aa0-9725-36929c5c8f19",
  "is_favorite": false,
  "is_hidden": false,
  "name": "Timon",
  "thumbnail_path": "/data/thumbs/0245136d-b027-4144-a764-81ecca080cf8/
    61/30/6130d2d5-5f96-4aa0-9725-36929c5c8f19.jpeg",
  "updated_at": "2026-01-20 22:30:00.771000+00:00"
}
```

## Upload and share

### Upload a folder into an album

Upload a folder, such as an SD card, and add the assets to an album, creating it if it does not exist. Use `--dry-run` to preview what would be uploaded and `--show-progress` for progress bars:

<!-- termynal -->

```console
$ immichpy assets upload /Volumes/SD/DCIM/101NIKON/ --album-name "Paris 2025" --dry-run | jq .stats
{
  "total": 3,
  "uploaded": 3,
  "rejected": 0,
  "failed": 0
}

$ immichpy assets upload /Volumes/SD/DCIM/101NIKON/ --album-name "Paris 2025" --show-progress

---> 100%
```

### Share an album with a password-protected link

Create a shared link for people without an Immich account. The link is `<your server>/share/<key>`:

<!-- termynal -->

```console
$ immichpy shared-links create-shared-link --type ALBUM \
  --album-id cb3071c9-4fb6-49f1-87dd-fa8890b5cc42 \
  --password s3cret --allow-download true | jq -r '.key'
5CCZJL7zI2QW6NVCkE6aX1_HRWiX0TGY620sjVFfiZWxpYvYf886SNy6vcwOt2FciBQ
```

### Share an album with multiple users

Add multiple users to an album by repeating `--album-users`:

<!-- termynal -->

```console
$ immichpy albums add-users-to-album cccdd9f7-6a0f-4ed1-9dc0-ad8774ff9798 \
  --album-users '{"userId":"0025cccf-27ca-…","role":"viewer"}' \
  --album-users '{"userId":"033dda4c-5009-…","role":"viewer"}'
{
  "album_name": "2025'04 - April's Pictures",
  "album_users": [
    {
      "role": "editor",
      "user": {
        "email": "mich@immich.app",
        "id": "743f389e-ee80-4682-8d56-2cd45f692c40",
        "name": "Mich"
      }
    },
    {
      "role": "viewer",
      "user": {
        "email": "alex@immich.app",
        "id": "0025cccf-27ca-4973-9be1-ffb549b10441",
        "name": "Alex"
      }
    },
    {
      "role": "viewer",
      "user": {
        "email": "zack@immich.app",
        "id": "033dda4c-5009-4475-afa5-dcc8ed2e5885",
        "name": "Zack"
      }
    }
  ],
  ...
}
```

### Download an album archive

Download an album archive to a directory with progress bar:

<!-- termynal -->

```console
$ immichpy download download-archive-to-file out-dir/ \
 --album-id 851c8f67-9bf3-48f5-8130-59da9ab17c06 --show-progress

---> 100%

[
  "out-dir/archive-d73aaebe-f8d2-486d-b0f0-a0a64c75320b.zip"
]
```

## Organize your library

### Fix the date and location of an album

Set the same capture date and location on every asset in an album, for example scans that carry the date they were scanned. Immich reverse-geocodes the coordinates:

<!-- termynal -->

```console
$ immichpy assets update-assets \
  $(immichpy search search-assets --album-ids cb3071c9-4fb6-49f1-87dd-fa8890b5cc42 \
    | jq -r '.assets.items[] | "--ids \(.id)"') \
  --date-time-original "2025-05-14T12:00:00+02:00" --latitude 48.8584 --longitude 2.2945

$ immichpy search search-assets --album-ids cb3071c9-4fb6-49f1-87dd-fa8890b5cc42 --with-exif true \
  | jq -c '.assets.items[].exif_info | {date_time_original, city}'
{"date_time_original":"2025-05-14T10:00:00Z","city":"Paris 16 Passy"}
{"date_time_original":"2025-05-14T10:00:00Z","city":"Paris 16 Passy"}
{"date_time_original":"2025-05-14T10:00:00Z","city":"Paris 16 Passy"}
```

### Tag all photos taken with a camera

Count the assets from a camera, create a tag and apply it to all of them. `--make` must match exactly; list the values with `immichpy search get-search-suggestions --type camera-make`. A search returns at most 1000 assets per page, use `--page` for more:

<!-- termynal -->

```console
$ immichpy search search-asset-statistics --make GoPro
{
  "total": 15
}

$ TAG=$(immichpy tags upsert-tags --tags "Camera/GoPro" | jq -r '.[0].id')

$ immichpy tags bulk-tag-assets --tag-ids $TAG \
  $(immichpy search search-assets --make GoPro --size 1000 | jq -r '.assets.items[] | "--asset-ids \(.id)"')
{
  "count": 15
}
```

### Create an album for each folder

Create one album per folder, named after the folder. This is useful for external libraries with a meaningful folder structure:

```bash
immichpy views get-unique-original-paths | jq -r '.[]' | while read -r dir; do
  immichpy albums create-album --album-name "$(basename "$dir")" \
    $(immichpy views get-assets-by-original-path --path "$dir" | jq -r '.[] | "--asset-ids \(.id)"') \
    | jq -c '{album_name, asset_count}'
done
```

```console
{"album_name":"2019-Hiking","asset_count":42}
{"album_name":"2020-Wedding","asset_count":318}
```

### Clean up duplicates

Resolve every duplicate group by keeping the largest file and moving the others to the trash:

<!-- termynal -->

```console
$ immichpy duplicates get-asset-duplicates | jq length
1182

$ immichpy duplicates get-asset-duplicates \
  | jq -c '.[] | (.assets | sort_by(.exif_info.file_size_in_byte) | reverse) as $a
    | {duplicateId: .duplicate_id, keepAssetIds: [$a[0].id], trashAssetIds: [$a[1:][].id]}' \
  | while read -r group; do immichpy duplicates resolve-duplicates --groups "$group"; done
[
  {
    "error": null,
    "error_message": null,
    "id": "009f78bb-67a3-46d5-b03d-8a53ed15c412",
    "success": true
  }
]
...
```

### Delete assets listed in a file

Delete every asset whose path is listed in `files.txt`, one path per line. `--original-path` matches any part of the path, so prefer full paths. Deleted assets go to the trash unless you pass `--force true`:

```bash
while read -r path; do
  id=$(immichpy search search-assets --original-path "$path" | jq -r '.assets.items[0].id')
  if [ "$id" != null ]; then
    immichpy assets delete-assets --ids "$id" > /dev/null && echo "Deleted $id $path"
  else
    echo "Not found: $path"
  fi
done < files.txt
```

```console
Deleted 81acecd9-ac4e-467d-a007-d83783116997 /data/library/2004/01/IMGP0548.avi
Not found: /data/library/2004/01/IMGP0549.avi
```

## Administration

### Onboard a family member

Create an account with a storage quota and a forced password change, then share your library with them as a partner:

<!-- termynal -->

```console
$ immichpy users-admin create-user-admin --email alex@example.com --name Alex \
  --password change-me-123 --should-change-password true \
  --quota-size-in-bytes $((50 * 1024 ** 3)) | jq -r '.id'
04f0bbfd-9640-4b07-85c2-7f912cdfb65a

$ immichpy partners create-partner --shared-with-id 04f0bbfd-9640-4b07-85c2-7f912cdfb65a
{
  "email": "alex@example.com",
  "id": "04f0bbfd-9640-4b07-85c2-7f912cdfb65a",
  "name": "Alex",
  ...
}
```

### Show storage usage per user

Print photos and storage per user, for example for a dashboard or a cron job:

<!-- termynal -->

```console
$ immichpy server get-server-statistics \
  | jq -r '.usage_by_user[] | "\(.user_name) \(.photos) photos \(.usage / 1e9 * 100 | round / 100) GB"'
Jane Doe 32566 photos 13.43 GB
Alex 0 photos 0 GB
Jason 26 photos 0.1 GB
Mich 8 photos 0.03 GB
```

### Scan a library with machine learning paused

Pause the machine learning queues during a large import, trigger an external library scan, and resume them afterwards:

<!-- termynal -->

```console
$ immichpy libraries get-all-libraries | jq -r '.[] | "\(.name) \(.id)"'
Family Photos 098adb6d-0a9b-494a-bd66-2ae6c0bf28ff

$ for q in smartSearch faceDetection; do immichpy queues update-queue $q --is-paused true | jq -c '{name, is_paused}'; done
{"name":"smartSearch","is_paused":true}
{"name":"faceDetection","is_paused":true}

$ immichpy libraries scan-library 098adb6d-0a9b-494a-bd66-2ae6c0bf28ff

$ for q in smartSearch faceDetection; do immichpy queues update-queue $q --is-paused false | jq -c '{name, is_paused}'; done
{"name":"smartSearch","is_paused":false}
{"name":"faceDetection","is_paused":false}
```

### Run a command against several profiles

Select a profile per command with `--profile` (`-p`) or the `IMMICH_PROFILE` environment variable, or loop over profiles to run the same command for several accounts:

<!-- termynal -->

```console
$ IMMICH_PROFILE=family immichpy server get-about-info | jq -r .version
v2.4.0

$ for p in alice bob; do immichpy -p $p albums get-all-albums | jq length; done
12
4
```

### Rotate an API key

Rotate an API key and store the new secret in your profile. The secret is only shown once:

<!-- termynal -->

```console
$ immichpy config set profiles.default.api_key \
  --value "$(immichpy api-keys rotate-api-key 016601fa-3462-4299-8f73-84555c8043a4 | jq -r '.secret')"
```
