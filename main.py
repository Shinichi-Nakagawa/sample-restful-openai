from typing import Dict
from fastapi import FastAPI, Depends, HTTPException
import uvicorn

from environments import OPENAI_MODEL, OPENAI_ORGANIZATION, OPENAI_API_KEY
from ai.chat import OpenAI, OpenAIException
from ai.interface import RequestForm, ResponseBody

app = FastAPI()


def _engine() -> OpenAI:
    """
    Chat Engine
    :return: OpenAI Chat Engine
    """
    return OpenAI(api_key=OPENAI_API_KEY, organization=OPENAI_ORGANIZATION, model=OPENAI_MODEL)


@app.get("/")
def index() -> Dict[str, str]:
    # Use to Healthcheck endpoints.
    return {"status": "OK"}


@app.post("/chat")
async def chat(request: RequestForm, engine: OpenAI = Depends(_engine)) -> ResponseBody:
    # TODO: Validator
    try:
        messages = await engine.create(request.messages)
        response = ResponseBody(model=OPENAI_MODEL, chat=messages)
    except OpenAIException as e:
        raise HTTPException(status_code=500, detail=str(e))
    return response


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
