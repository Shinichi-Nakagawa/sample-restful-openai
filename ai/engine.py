from typing import List, Dict

import openai
from openai.openai_object import OpenAIObject
from ai.schema import Message


class OpenAI:
    def __init__(self, api_key: str, organization: str, model: str):
        self.api_key: str = api_key
        self.organization: str = organization
        self.model: str = model

    def create(self, messages: List[Message]) -> List[Message]:
        openai.organization = self.organization
        openai.api_key = self.api_key

        new_messages: List[Message] = messages
        messages: List[Dict[str, str]] = [{'role': m.role, 'content': m.content} for m in messages]
        _response: OpenAIObject = openai.ChatCompletion.create(
            model=self.model,
            messages=messages
        )
        # 会話のラリーをそのまま返す
        for r in _response.choices:
            response_message: Dict[str, str] = r["message"]
            _m: Message = Message(
                index=r.get('index', -100),
                role=response_message.get('role'),
                content=str(response_message.get('content', '')).strip()
            )
            new_messages.append(_m)
        return new_messages
