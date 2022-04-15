from typing import Optional
from pydantic import BaseModel, HttpUrl


class RequestConfiguration(BaseModel):
    element_name: str
    type: str
    attributes: list[str]
    base_address: Optional[str] = None


class RequestInputModel(BaseModel):
    url: HttpUrl
    parser_config: list[RequestConfiguration]


class RequestOutputModel(BaseModel):
    # TODO: need to work on output model for response
    test: str
