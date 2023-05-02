from typing import List
from dataclasses import dataclass

from pydantic import BaseModel, validator

from ai.schema import Messages, Message, Role


class RequestForm(BaseModel):
    messages: List[Message]

    @validator("messages")
    def validate_messages(cls, messages):
        for m in messages:
            # check role
            if m.role not in [r.value for r in Role]:
                raise TypeError(f'Invalid Parameter for role: {m.role}')
            # check content
            if len(m.content) <= 0:
                raise ValueError(f'Not content')
        return messages


@dataclass
class ResponseBody:
    model: str
    chat: Messages
