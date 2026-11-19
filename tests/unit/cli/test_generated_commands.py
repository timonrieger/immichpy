"""Contract tests over all generated CLI commands."""

from __future__ import annotations

from collections.abc import Iterator
from typing import Any

from typer.main import get_command

from immichpy.cli.main import app


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
