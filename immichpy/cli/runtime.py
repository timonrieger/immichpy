"""Runtime helpers for executing async client calls and handling output."""

from __future__ import annotations

import asyncio
import json
import traceback
from typing import Any, Awaitable, Callable, Protocol, cast

from immichpy.cli.utils import print_
from pydantic import BaseModel
from typer import Context, Exit

from immichpy.cli.types import MaybeBaseModel

from immichpy.client.generated.api_client import ApiClient
from immichpy.client.generated.exceptions import ApiException


class _ApiGroup(Protocol):
    api_client: ApiClient


def set_nested(d: dict[str, Any], path: list[str], value: Any) -> None:
    """Set a nested dictionary value using a path list.

    Example: set_nested({}, ['user', 'name'], 'John') -> {'user': {'name': 'John'}}

    :param d: The dictionary to set the value in
    :param path: The path to the value
    :param value: The value to set
    :return: None
    :raises IndexError: If `path` is empty
    """
    current = d
    for part in path[:-1]:
        if part not in current:
            current[part] = {}
        elif not isinstance(current[part], dict):
            current[part] = {}
        current = current[part]
    current[path[-1]] = value


def print_response(data: MaybeBaseModel, ctx: Context) -> None:
    """Print response data.

    :param data: The data to print
    :param ctx: The context to use
    :return: None
    """

    def convert_to_dict(obj: MaybeBaseModel) -> Any:
        """Recursively convert Pydantic models to dictionaries.

        :param obj: The value to convert
        :return: A JSON-serializable value
        """
        if isinstance(obj, list):
            return [convert_to_dict(item) for item in obj]
        elif isinstance(obj, BaseModel):
            return obj.model_dump()
        else:
            return obj

    json_str = json.dumps(convert_to_dict(data), default=str)

    print_(message=json_str, type="json", ctx=ctx)


def format_api_error(e: ApiException) -> tuple[str, int]:
    """Convert an API exception into a CLI message and exit code.

    :param e: The API exception to convert
    :return: A tuple of error message and exit code
    """
    exit_code = 1 if e.status is None else e.status // 100

    if not e.body:
        return ("API error", exit_code)

    if isinstance(e.body, str):
        return (e.body, exit_code)

    return (json.dumps(e.body, default=str), exit_code)


async def run_async(coro: Awaitable[Any]) -> Any:
    """Await and return an awaitable.

    :param coro: The awaitable to run
    :return: The awaitable result
    :raises Exception: Propagates any exception raised by `coro`
    """
    return await coro


def run_command(
    method: Callable[..., Awaitable[Any]],
    *,
    ctx: Context | None = None,
    **kwargs: Any,
) -> Any:
    """Run a client API method and handle the result.

    :param method: Bound API method to invoke
    :param ctx: Optional Typer context for CLI output formatting
    :param kwargs: Keyword arguments forwarded to the API method
    :return: The API method return value
    :raises Exit: Raised with a CLI exit code when API or unexpected errors occur
    """

    async def _call_and_close() -> Any:
        try:
            return await method(**kwargs)
        finally:
            await cast(_ApiGroup, getattr(method, "__self__")).api_client.close()

    try:
        return asyncio.run(_call_and_close())

    except ApiException as e:
        message, code = format_api_error(e)
        print_(message, type="error", ctx=ctx)
        print_(traceback.format_exc(), type="debug", ctx=ctx)
        raise Exit(code=code)

    except Exception as e:
        print_(f"Unexpected error: {str(e).strip()}", type="error", ctx=ctx)
        print_(traceback.format_exc(), type="debug", ctx=ctx)
        raise Exit(code=1)
