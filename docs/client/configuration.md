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

## Advanced usage

!!! warning "Only if you know what you're doing"
    Bypassing the high-level client is for **custom behaviour** (e.g. retries, SSL, proxy, server variables) that the high-level client does not expose. Use the advanced path only when you need full control over the generated client configuration.

!!! info "No support from maintainers"
    The high-level client is the recommended way to use the API. We will not provide support for custom configurations. For reference, you can inspect the implementation of the high-level client yourself.

Build your own [Configuration](../client/reference/configuration.md), create an [ApiClient](../client/reference/api_client.md), then instantiate only the API classes you need. You must call `api_client.close()` when done. To use a custom aiohttp session (connector, proxy, timeouts), set `api_client.rest_client.pool_manager` before making requests.

```python
from immichpy.client.generated.configuration import Configuration
from immichpy.client.generated.api_client import ApiClient
from immichpy.client.generated.api.server_api import ServerApi
from immichpy.client.wrapper.users_api_wrapped import UsersApiWrapped

config = Configuration(
    host="https://immich.example.com/api",
    retries=0,
    ssl_ca_cert=None,
    verify_ssl=True,
)
config.api_key["api_key"] = "your-api-key"

api_client = ApiClient(configuration=config)
api_client.user_agent = "immichpy"
server_api = ServerApi(api_client)
users_api = UsersApiWrapped(api_client)


async def main():
    info = await server_api.ping_server()
    me = await users_api.get_my_user()
    await api_client.close()
```
