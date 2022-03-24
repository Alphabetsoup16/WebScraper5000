from pydantic import BaseModel, HttpUrl


class RequestConfiguration(BaseModel):
    name: str
    type: str
    attributes: list[str]


class RequestInputModel(BaseModel):
    url: HttpUrl
    title: str
    config: RequestConfiguration
