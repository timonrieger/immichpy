# Session management

The client manages a shared `aiohttp.ClientSession` by default, alternatively you can pass your own via `http_client=...`. In that case, you are responsible for its lifecycle, meaning you need to close it yourself when you are done with it.
