# Examples

This page contains practical examples of using the immichpy CLI for common tasks.
> Have an example? You’re welcome to suggest it on [GitHub issues](https://github.com/timonrieger/immichpy/issues).

## List all albums and parse with jq

Get all albums and their name and ID:

<!-- termynal -->

```console
$ immichpy albums get-all-albums | jq -r '.[] | "\(.album_name) \(.id)"'
Animal Portraits ff09c49f-525d-4216-bc5a-8ff070bca149
Vacation 2023 851c8f67-9bf3-48f5-8130-59da9ab17c06
Selfies c980670b-69d1-42ee-b4a5-86947f169d99
```

## Download an album archive

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

## Upload assets

Upload assets to your Immich server. Use `--dry-run` to preview what would be uploaded:

<!-- termynal -->

```console
$ immichpy assets upload ~/timelapse.mp4 --dry-run
{
  "uploaded": [
    {
      "asset": {
        "id": "ba199326-210b-492c-b5cb-4fc54e00f032",
        "status": "created"
      },
      "filepath": "~/timelapse.mp4"
    }
  ],
  "rejected": [],
  "failed": [],
  "stats": {
    "total": 1,
    "uploaded": 1,
    "rejected": 0,
    "failed": 0
  }
}
```

## List all people with names

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

## List all users

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

## Share an album with multiple users

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

## Trigger library scan

Trigger an external library scan by using it's ID:

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

Success!
```

## Upload a folder into an album

Upload a whole folder and add the assets to an album, creating it if it does not exist:

<!-- termynal -->

```console
$ immichpy assets upload /Volumes/SD/DCIM/101NIKON/ --album-name "Paris 2025" --show-progress

---> 100%
```

## Find an asset by its file path

Look up an asset ID by the path it has on the server:

<!-- termynal -->

```console
$ immichpy search search-assets --original-path library/family/2025/09/IMG_9419.jpg \
  | jq -r '.assets.items[0].id'
16101f82-1407-4725-ba58-3ffb67a3ef7c
```

## Read an asset's EXIF data

Get the EXIF data of an asset and extract a single field:

<!-- termynal -->

```console
$ immichpy assets get-asset-info 16101f82-1407-4725-ba58-3ffb67a3ef7c | jq -r '.exif_info.description'
OLYMPUS DIGITAL CAMERA
```

## Count and page through search results

Count the assets matching a filter, then fetch them page by page:

<!-- termynal -->

```console
$ immichpy search search-asset-statistics --make OLYMPUS
{
  "total": 1342
}

$ immichpy search search-assets --make OLYMPUS --page 2 --size 10 | jq '.assets.next_page'
"3"
```

## Delete assets listed in a file

Delete every asset whose server path is listed in `files.txt`, one path per line. Run it with `echo` in front of `immichpy assets delete-assets` first to preview what would be deleted:

```bash
while read -r path; do
  id=$(immichpy search search-assets --original-path "$path" | jq -r '.assets.items[0].id')
  if [ "$id" != null ]; then
    immichpy assets delete-assets --ids "$id" && echo "Deleted $id $path"
  else
    echo "Not found: $path"
  fi
done < files.txt
```

## Run a command against several profiles

Select a profile per command with `--profile` (`-p`) or the `IMMICH_PROFILE` environment variable, or loop over profiles to apply the same change to several accounts:

<!-- termynal -->

```console
$ IMMICH_PROFILE=family immichpy server get-about-info

$ for p in alice bob; do immichpy -p $p albums get-all-albums | jq length; done
12
4
```

## Rotate an API key

Rotate an API key and store the new secret in your profile. The secret is only shown once:

<!-- termynal -->

```console
$ immichpy config set profiles.default.api_key \
  --value "$(immichpy api-keys rotate-api-key 016601fa-3462-4299-8f73-84555c8043a4 | jq -r '.secret')"
```
