"""Contract tests over all generated CLI commands."""

from __future__ import annotations

import ast
import inspect
from collections.abc import Iterator
from pathlib import Path
from typing import Any, get_type_hints

import pytest
from typer.main import get_command

from immichpy import AsyncClient
from immichpy.cli import commands
from immichpy.cli.main import app

COMMAND_FILES = sorted(Path(next(iter(commands.__path__))).glob("*.py"))
CLIENT_APIS = get_type_hints(AsyncClient)


def _client_calls(path: Path) -> Iterator[tuple[str, str, set[str]]]:
    """Yield (api group, method, kwargs keys) for each `run_command(client.<group>.<method>, **kwargs)`."""
    for fn in ast.walk(ast.parse(path.read_text(encoding="utf-8"))):
        if not isinstance(fn, ast.FunctionDef):
            continue
        keys = {
            str(node.slice.value)
            for node in ast.walk(fn)
            if isinstance(node, ast.Subscript)
            and isinstance(node.value, ast.Name)
            and node.value.id == "kwargs"
            and isinstance(node.slice, ast.Constant)
        }
        for call in ast.walk(fn):
            if (
                isinstance(call, ast.Call)
                and isinstance(call.func, ast.Name)
                and call.func.id == "run_command"
            ):
                target = call.args[0]
                assert isinstance(target, ast.Attribute)
                assert isinstance(target.value, ast.Attribute)
                yield target.value.attr, target.attr, keys


@pytest.mark.parametrize("path", COMMAND_FILES, ids=lambda p: p.stem)
def test_command_kwargs_match_client_signature(path: Path) -> None:
    """Every kwarg a command passes exists on the client method it calls."""
    for group, method, keys in _client_calls(path):
        params = inspect.signature(getattr(CLIENT_APIS[group], method)).parameters
        assert keys <= params.keys(), f"{group}.{method}: {keys - params.keys()}"


def _params(command: Any) -> Iterator[tuple[str, Any]]:
    # Typer vendors click, so match groups and types structurally instead of with `isinstance`.
    for sub in getattr(command, "commands", {}).values():
        yield from _params(sub)
    for param in command.params:
        yield command.name, param


def test_no_option_uses_click_datetime() -> None:
    """Click's DateTime type rejects timezones and yields naive datetimes, which the server rejects."""
    params = list(_params(get_command(app)))
    offenders = [f"{name} {p.name}" for name, p in params if p.type.name == "datetime"]
    assert len(params) > 1000
    assert not offenders
