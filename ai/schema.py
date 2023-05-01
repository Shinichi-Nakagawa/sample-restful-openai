from dataclasses import dataclass
from typing import List


@dataclass
class Message:
    index: int
    role: str
    content: str


@dataclass
class Messages:
    size: int
    messages: List[Message]
