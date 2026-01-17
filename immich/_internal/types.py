from typing import Optional, Union

from pydantic import BaseModel

_MaybeBaseModel = Optional[Union[BaseModel, list[BaseModel]]]
