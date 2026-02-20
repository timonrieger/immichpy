import pytest

from immichpy import AsyncClient
from immichpy.client.generated.api.assets_api import AssetsApi
from immichpy.client.generated.api.users_api import UsersApi
from immichpy.client.generated.configuration import Configuration


@pytest.mark.asyncio
async def test_client_requires_base_url():
    with pytest.raises(TypeError):
        AsyncClient()  # type: ignore[call-arg]


@pytest.mark.asyncio
async def test_client_exposes_api_groups():
    async with AsyncClient(base_url="http://localhost:2283/api") as client:
        assert isinstance(client.assets, AssetsApi)
        assert isinstance(client.users, UsersApi)


@pytest.mark.asyncio
async def test_client_passes_parameters():
    async with AsyncClient(
        base_url="http://localhost:2283/api", api_key="test", access_token="test"
    ) as client:
        assert client.base_client.configuration.host == "http://localhost:2283/api"
        assert client.base_client.configuration.api_key == {"api_key": "test"}
        assert client.base_client.configuration.access_token == "test"


@pytest.mark.asyncio
async def test_client_normalizes_base_url():
    async with AsyncClient(base_url="http://localhost:2283/api/") as client:
        assert client.base_client.configuration.host == "http://localhost:2283/api"


@pytest.mark.asyncio
async def test_client_uses_configuration_when_provided():
    config = Configuration(host="https://custom.example.com/api", retries=0)
    config.api_key["api_key"] = "custom-key"
    async with AsyncClient(configuration=config) as client:
        assert client._config is config
        assert client.base_client.configuration.host == "https://custom.example.com/api"
        assert client.base_client.configuration.api_key == {"api_key": "custom-key"}
