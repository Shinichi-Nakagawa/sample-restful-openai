from fastapi import APIRouter, Depends, HTTPException
from environments import OPENAI_MODEL, OPENAI_ORGANIZATION, OPENAI_API_KEY
from ai.chat import OpenAI, OpenAIException
from ai.interface import RequestForm, ResponseBody

app = APIRouter()


def _engine() -> OpenAI:
    """
    Chat Engine
    :return: OpenAI Chat Engine
    """
    return OpenAI(api_key=OPENAI_API_KEY, organization=OPENAI_ORGANIZATION, model=OPENAI_MODEL)


@app.post("/chat")
async def chat(request: RequestForm, engine: OpenAI = Depends(_engine)) -> ResponseBody:
    try:
        messages = await engine.create(request.messages)
        response = ResponseBody(model=OPENAI_MODEL, chat=messages)
    except OpenAIException as e:
        raise HTTPException(status_code=500, detail=str(e))
    return response
