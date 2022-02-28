from dataclasses import dataclass


@dataclass
class RequestConfig():
    url: str
    method: str
    nested: bool
    elements: list[str]
    arguments: list[str]
