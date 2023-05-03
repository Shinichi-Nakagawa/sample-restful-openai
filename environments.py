import os
from typing import Any

OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "your openai api key")
OPENAI_ORGANIZATION: str = os.getenv("OPENAI_ORGANIZATION", "your openai organization")
OPENAI_MODEL: str = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")  # Use to Open AI Model(default: 3.5)
DOCS_OPENAPI_URL: str = os.getenv("DOCS_OPENAPI_URL")  # OpenAPI docs url(default: None)
