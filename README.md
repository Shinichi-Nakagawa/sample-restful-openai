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

```bash
docker compose build
docker compose up

```

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
DOCS_OPENAPI_URL: str = os.getenv("DOCS_OPENAPI_URL")  # OpenAPI docs url(default: None)
```

## Endpoints

- GET `/` - Get status(use to healthcheck)
- POST `/openai/chat` - Create a new messages, use to [Create chat completion](https://platform.openai.com/docs/api-reference/chat/create)

## Test

### type check

```bash
poetry run mypy .
```

### code check

```bash
poetry run black .
```
### unit test

```bash
poetry run pytest .
```

## Deploy

### Cloud Run

#### Create Repository(1st Time only.)

create repository for artifacts

```bash
gcloud artifacts repositories create restful-openapi \
    --repository-format=Docker \
    --location=asia-northeast1 \
    --description="Open AI RESTful API sample for Python" \
    --async
```

image build and deploy

```bash
sh ./deploy_cloudrun.sh ${your google cloud project id} ${imagetag}
```
