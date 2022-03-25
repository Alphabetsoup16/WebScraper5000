from typing import Optional
from pydantic import BaseModel, HttpUrl


class RequestConfiguration(BaseModel):
    element_name: str
    type: str
    attributes: list[str]
    base_address: Optional[str] = None


class RequestInputModel(BaseModel):
    url: list[HttpUrl]
    parser_config: list[RequestConfiguration]
