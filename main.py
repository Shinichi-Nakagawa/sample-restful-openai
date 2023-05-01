from typing import Dict
from fastapi import FastAPI, Depends
import uvicorn

from environments import OPENAI_MODEL, OPENAI_ORGANIZATION, OPENAI_API_KEY
from ai.engine import OpenAI
from ai.chat import Request, Response
from ai.schema import Messages

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
def chat(request: Request, engine: OpenAI = Depends(_engine)) -> Response:
    # TODO: Validator
    messages: Messages = engine.create(request.messages)
    response: Response = Response(model=OPENAI_MODEL, chat=messages)
    return response


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
