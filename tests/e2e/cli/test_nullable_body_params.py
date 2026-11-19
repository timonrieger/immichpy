"""Test nullable body params → `--unset` sets the field to null on the server.

Example command tested: users-admin update-user-admin --unset quota-size-in-bytes
"""

import asyncio
import json

import pytest
from typer.testing import CliRunner

from immichpy.cli.main import app as cli_app
from immichpy.client.generated import UserAdminResponseDto


@pytest.mark.asyncio
async def test_unset_clears_nullable_field(
    runner_with_api_key: CliRunner, user: UserAdminResponseDto
) -> None:
    args = ["users-admin", "update-user-admin", str(user.id)]
    result = await asyncio.to_thread(
        runner_with_api_key.invoke, cli_app, [*args, "--quota-size-in-bytes", "1024"]
    )
    assert result.exit_code == 0, result.stdout + result.stderr
    assert json.loads(result.stdout)["quota_size_in_bytes"] == 1024

    result = await asyncio.to_thread(
        runner_with_api_key.invoke, cli_app, [*args, "--unset", "quota-size-in-bytes"]
    )
    assert result.exit_code == 0, result.stdout + result.stderr
    assert json.loads(result.stdout)["quota_size_in_bytes"] is None
