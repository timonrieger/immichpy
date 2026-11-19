"""Test date and datetime params → values reach the server in a format it accepts.

The server requires datetimes with a timezone. The CLI reads naive input as local time.
"""

import asyncio

import pytest
from typer.testing import CliRunner

from immichpy.cli.main import app as cli_app


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "args",
    [
        # datetime in a request body
        ["search", "search-asset-statistics", "--taken-after", "2020-01-01"],
    ],
    ids=["datetime-body"],
)
async def test_date_params(runner_with_api_key: CliRunner, args: list[str]) -> None:
    result = await asyncio.to_thread(runner_with_api_key.invoke, cli_app, args)

    assert result.exit_code == 0, result.stdout + result.stderr
