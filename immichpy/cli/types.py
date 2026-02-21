from typing import Literal

from pydantic import BaseModel

MaybeBaseModel = BaseModel | list[BaseModel] | str | None
FormatMode = Literal["pretty", "json", "table"]
PrintType = Literal["info", "warning", "error", "debug", "success", "json", "text"]


class ClientConfig(BaseModel):
    """
    A configuration for a client to connect to an Immich server.
    """

    base_url: str | None
    api_key: str | None
    access_token: str | None
