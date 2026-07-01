"""Tests for immichpy.cli.runtime module."""

from __future__ import annotations

import asyncio
import json
from typing import TYPE_CHECKING, Any, cast
from unittest.mock import AsyncMock, MagicMock, Mock, patch

import pytest
from pydantic import BaseModel
from typer import Context, Exit

if TYPE_CHECKING:
    from _pytest.capture import CaptureFixture

from immichpy.cli.runtime import (
    set_nested,
    parse_json_option,
    parse_json_options,
    print_response,
    format_api_error,
    run_async,
    run_command,
)
from immichpy.client.generated.exceptions import ApiException


class TestSetNested:
    """Tests for set_nested function."""

    def test_set_nested_nested_levels(self) -> None:
        """Test setting nested values and overwriting non-dict values."""
        d: dict[str, Any] = {}
        set_nested(d, ["user", "name"], "John")
        assert d == {"user": {"name": "John"}}

        # Test overwriting non-dict value
        d = {"user": "not-a-dict"}
        set_nested(d, ["user", "name"], "John")
        assert d == {"user": {"name": "John"}}


class TestParseJsonOption:
    """Tests for parse_json_option function."""

    def test_parse_json_option_valid(self) -> None:
        """Valid JSON object is parsed into a dict."""
        assert parse_json_option('{"role": "viewer"}', "--data") == {"role": "viewer"}

    @patch("immichpy.cli.runtime.print_")
    def test_parse_json_option_invalid_exits(self, mock_print: Mock) -> None:
        """Invalid JSON prints a clean error naming the option and exits 1."""
        with pytest.raises(Exit) as exc_info:
            parse_json_option('{"role": "viewer}', "--data")

        assert exc_info.value.exit_code == 1
        error_calls = [
            call
            for call in mock_print.call_args_list
            if call.kwargs.get("type") == "error"
        ]
        assert error_calls
        assert "--data" in error_calls[0].args[0]


class TestParseJsonOptions:
    """Tests for parse_json_options function."""

    def test_parse_json_options_valid(self) -> None:
        """Each valid JSON string is parsed into the returned list."""
        assert parse_json_options(['{"a": 1}', '{"b": 2}'], "--assets") == [
            {"a": 1},
            {"b": 2},
        ]

    @patch("immichpy.cli.runtime.print_")
    def test_parse_json_options_invalid_element_exits(self, mock_print: Mock) -> None:
        """A single invalid element prints a clean error and exits 1."""
        with pytest.raises(Exit) as exc_info:
            parse_json_options(['{"a": 1}', "not json"], "--assets")

        assert exc_info.value.exit_code == 1
        error_calls = [
            call
            for call in mock_print.call_args_list
            if call.kwargs.get("type") == "error"
        ]
        assert error_calls
        assert "--assets" in error_calls[0].args[0]


class TestPrintResponse:
    """Tests for print_response function."""

    def test_print_response_base_model_json(
        self, capsys: "CaptureFixture[str]"
    ) -> None:
        """Test print_response with BaseModel and json format."""
        ctx: Mock = Mock(spec=Context)
        ctx.obj = {"format": "json"}

        class TestModel(BaseModel):
            name: str
            age: int

        data = TestModel(name="John", age=30)
        print_response(data, ctx=ctx)

        captured = capsys.readouterr()
        output = json.loads(captured.out)
        assert output["name"] == "John"
        assert output["age"] == 30

    def test_print_response_list_pretty(self, capsys: "CaptureFixture[str]") -> None:
        """Test print_response with list and pretty format."""
        ctx: Mock = Mock(spec=Context)
        ctx.obj = {"format": "pretty"}

        class TestModel(BaseModel):
            name: str

        data = cast(list[BaseModel], [TestModel(name="John"), TestModel(name="Jane")])
        print_response(data, ctx=ctx)

        captured = capsys.readouterr()
        assert "John" in captured.out
        assert "Jane" in captured.out

    def test_print_response_primitive_type(self, capsys: "CaptureFixture[str]") -> None:
        """Test print_response with primitive type (neither list nor BaseModel)."""
        ctx: Mock = Mock(spec=Context)
        ctx.obj = {"format": "json"}

        data = "simple string"
        print_response(data, ctx=ctx)

        captured = capsys.readouterr()
        output = json.loads(captured.out)
        assert output == "simple string"


class TestFormatApiError:
    """Tests for format_api_error function."""

    def test_format_api_error_no_body(self) -> None:
        """Test format_api_error with no body (with and without status)."""
        e: ApiException = ApiException(status=404)
        e.body = None

        message, code = format_api_error(e)
        assert message == "API error"
        assert code == 4

        # Test with no status
        e = ApiException(status=None)
        e.body = None

        message, code = format_api_error(e)
        assert message == "API error"
        assert code == 1

    def test_format_api_error_string_body(self) -> None:
        """Test format_api_error with string body."""
        e: ApiException = ApiException(status=400)
        e.body = '{"error": "test"}'

        message, code = format_api_error(e)
        assert message == '{"error": "test"}'
        assert code == 4

    def test_format_api_error_dict_body(self) -> None:
        """Test format_api_error with dict body (converts to JSON)."""
        e: ApiException = ApiException(status=500)
        e.body = {"error": "test", "code": 500}

        message, code = format_api_error(e)
        parsed = json.loads(message)
        assert parsed == {"error": "test", "code": 500}
        assert code == 5


class TestRunAsync:
    """Tests for run_async function."""

    async def test_run_async_success(self) -> None:
        """Test run_async with simple coroutine."""

        async def simple_coro() -> int:
            return 42

        result: int = await run_async(simple_coro())
        assert result == 42

    async def test_run_async_with_exception(self) -> None:
        """Test run_async with coroutine that raises exception."""

        async def failing_coro() -> None:
            raise ValueError("test error")

        with pytest.raises(ValueError, match="test error"):
            await run_async(failing_coro())


def _make_bound_method(return_value: Any = None, side_effect: Any = None) -> AsyncMock:
    """Create an AsyncMock that looks like a bound method with an api_client."""
    mock_api_client: MagicMock = MagicMock()
    mock_api_client.close = AsyncMock()
    mock_api_group: MagicMock = MagicMock()
    mock_api_group.api_client = mock_api_client
    method: AsyncMock = AsyncMock(return_value=return_value, side_effect=side_effect)
    method.__self__ = mock_api_group
    return method


class TestRunCommand:
    """Tests for run_command function."""

    @patch("immichpy.cli.runtime.asyncio.run")
    def test_run_command_success(self, mock_asyncio_run: Mock) -> None:
        """Test run_command with successful execution."""
        method = _make_bound_method(return_value={"result": "success"})

        def mock_run(coro: Any) -> Any:
            loop = asyncio.new_event_loop()
            try:
                return loop.run_until_complete(coro)
            finally:
                loop.close()

        mock_asyncio_run.side_effect = mock_run

        result: dict[str, str] = run_command(method, ctx=None, arg1="value1")

        assert result == {"result": "success"}
        mock_asyncio_run.assert_called_once()
        method.__self__.api_client.close.assert_awaited_once()

    @patch("immichpy.cli.runtime.print_")
    @patch("immichpy.cli.runtime.format_api_error")
    @patch("immichpy.cli.runtime.asyncio.run")
    def test_run_command_api_exception(
        self, mock_asyncio_run: Mock, mock_format_error: Mock, mock_print: Mock
    ) -> None:
        """Test run_command with ApiException."""
        api_error: ApiException = ApiException(status=404)
        api_error.body = {"error": "not found"}
        method = _make_bound_method(side_effect=api_error)

        def mock_run(coro: Any) -> Any:
            loop = asyncio.new_event_loop()
            try:
                return loop.run_until_complete(coro)
            finally:
                loop.close()

        mock_asyncio_run.side_effect = mock_run
        mock_format_error.return_value = ("not found", 4)

        ctx: Mock = Mock(spec=Context)
        ctx.obj = {"format": "json"}

        with pytest.raises(Exit) as exc_info:
            run_command(method, ctx=ctx)

        assert exc_info.value.exit_code == 4
        mock_format_error.assert_called_once_with(api_error)
        mock_print.assert_any_call("not found", type="error", ctx=ctx)

    @patch("immichpy.cli.runtime.print_")
    @patch("immichpy.cli.runtime.asyncio.run")
    def test_run_command_other_exception(
        self, mock_asyncio_run: Mock, mock_print: Mock
    ) -> None:
        """Test run_command with non-ApiException."""
        method = _make_bound_method(side_effect=ValueError("test error"))

        def mock_run(coro: Any) -> Any:
            loop = asyncio.new_event_loop()
            try:
                return loop.run_until_complete(coro)
            finally:
                loop.close()

        mock_asyncio_run.side_effect = mock_run

        with pytest.raises(Exit) as exc_info:
            run_command(method, ctx=None)

        assert exc_info.value.exit_code == 1
        mock_print.assert_any_call(
            "Unexpected error: test error", type="error", ctx=None
        )
        mock_asyncio_run.assert_called_once()
        method.__self__.api_client.close.assert_awaited_once()
