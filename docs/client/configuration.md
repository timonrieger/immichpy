# Configuration

This section covers additional configuration of the client. For most usecases, the default configuration is sufficient and this section can be skipped.

## Session management

??? note "Session management is non-trivial"
    HTTP session handling comes with subtle lifecycle and event-loop constraints. For typical usage, you should not create or manage sessions yourself - let the client handle it.

    If you choose to pass a custom session, you take full responsibility for it. That includes:

    - Creating it in a running async context
    - Ensuring it is used only within the same event loop
    - Properly closing it to avoid connection leaks and warnings

    Incorrect session handling can lead to resource leaks, “attached to a different loop” errors, or unstable behavior. Only override the default if you clearly need advanced control (e.g., custom connectors, shared pooling, or transport tuning).

=== "Without context manager"

    ```python hl_lines="1 3 7 12"
    >>> from aiohttp import ClientSession
    >>> from immichpy import AsyncClient
    >>> custom_session = ClientSession()

    >>> client = AsyncClient(
          base_url="http://localhost:2283/api",
          http_client=custom_session,
          api_key="your-immich-api-key",
      )
    >>> await client.server.get_about_info()
    >>> await client.close()
    >>> await custom_session.close()
    ```

=== "Context manager"

    ```python hl_lines="1 3 7 11"
    >>> from aiohttp import ClientSession
    >>> from immichpy import AsyncClient
    >>> custom_session = ClientSession()

    >>> async with AsyncClient(
    ...     base_url="http://localhost:2283/api",
    ...     http_client=custom_session,
    ...     api_key="your-immich-api-key",
    ... ) as client:
    ...     await client.server.get_about_info()
    >>> await custom_session.close()
    ```

## Custom configuration

For custom behaviour (retries, SSL, proxy, etc.) pass a [Configuration](../client/reference/configuration.md) so it is the single source of truth. You get the same high-level client and lifecycle; `base_url`, `api_key`, and `access_token` are ignored when `configuration` is provided.

```python
from immichpy import AsyncClient
from immichpy.client.generated.configuration import Configuration

config = Configuration(
    host="https://immich.example.com/api",
    retries=0,
    verify_ssl=True,
)
config.api_key["api_key"] = "your-api-key"

client = AsyncClient(configuration=config)
# same client: client.server, client.users, async with client, client.close(), etc.
```
