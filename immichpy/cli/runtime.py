"""Runtime helpers for executing async client calls and handling output."""

from __future__ import annotations

import asyncio
import json
import keyword
import sys
import traceback
from collections.abc import Awaitable, Callable
from datetime import datetime
from typing import TYPE_CHECKING, Any, Protocol, TypeVar, cast

from pydantic import BaseModel
from typer import Context, Exit

from immichpy.cli.types import MaybeBaseModel
from immichpy.cli.utils import print_
from immichpy.client.generated.exceptions import ApiException

if TYPE_CHECKING:
    from immichpy.client.generated.api_client import ApiClient


class _ApiGroup(Protocol):
    api_client: ApiClient


ModelT = TypeVar("ModelT", bound=BaseModel)


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
        if part not in current or not isinstance(current[part], dict):
            current[part] = {}
        current = current[part]
    current[path[-1]] = value


def validate_body(model: type[ModelT], data: Any) -> ModelT:
    """Validate a request body built from CLI options, rejecting unknown keys.

    The generated models ignore unknown keys so that responses stay forward
    compatible, which would silently drop a mis-built CLI body instead.

    :param model: The request body model to validate against
    :param data: The request body data
    :return: The validated model instance
    :raises pydantic.ValidationError: If `data` has keys the model does not define
    """
    return model.model_validate(data, extra="forbid")


def parse_datetime(value: str) -> datetime:
    """Parse an ISO 8601 datetime option value.

    The server rejects datetimes without a timezone, so naive input is read as local time.

    :param value: The raw option string, e.g. `2024-01-01` or `2024-01-01T00:00:00Z`
    :return: The timezone-aware datetime
    :raises ValueError: If `value` is not a valid ISO 8601 datetime
    """
    dt = datetime.fromisoformat(value)
    return dt if dt.tzinfo else dt.astimezone()


def parse_json_option(value: str, option: str, *, ctx: Context | None = None) -> Any:
    """Parse a single JSON option value, exiting cleanly on invalid JSON.

    :param value: The raw option string to parse
    :param option: The option flag name, used in the error message
    :param ctx: Optional Typer context for CLI output formatting
    :return: The parsed JSON value
    :raises Exit: Raised with exit code 1 when the value is not valid JSON
    """
    try:
        return json.loads(value)
    except json.JSONDecodeError as e:
        print_(f"Invalid JSON in {option}: {e}", type="error", ctx=ctx)
        print_(traceback.format_exc(), type="debug", ctx=ctx)
        raise Exit(code=1)


def parse_json_options(
    values: list[str], option: str, *, ctx: Context | None = None
) -> list[Any]:
    """Parse a list of JSON option values, exiting cleanly on invalid JSON.

    :param values: The raw option strings to parse
    :param option: The option flag name, used in the error message
    :param ctx: Optional Typer context for CLI output formatting
    :return: The parsed JSON values
    :raises Exit: Raised with exit code 1 when any value is not valid JSON
    """
    return [parse_json_option(value, option, ctx=ctx) for value in values]


def restore_keyword_keys(obj: Any) -> Any:
    """Rename fields the generated models prefix with `var_`, like `var_from`, back to their API name.

    :param obj: A dumped model, possibly nested
    :return: The same data with keyword field names restored
    """
    if isinstance(obj, list):
        return [restore_keyword_keys(item) for item in obj]
    if isinstance(obj, dict):
        return {
            (
                key.removeprefix("var_")
                if keyword.iskeyword(key.removeprefix("var_"))
                else key
            ): restore_keyword_keys(value)
            for key, value in obj.items()
        }
    return obj


def print_response(data: MaybeBaseModel, ctx: Context) -> None:
    """Print response data. Binary data is written raw, so it can be redirected to a file.

    :param data: The data to print
    :param ctx: The context to use
    :return: None
    """
    if isinstance(data, bytes):
        sys.stdout.buffer.write(data)
        return

    def convert_to_dict(obj: MaybeBaseModel) -> Any:
        """Recursively convert Pydantic models to dictionaries.

        :param obj: The value to convert
        :return: A JSON-serializable value
        """
        if isinstance(obj, list):
            return [convert_to_dict(item) for item in obj]
        elif isinstance(obj, BaseModel):
            return restore_keyword_keys(obj.model_dump(mode="json"))
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
            self_ = getattr(method, "__self__", None)
            if self_ is not None:
                await cast(_ApiGroup, self_).api_client.close()

    try:
        return asyncio.run(_call_and_close())

    except ApiException as e:
        message, code = format_api_error(e)
        print_(message, type="error", ctx=ctx)
        print_(traceback.format_exc(), type="debug", ctx=ctx)
        raise Exit(code=code)

    except Exception as e:  # noqa: BLE001 - CLI top-level error boundary
        print_(f"Unexpected error: {str(e).strip()}", type="error", ctx=ctx)
        print_(traceback.format_exc(), type="debug", ctx=ctx)
        raise Exit(code=1)
