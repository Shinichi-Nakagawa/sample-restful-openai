from typing import List

from pydantic import BaseModel

from ai.schema import Messages, Message


class Request(BaseModel):
    messages: List[Message]


class Response(BaseModel):
    model: str
    chat: Messages
