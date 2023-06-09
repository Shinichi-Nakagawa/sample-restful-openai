from typing import Dict

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
import uvicorn

from environments import DOCS_OPENAPI_URL
from ai import app as openai_app

if DOCS_OPENAPI_URL:
    # change docs url
    app = FastAPI(docs_url=f"/{DOCS_OPENAPI_URL}")
else:
    # default docs url
    app = FastAPI()

# TODO Use Production（disable docs url）
# app =FastAPI(docs_url=None)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        # TODO CORS URLS
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(openai_app.app, prefix="/openai", tags=["openai"])


@app.get("/")
def index() -> Dict[str, str]:
    # Use to Healthcheck endpoints.
    return {"status": "OK"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
