# Examples

This page contains practical examples of using the immichpy CLI for common tasks.

## List all albums and parse with jq

Get all albums and their name and ID using [`albums get-all-albums`](reference.md#immichpy-albums-get-all-albums):

<!-- termynal -->

```console
$ immichpy albums get-all-albums | jq -r '.[] | "\(.album_name) \(.id)"'
Animal Portraits ff09c49f-525d-4216-bc5a-8ff070bca149
Vacation 2023 851c8f67-9bf3-48f5-8130-59da9ab17c06
Selfies c980670b-69d1-42ee-b4a5-86947f169d99
```

## List all users

Get all users in a table format using [`users search-users`](reference.md#immichpy-users-search-users):

<!-- termynal -->

```console
$ immichpy --format table users search-users
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
…
```

## Upload a folder into an album

Upload a folder and add the assets to an album, creating it if it does not exist, using [`assets upload`](reference.md#immichpy-assets-upload):

<!-- termynal -->

```console
$ immichpy assets upload ~/Pictures/paris/ --album-name "Paris 2025"
{
  "uploaded": [
    {
      "asset": {
        "id": "81acecd9-ac4e-467d-a007-d83783116997",
        "status": "created"
      },
      "filepath": "~/Pictures/paris/IMG_0001.jpg"
    },
    …
  ],
  "rejected": [],
  "failed": [],
  "stats": {
    "total": 3,
    "uploaded": 3,
    "rejected": 0,
    "failed": 0
  }
}
```

## Download an album archive

Download an album archive to a directory with progress bar using [`download download-archive-to-file`](reference.md#immichpy-download-download-archive-to-file):

<!-- termynal -->

```console
$ immichpy download download-archive-to-file out-dir/ \
 --album-id 851c8f67-9bf3-48f5-8130-59da9ab17c06 --show-progress

---> 100%

[
  "out-dir/archive-d73aaebe-f8d2-486d-b0f0-a0a64c75320b.zip"
]
```

## Share an album with multiple users

Add multiple users to an album by repeating `--album-users` in [`albums add-users-to-album`](reference.md#immichpy-albums-add-users-to-album):

<!-- termynal -->

```console
$ immichpy albums add-users-to-album cccdd9f7-6a0f-4ed1-9dc0-ad8774ff9798 \
  --album-users '{"userId":"0025cccf-27ca-…","role":"viewer"}' \
  --album-users '{"userId":"033dda4c-5009-…","role":"viewer"}'
{
  "album_name": "2025'04 - April's Pictures",
  "album_users": [
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
  …
}
```

## Share an album with a link

Create a password-protected link with a custom name for people without an Immich account using [`shared-links create-shared-link`](reference.md#immichpy-shared-links-create-shared-link):

<!-- termynal -->

```console
$ immichpy shared-links create-shared-link --type ALBUM \
  --album-id 851c8f67-9bf3-48f5-8130-59da9ab17c06 --password s3cret --slug paris-2025
{
  "allow_download": true,
  "id": "3146a36e-abc2-447d-a890-3b26ab08e36f",
  "slug": "paris-2025",
  "type": "ALBUM",
  …
}
```

## Find an asset by its file path

Find an asset using [`search search-assets`](reference.md#immichpy-search-search-assets), where `--original-path` matches any part of the path:

<!-- termynal -->

```console
$ immichpy search search-assets --original-path 2025/09/IMG_9419.jpg | jq -r '.assets.items[].id'
16101f82-1407-4725-ba58-3ffb67a3ef7c
```

## Trigger library scan

Look up the library ID using [`libraries get-all-libraries`](reference.md#immichpy-libraries-get-all-libraries) and trigger a scan using [`libraries scan-library`](reference.md#immichpy-libraries-scan-library):

<!-- termynal -->

```console
$ immichpy libraries get-all-libraries
[
  {
    "id": "098adb6d-0a9b-494a-bd66-2ae6c0bf28ff",
    …
  }
]

$ immichpy libraries scan-library 098adb6d-0a9b-494a-bd66-2ae6c0bf28ff
```

## Show storage usage per user

Print the photos and storage per user using [`server get-server-statistics`](reference.md#immichpy-server-get-server-statistics):

<!-- termynal -->

```console
$ immichpy server get-server-statistics \
  | jq -r '.usage_by_user[] | "\(.user_name) \(.photos) photos \(.usage / 1e9 * 100 | round / 100) GB"'
Jane Doe 32566 photos 13.43 GB
Jason 26 photos 0.1 GB
Mich 8 photos 0.03 GB
```

## Use another profile

Run a command against another server or account with a profile:

<!-- termynal -->

```console
$ immichpy --profile john server get-about-info
{
  "version": "v2.4.1",
  …
}
```
