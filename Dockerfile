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

#docker run --env-file ./.env -p 5100:5000 --mount type=bind,source="$(pwd)"/todo_app,target=/opt/todo_app development
# FROM python:3.10.5 AS BASE
# RUN curl -sSL https://install.python-poetry.org | python3 -
# WORKDIR /opt
# COPY poetry.lock pyproject.toml /opt/
# RUN /root/.local/bin/poetry install
# COPY todo_app /opt/todo_app
# CMD /root/.local/bin/poetry run gunicorn --bind 0.0.0.0 "todo_app.app:create_app()"


#FROM BASE AS PRODUCTION

#docker build --target development --tag todo-app:dev .
#docker build --target production --tag todo-app:production .

#docker run --env-file .env -p 8000:5000 --mount type=bind, source="$(pwd)"/target, target=/todo_app \
#nginx: development

#docker run --env-file .env -p 8000:5000  --mount type=bind, source="$(pwd)"/target, target=/todo_app \
#nginx: production






#RUN pip install REQUEST
#RUN PIP INSTALL poetry
# CMD ["PYTHON","/.app.py"]
# RUN ENTRYPOINT []
# RUN DOCKER BUILD - tag
# docker run 'image name'
# docker run -t -i image name to enter env parameters ? --env-file option from env.template
# from <bas python image > as base
# from bas as production and from base as development
#$ docker build --target development --tag todo-app:dev .
#  $ docker build --target production --tag todo-app:prod .
# $ docker run --env-file ./.env -p 5100:80 --mount type=bind,source="$(pwd)"/
# todo_app,target=/app/todo_app todo-app:dev 





