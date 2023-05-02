# ここはビルド用のコンテナ
FROM python:3.11-slim-buster as builder

WORKDIR /opt/app

RUN pip3 install poetry
COPY poetry.lock pyproject.toml poetry.toml ./
RUN poetry install --no-dev

# ここからは実行用コンテナの準備
FROM python:3.11-slim-buster as runner

ENV PYTHONPATH "${PYTHONPATH}:/opt/app/app"
RUN useradd -r -s /bin/false appuser
WORKDIR /opt/app
COPY --from=builder /opt/app/.venv /opt/app/.venv
COPY ai ./ai
COPY *.py .
USER appuser
EXPOSE 8000
CMD ["/opt/app/.venv/bin/gunicorn", "main:app", "--workers", "4", "--log-level", "warning", "--access-logfile", "-", "--bind", "0.0.0.0:8000", "--worker-class", "uvicorn.workers.UvicornWorker"]
