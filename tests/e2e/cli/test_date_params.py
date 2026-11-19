"""Test date and datetime params → values reach the server in a format it accepts.

The server requires datetimes with a timezone. The CLI reads naive input as local time,
the client serializes datetime query params as ISO 8601, and keyword-named params
like `for` reach the client under their generated name `var_for`.
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
        # datetime in a query param
        ["map", "get-map-markers", "--file-created-after", "2020-01-01T00:00:00+02:00"],
        # date in a keyword-named query param
        ["memories", "search-memories", "--for", "2020-01-01"],
    ],
    ids=["datetime-body", "datetime-query", "date-keyword-query"],
)
async def test_date_params(runner_with_api_key: CliRunner, args: list[str]) -> None:
    result = await asyncio.to_thread(runner_with_api_key.invoke, cli_app, args)

    assert result.exit_code == 0, result.stdout + result.stderr
