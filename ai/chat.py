from typing import List

from pydantic import BaseModel
from ai.schema import Message


class Request(BaseModel):
    messages: List[Message]


class Response(BaseModel):
    size: int
    messages: List[Message]
