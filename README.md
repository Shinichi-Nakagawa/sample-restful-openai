# Sample RESTful API for Open AI

Open AI RESTful API sample for Python

## Prerequisites

Make sure you have the following software installed:

- Python 3.11 or higher
- Use to [FastAPI](https://fastapi.tiangolo.com/) and [poetry](https://python-poetry.org/)

## Installation

### Local Use

Create and activate a virtual environment. and Install the required packages.

```bash
poetry install
```

### Container(Docker)

TBD

## Usage

### Run the Application

```bash
python main.py
```

### Run the Application(uvicorn)

```bash
uvicorn main:app --reload
```

## Project Environment

setting for [environments.py](./environments.py)

```python
OPENAI_API_KEY: str = os.getenv('OPENAI_API_KEY', 'your openai api key')
OPENAI_ORGANIZATION: str = os.getenv('OPENAI_ORGANIZATION', 'your openai organization')
OPENAI_MODEL: str = os.getenv('OPENAI_MODEL', 'gpt-3.5-turbo')  # Use to Open AI Model(default: 3.5)
```

## Endpoints

- GET `/` - Get status(use to healthcheck)
- POST `/chat` - Create a new messages

## Deploy

### Cloud Run

TBD
