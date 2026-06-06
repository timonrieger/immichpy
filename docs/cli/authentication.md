# Authentication

The CLI supports three ways to provide credentials, applied in this priority order (highest first):

1. **Command-line flags**: `--api-key`, `--base-url`, etc. passed directly to each command.
2. **Environment variables**: useful for CI/CD or scripting without a profile.
3. **Profile**: stored credentials from `immichpy setup`, used by default when nothing else is set.

## Profiles

Run `immichpy setup` to create a named profile. The `default` profile is used automatically; pass `--profile <name>` to switch.

See [Getting Started](getting-started.md#create-a-profile) for a walkthrough.

## Environment Variables

| Variable | Description | Equivalent flag |
|---|---|---|
| `IMMICH_API_URL` | Server URL | `--base-url` |
| `IMMICH_API_KEY` | API key | `--api-key` |
| `IMMICH_ACCESS_TOKEN` | Access token | `--access-token` |
| `IMMICH_PROFILE` | Profile name | `--profile` |
| `IMMICH_FORMAT` | Output format (`pretty`, `json`, `table`) | `--format` |

See the [CLI Reference](./reference.md) for full details on each flag.
