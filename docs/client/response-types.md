# Response Types

There are three different available output formats you can choose from:

## Serialized Response

You can get fully serialized responses as [Pydantic](https://docs.pydantic.dev/) models. Using this, you get the full benefits of Pydantic's type checking.

```python title="main.py"
res = await client.server.get_about_info()
```

The output would look like this:

<div class="termy">

```console
$ python main.py

ServerAboutResponseDto(
    build='20375083601',
    build_image='main',
    ...
    licensed=False,
    nodejs='v22.13.0',
    repository='immich-app/immich',
    ...
    version='v2.4.1',
    version_url='https://github.com/immich-app/immich/releases/tag/v2.4.1'
)
```

</div>

## Serialized Response with HTTP Info

Same as above, but with additional metadata about the HTTP response.

```python title="main.py"
res = await client.server.get_about_info_with_http_info()
```

<div class="termy">

```console
$ python main.py

ApiResponse(
    status_code=200,
    headers={'Content-Type': 'application/json'},
    data=ServerAboutResponseDto(
        build='20375083601',
        build_image='main',
        ...
        version='v2.4.1',
        version_url='https://github.com/immich-app/immich/releases/tag/v2.4.1'
    ),
    raw_data=b'{"build":"20375083601","buildImage":"main",...}'
)
```

</div>

## JSON Response

You can receive a classical JSON response by suffixing the function name with `_without_preload_content`:

```python title="main.py"
response = await client.server.get_about_info_without_preload_content()
await response.json()
```

<div class="termy">

```console
$ python main.py

{
    "build": "20375083601",
    "buildImage": "main",
    ...
    "version": "v2.4.1",
    "versionUrl": "https://github.com/immich-app/immich/releases/tag/v2.4.1"
}
```

</div>
