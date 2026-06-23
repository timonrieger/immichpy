"""Test command with optional query bool enum → String-to-bool conversion works.

This test verifies that optional boolean query parameters are correctly converted
from string literals ("true"/"false") to actual boolean values. The generated
CLI code uses Literal["true", "false"] | None for optional bool query params
and converts them using .lower() == 'true' before adding to kwargs.

Example command tested: get-all-albums with --shared "true"
"""

import asyncio
import json

import pytest
from typer.testing import CliRunner

from immichpy import AsyncClient
from immichpy.cli.main import app as cli_app
from immichpy.client.generated import (
    AlbumResponseDto,
    AlbumUserCreateDto,
    AlbumUserRole,
    CreateAlbumDto,
    UserResponseDto,
)


@pytest.mark.asyncio
async def test_get_all_albums_with_shared_filter(
    runner_with_api_key: CliRunner,
    user: UserResponseDto,
    client_with_api_key: AsyncClient,
) -> None:
    """Test get-all-albums command with shared filter and validate response structure."""
    album_users = [AlbumUserCreateDto(role=AlbumUserRole.VIEWER, userId=user.id)]
    album = await client_with_api_key.albums.create_album(
        CreateAlbumDto(albumName="Test Album", albumUsers=album_users)
    )
    result = await asyncio.to_thread(
        runner_with_api_key.invoke,
        cli_app,
        [
            "albums",
            "get-all-albums",
            "--is-shared",
            "true",
        ],
    )
    assert result.exit_code == 0, result.stdout + result.stderr
    response_data = json.loads(result.stdout)
    assert isinstance(response_data, list)
    albums: list[AlbumResponseDto] = []
    for item in response_data:
        albums.append(AlbumResponseDto.model_validate(item))
    assert any(a.id == album.id for a in albums)
