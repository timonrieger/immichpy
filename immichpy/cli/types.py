from typing import Literal

from pydantic import BaseModel

MaybeBaseModel = BaseModel | list[BaseModel] | str | None
"""A type that represents a Pydantic model, a list of Pydantic models, or a string."""
FormatMode = Literal["pretty", "json", "table"]
"""A type that represents a format mode for the CLI."""
PrintType = Literal["info", "warning", "error", "debug", "success", "json", "text"]
"""A type that represents a print type for the CLI."""


class ClientConfig(BaseModel):
    """
    A configuration for a client to connect to an Immich server.
    """

    base_url: str | None
    api_key: str | None
    access_token: str | None
