FROM python:3.8-alpine

ARG SERVICE_DIR
ARG APP_PORT

# Prepare the python environment
RUN apk update && \
    apk upgrade && \
    pip install --upgrade pip && \
    pip install pipenv && \
    pip install waitress

RUN mkdir -p /$SERVICE_DIR
RUN echo "1+$SERVICE_DIR+$APP_PORT"
WORKDIR /${SERVICE_DIR}

# Using the root docker context. See the docker-compose.yml file
COPY "./src/${SERVICE_DIR}/." /${SERVICE_DIR}

# Installing the project dependencies
RUN pipenv install

EXPOSE $APP_PORT

# Run with waitress
ENTRYPOINT ["sh", "-c", "pipenv run python main.py"]
