from typing import List
from dataclasses import dataclass
from enum import Enum

from pydantic import BaseModel, validator

from ai.schema import Messages, Message


class Role(Enum):
    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"


class RequestForm(BaseModel):
    # request message
    messages: List[Message]

    @validator("messages")
    def validate_messages(cls, messages: List[Message]):
        for m in messages:
            # check role
            if m.role not in [r.value for r in Role]:
                raise TypeError(f"Invalid Parameter for role: {m.role}")
            # check content
            if len(m.content) <= 0:
                raise ValueError(f"Invalid Parameter for content")
        return messages


@dataclass
class ResponseBody:
    # chat response
    model: str
    chat: Messages
