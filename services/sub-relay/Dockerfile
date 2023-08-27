FROM python:3.10-slim-bullseye

ENV VIRTUAL_ENV="/venv" \
    PATH="/venv/bin:$PATH" \
    PYTHONBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

COPY pyproject.toml poetry.lock /tmp/builder/

WORKDIR /tmp/builder/

RUN umask 0002 && \
    # Install poetry as a system app, so it doesn't end up in the prod image
    env -u VIRTUAL_ENV pip install --no-cache-dir poetry==1.6.1 && \
    # Create the venv
    python -m venv /venv && \
    mkdir -p /venv/src && \
    poetry install --no-interaction --no-dev && \
    rm -rf ~/.cache/pip ~/.cache/pypoetry/cache ~/.cache/pypoetry/artifacts

COPY . /app

WORKDIR /app

ENTRYPOINT ["gunicorn"]

CMD ["-b", ":8080", "-w", "1", "main:app"]

