from dataclasses import dataclass
from typing import List
from enum import Enum


class Role(Enum):
    SYSTEM = 'system'
    USER = 'user'
    ASSISTANT = 'assistant'


@dataclass
class Message:
    index: int
    role: str
    content: str


@dataclass
class Messages:
    size: int
    messages: List[Message]
