## Getting Started with Immich CLI Authentication

**Step 1: Set up your Immich server**
- Have your Immich server running or use the demo server at
- Get an API key from your Immich account settings: https://my.immich.app/user-settings?isOpen=api-keys

**Step 2: Create a profile (recommended)**
- Run `immich setup` and follow the prompts:
  - Enter your server URL
  - Enter your API key (hidden for security)
- This saves a "profile" (a named configuration) so you don't need to enter these each time
- You can create multiple profiles for different servers using `--profile <name>`, e.g. `immich --profile demo` for the demo server

**Step 3: Alternative — use environment variables**
- Instead of profiles, you can set:
  - `IMMICH_API_URL` — your server URL
  - `IMMICH_API_KEY` — your API key
  - `IMMICH_ACCESS_TOKEN` — or use an access token instead
- Environment variables override profile settings if both are set

**Step 4: Use the CLI**
- Run commands like `immich assets list` or `immich albums list`
- The CLI uses the default profile `default` automatically
- To use a different profile: `immich --profile <name> <command>`
- To override temporarily: `immich --base-url <url> --api-key <key> <command>`

**Priority order (highest to lowest):**
1. Command-line flags (`--api-key`, `--base-url`)
2. Environment variables
3. Profile settings (from `immich setup`)

This lets you switch between servers or override settings when needed. If you are unsure which configuration is used, run `immich --verbose <command>` to see the configuration in use.

## Boolean Options

- Flags like --verbose, --dry-run are simple toggles: present = true, absent = false.
- Optional flags like --albums let you pass true, false, or omit them — omission lets the server apply its default.

Use "true"/"false" only when the option is optional; required toggles work like normal CLI flags.

Make flags opt-in by default unless it’s universally expected behavior.