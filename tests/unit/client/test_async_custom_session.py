import pytest
from aiohttp import ClientSession
from immich import AsyncClient


@pytest.mark.asyncio
async def test_client_owned_session_closed():
    # Client creates its own session → should be closed on exit
    async with AsyncClient(base_url="http://localhost:2283/api") as client:
        session = client.base_client.rest_client.pool_manager
        assert session is not None
        assert not session.closed

    # After context: pool_manager detached
    assert client.base_client.rest_client.pool_manager is None
    # Session object still valid → closed
    assert session.closed


@pytest.mark.asyncio
async def test_injected_session_not_closed_on_close():
    # User injects a session → should not be closed by client
    session = ClientSession()
    client = AsyncClient(base_url="http://localhost:2283/api", http_client=session)

    await client.close()
    assert client.base_client.rest_client.pool_manager is None
    assert not session.closed  # ownership respected

    await session.close()  # user cleans up
    assert session.closed


@pytest.mark.asyncio
async def test_injected_session_context_manager():
    session = ClientSession()

    async with AsyncClient(base_url="http://localhost:2283/api", http_client=session):
        # inside context, session exists
        inner_session = session
        assert inner_session is not None
        assert not inner_session.closed

    # After context, pool_manager detached
    assert inner_session is session
    assert not inner_session.closed
    await session.close()


@pytest.mark.asyncio
async def test_close_is_idempotent():
    # Ensure multiple closes do not raise, client-owned session
    async with AsyncClient(base_url="http://localhost:2283/api") as client:
        session = client.base_client.rest_client.pool_manager

    # session detached from client
    assert client.base_client.rest_client.pool_manager is None
    assert session.closed

    # Should not raise
    await client.close()


@pytest.mark.asyncio
async def test_reuse_injected_session():
    # Injected session can be reused across multiple clients
    session = ClientSession()

    async with AsyncClient(base_url="http://localhost:2283/api", http_client=session):
        inner_session1 = session
        assert not inner_session1.closed

    async with AsyncClient(base_url="http://localhost:2283/api", http_client=session):
        inner_session2 = session
        assert not inner_session2.closed

    # Session is still alive
    assert inner_session1 is inner_session2
    assert not session.closed

    await session.close()
    assert session.closed
