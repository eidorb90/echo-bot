FROM ghcr.io/astral-sh/uv:python3.13-bookworm AS builder

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1
WORKDIR /app

RUN uv venv
COPY pyproject.toml ./
RUN uv sync
FROM python:3.13-slim
WORKDIR /app
COPY --from=builder /app/.venv .venv/
COPY . .
CMD ["/app/.venv/bin/flask", "run", "--host=0.0.0.0", "--port=8080"]
