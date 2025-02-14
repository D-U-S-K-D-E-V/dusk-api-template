FROM python:3-slim AS base
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*
ARG APP_PORT=8000
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=app
ENV APP_PORT = ${APP_PORT}
COPY requirements.txt .
RUN python -m pip install -r requirements.txt
WORKDIR /app
COPY . .
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

FROM base AS dev
ENV DEBUG=true
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "$APP_PORT", "--reload", "--reload-dir", "/app"]

FROM base AS prod
ENV DEBUG=false
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "$APP_PORT"]