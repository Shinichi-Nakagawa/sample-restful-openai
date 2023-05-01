from fastapi import FastAPI
import uvicorn

from environments import OPENAI_MODEL
from ai.chat import Request, Response
from ai.schema import Messages

app = FastAPI()


@app.get("/")
def read_root():
    # Use to Healthcheck endpoints.
    return {"status": "OK"}


@app.post("/chat")
def chat(request: Request):
    # TODO: Generate
    messages: Messages = Messages(size=len(request.messages), messages=request.messages)
    response: Response = Response(model=OPENAI_MODEL, chat=messages)
    return response


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
