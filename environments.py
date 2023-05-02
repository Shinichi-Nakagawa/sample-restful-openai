import os

OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "your openai api key")
OPENAI_ORGANIZATION: str = os.getenv("OPENAI_ORGANIZATION", "your openai organization")
OPENAI_MODEL: str = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")  # Use to Open AI Model(default: 3.5)
