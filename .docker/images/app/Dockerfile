FROM python:3.8-slim-buster as base

# If we use the blow image the build will fail on package installations
#FROM python:3.8 as base

# Based on https://sourcery.ai/blog/python-docker/
FROM base AS python-deps
ARG GIT_SHA=local

# Install pipenv
RUN pip install pipenv

# Install python dependencies in /.venv
WORKDIR /
COPY Pipfile .
COPY Pipfile.lock .
ENV PIPENV_VENV_IN_PROJECT=1

RUN echo "GIT_SHA=${GIT_SHA}"
RUN if [ "$GIT_SHA" = "local" ]; then pipenv install --dev; else pipenv install --deploy; fi

FROM base AS runtime

# Copy production Gunicorn start script
COPY .docker/images/app/start.sh /start.sh
RUN chmod +x /start.sh

# Copy Gunicorn configuration
COPY .docker/images/app/gunicorn_conf.py /gunicorn_conf.py

# Copy local development Gunicorn start script
COPY .docker/images/app/start-reload.sh /start-reload.sh
RUN chmod +x /start-reload.sh

# Copy virtual env from python-deps stage
COPY --from=python-deps /.venv /.venv
ENV PATH="/.venv/bin:$PATH"

# Create and switch to a new user
RUN useradd --create-home appuser
USER appuser

# FastAPI config
ENV PORT=8000
ENV PYTHONPATH=/app
EXPOSE $PORT

#Sentry GITSHA
ENV GIT_SHA=$GIT_SHA

# Install application into container
WORKDIR /
COPY ./app /app

CMD ["/start.sh"]
