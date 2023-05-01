from dataclasses import dataclass
from typing import List


@dataclass
class Message:
    role: str
    content: str


@dataclass
class Messages:
    size: int
    messages: List[Message]
