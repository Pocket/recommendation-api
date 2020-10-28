FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8 as base

# Based on https://sourcery.ai/blog/python-docker/
FROM base AS python-deps

# Install pipenv
RUN pip install pipenv

# Install python dependencies in /.venv
WORKDIR /
COPY Pipfile .
COPY Pipfile.lock .
ENV PIPENV_VENV_IN_PROJECT=1
RUN if [ "$APP_ENV" = "production" ]; then pipenv install --deploy; else pipenv install --dev; fi

FROM base AS runtime

# Copy virtual env from python-deps stage
COPY --from=python-deps /.venv /.venv
ENV PATH="/.venv/bin:$PATH"

# Create and switch to a new user
RUN useradd --create-home appuser
USER appuser

# FastAPI config
ENV PORT=8000
EXPOSE $PORT

# Install application into container
WORKDIR /
COPY ./app /app
