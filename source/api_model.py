from pydantic import BaseModel, HttpUrl


class RequestConfiguration(BaseModel):
    name: str
    method: str
    arguments: list[str]
    attributes: list[dict]


class RequestInputModel(BaseModel):
    url: HttpUrl  # can also just make string
    title: str
    config: RequestConfiguration
