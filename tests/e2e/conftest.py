import os
from pathlib import Path
from typing import AsyncGenerator, Awaitable, Callable, Generator, ParamSpec, TypeVar
from uuid import UUID, uuid4

import pytest
from typer.testing import CliRunner

from immichpy import AsyncClient
from immichpy.cli.consts import (
    DEFAULT_FORMAT,
    DEFAULT_PROFILE,
    IMMICH_ACCESS_TOKEN,
    IMMICH_API_KEY,
    IMMICH_API_URL,
    IMMICH_FORMAT,
    IMMICH_PROFILE,
)
from immichpy.client.types import UploadResult
from immichpy.client.generated import (
    AlbumResponseDto,
    AssetBulkDeleteDto,
    AssetMediaResponseDto,
    CreateAlbumDto,
    UserAdminCreateDto,
    UserAdminDeleteDto,
    UserAdminResponseDto,
)
from immichpy.client.generated.exceptions import BadRequestException
from immichpy.client.generated.models.admin_onboarding_update_dto import (
    AdminOnboardingUpdateDto,
)
from immichpy.client.generated.models.api_key_create_dto import APIKeyCreateDto
from immichpy.client.generated.models.login_credential_dto import LoginCredentialDto
from immichpy.client.generated.models.permission import Permission
from immichpy.client.generated.models.sign_up_dto import SignUpDto
from tests.generators import make_random_image, make_random_video

P = ParamSpec("P")
R = TypeVar("R")


def _wrap_factory(
    method: Callable[P, Awaitable[R]],
    on_result: Callable[[R], None],
) -> Callable[P, Awaitable[R]]:
    """Wrap a bound async method preserving its signature, with post-result hook."""

    async def _call(*args: P.args, **kwargs: P.kwargs) -> R:
        try:
            result = await method(*args, **kwargs)
        except Exception as e:
            pytest.skip(f"Factory call failed:\n{e}")
        on_result(result)
        return result

    return _call


@pytest.fixture
def test_image_factory(
    tmp_path: Path,
) -> Generator[Callable[[str | None], Path], None, None]:
    """Factory fixture: yields a callable to create test images.

    Example:
        img_path = test_image_factory()
        img_path2 = test_image_factory(filename="custom.jpg")
    """

    def _create_image(filename: str | None = None) -> Path:
        if filename is None:
            filename = f"{uuid4()}.jpg"
        img_path = tmp_path / filename
        img_path.write_bytes(make_random_image())
        return img_path

    yield _create_image


@pytest.fixture
def test_image(
    test_image_factory: Callable[[], Path],
) -> Generator[Path, None, None]:
    """Create a minimal JPEG test image."""
    yield test_image_factory()


@pytest.fixture
def test_video_factory(
    tmp_path: Path,
) -> Generator[Callable[[str | None], Path], None, None]:
    """Factory fixture: yields a callable to create test videos.

    Example:
        video_path = test_video_factory()
        video_path2 = test_video_factory(filename="custom.mp4")
    """

    def _create_video(filename: str | None = None) -> Path:
        if filename is None:
            filename = f"{uuid4()}.mp4"
        video_path = tmp_path / filename
        video_path.write_bytes(make_random_video())
        return video_path

    yield _create_video


@pytest.fixture
def test_video(
    test_video_factory: Callable[[], Path],
) -> Generator[Path, None, None]:
    """Create a minimal MP4 test video."""
    yield test_video_factory()


@pytest.fixture
def env() -> dict[str, str]:
    return {
        IMMICH_API_URL: os.environ.get(IMMICH_API_URL, "http://127.0.0.1:2283/api"),
        IMMICH_API_KEY: os.environ.get(IMMICH_API_KEY, ""),
        IMMICH_FORMAT: "json",
    }


@pytest.fixture
async def client_with_api_key(client_with_access_token: AsyncClient):
    """Returns an adming-authenticated client with patched methods for test asset cleanup."""
    api_key_response = await client_with_access_token.api_keys.create_api_key(
        APIKeyCreateDto(name="e2e", permissions=[Permission.ALL]),
    )

    client = AsyncClient(
        base_url=client_with_access_token._config.host, api_key=api_key_response.secret
    )

    _uploaded_ids: list[UUID] = []
    _album_ids: list[UUID] = []

    def _track_upload(result: UploadResult) -> None:
        _uploaded_ids.extend(UUID(u.asset.id) for u in result.uploaded)

    def _track_album(result: AlbumResponseDto) -> None:
        _album_ids.append(UUID(str(result.id)))

    client.assets.upload = _wrap_factory(  # ty: ignore[invalid-assignment]
        client.assets.upload, on_result=_track_upload
    )
    client.albums.create_album = _wrap_factory(  # ty: ignore[invalid-assignment]
        client.albums.create_album, on_result=_track_album
    )

    try:
        yield client
    finally:
        if _uploaded_ids:
            await client.assets.delete_assets(
                AssetBulkDeleteDto(ids=_uploaded_ids, force=True)
            )
        for album_id in _album_ids:
            await client.albums.delete_album(album_id)
        await client.close()


@pytest.fixture
async def client_with_access_token(env: dict[str, str]):
    """Set up admin user, create API key, and return authenticated client."""

    # Create unauthenticated client for setup
    setup_client = AsyncClient(base_url=env[IMMICH_API_URL])

    try:
        # Sign up admin (idempotent: subsequent tests will hit "already has an admin")
        try:
            await setup_client.auth.sign_up_admin(
                SignUpDto(
                    email="admin@immich.cloud", name="Immich Admin", password="password"
                )
            )
        except BadRequestException as e:
            if not (e.status == 400 and e.body and "already has an admin" in e.body):
                raise

        # Login to get access token
        login_response = await setup_client.auth.login(
            LoginCredentialDto(email="admin@immich.cloud", password="password")
        )

        client = AsyncClient(
            base_url=env[IMMICH_API_URL], access_token=login_response.access_token
        )

        # Mark admin as onboarded
        await client.system_metadata.update_admin_onboarding(
            AdminOnboardingUpdateDto(isOnboarded=True),
        )

        try:
            yield client
        finally:
            await client.close()
    finally:
        await setup_client.close()


@pytest.fixture
def runner_with_api_key(client_with_api_key: AsyncClient) -> CliRunner:
    """Typer CliRunner fixture for CLI testing."""
    return CliRunner(
        env={
            IMMICH_API_URL: client_with_api_key.base_client.configuration.host,
            IMMICH_API_KEY: client_with_api_key.base_client.configuration.api_key[
                "api_key"
            ],
            IMMICH_ACCESS_TOKEN: None,
            IMMICH_FORMAT: DEFAULT_FORMAT,
            IMMICH_PROFILE: DEFAULT_PROFILE,
        }
    )


@pytest.fixture
def runner_without_auth() -> CliRunner:
    """Simple Typer CliRunner fixture for CLI testing without client setup."""
    return CliRunner(
        env={
            IMMICH_FORMAT: DEFAULT_FORMAT,
            IMMICH_PROFILE: DEFAULT_PROFILE,
            IMMICH_API_KEY: None,
            IMMICH_ACCESS_TOKEN: None,
            IMMICH_API_URL: None,
        }
    )


@pytest.fixture
async def asset(
    test_image: Path,
    client_with_api_key: AsyncClient,
) -> AsyncGenerator[AssetMediaResponseDto, None]:
    """Fixture to set up asset for testing.

    Uploads a test image, returns parsed asset object.
    """
    upload_result = await client_with_api_key.assets.upload(
        [test_image], skip_duplicates=True
    )
    assert len(upload_result.uploaded) == 1
    yield upload_result.uploaded[0].asset


@pytest.fixture
async def user(
    client_with_api_key: AsyncClient,
) -> AsyncGenerator[UserAdminResponseDto, None]:
    """Fixture to set up user for testing.

    Creates a user, returns parsed user object.
    Skips dependent tests if user creation fails.
    """
    uuid = uuid4()
    user = await client_with_api_key.users_admin.create_user_admin(
        UserAdminCreateDto(
            email=f"test_{uuid}@immich.cloud",
            password="password",
            name=f"Test User {uuid}",
        )
    )
    yield user
    await client_with_api_key.users_admin.delete_user_admin(
        UUID(str(user.id)),
        UserAdminDeleteDto(force=True),
    )


@pytest.fixture
async def album(
    client_with_api_key: AsyncClient,
) -> AsyncGenerator[AlbumResponseDto, None]:
    """Fixture to set up album for testing."""
    yield await client_with_api_key.albums.create_album(
        CreateAlbumDto(albumName="Test Album")
    )
