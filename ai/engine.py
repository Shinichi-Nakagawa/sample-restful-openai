from typing import List, Dict

import openai
from openai.openai_object import OpenAIObject
from openai.error import RateLimitError
from ai.schema import Message, Messages


class OpenAIException(Exception):
    pass


class OpenAI:
    def __init__(self, api_key: str, organization: str, model: str):
        self.api_key: str = api_key
        self.organization: str = organization
        self.model: str = model

    async def create(self, messages: List[Message]) -> Messages:
        openai.organization = self.organization
        openai.api_key = self.api_key

        try:
            _response: OpenAIObject = await openai.ChatCompletion.acreate(
                model=self.model, messages=[{"role": m.role, "content": m.content} for m in messages]
            )
        except RateLimitError as e:
            raise OpenAIException("OpenAI Ratelimit")
        # 会話のラリーをそのまま返す
        new_messages: List[Message] = list()
        for r in _response.choices:
            response_message: Dict[str, str] = r["message"]
            _m: Message = Message(
                index=r.get("index"),
                role=str(response_message.get("role")),
                content=str(response_message.get("content", "")).strip(),
            )
            new_messages.append(_m)
        return Messages(size=len(new_messages), messages=new_messages)
