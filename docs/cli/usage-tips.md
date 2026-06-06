# Usage Tips

Practical notes on CLI behaviour that isn't obvious from `--help` alone.

- **Required boolean flags** (e.g. `--dry-run`) are simple toggles: present = true, absent = false.
- **Optional boolean flags** (e.g. `--shared`) accept `true` or `false` as a string value, or can be omitted entirely. Omission sends no value and lets the server apply its default — passing `false` explicitly is different from omitting the flag.
- **JSON flags** (e.g. `--album-users`) expect a valid JSON object string — the value is validated but there is no autocompletion. Run `--help` on the command to see the expected keys.
- Flags that map to an array field can be repeated to pass multiple values (e.g. `--album-users '...' --album-users '...'`). See the [share album example](examples.md#share-an-album-with-multiple-users).
- Every command's `--help` includes a link to the corresponding Immich API documentation page.
