from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from immichpy.client.main import AsyncClient

__all__ = ["AsyncClient"]


def __getattr__(name: str) -> object:
    if name != "AsyncClient":
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
    from immichpy.client.main import AsyncClient

    return AsyncClient
