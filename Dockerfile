FROM python:3.11-alpine as builder

RUN pip install poetry

WORKDIR /app

COPY . .

RUN poetry install --no-dev
ENV PYTHONUNBUFFERED=1
# CMD [ "cat", "pyproject.toml" ]
ENTRYPOINT ["poetry", "run", "python", "docker_bot/main.py"]