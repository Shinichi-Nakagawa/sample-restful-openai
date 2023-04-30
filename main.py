from typing import Dict
from fastapi import FastAPI
import uvicorn

from ai.chat import Request, Response

app = FastAPI()


@app.get("/")
def read_root():
    # Use to Healthcheck endpoints.
    return {"status": "OK"}


@app.post("/chat")
def chat(request: Request) -> Dict:
    # TODO: Generate
    response: Response = Response(**{'size': len(request.messages), 'messages': request.messages})  # type: ignore
    return response.dict  # type: ignore


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
