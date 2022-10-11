FROM python:3.10.5 AS base
RUN curl -sSL https://install.python-poetry.org | python3 -
WORKDIR /opt
COPY poetry.lock pyproject.toml /opt/
RUN /root/.local/bin/poetry install
COPY todo_app /opt/todo_app
FROM base AS production
CMD /root/.local/bin/poetry run gunicorn --bind 0.0.0.0 "todo_app.app:create_app()"
FROM base AS development
CMD /root/.local/bin/poetry run flask run --host 0.0.0.0 
