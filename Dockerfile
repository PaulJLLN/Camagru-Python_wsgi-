FROM python:3.10-slim-buster

WORKDIR /home

RUN apt update && apt -y upgrade
RUN apt install -y build-essential python-dev

COPY pyproject.toml pyproject.toml
RUN pip3 install poetry
RUN poetry install


CMD [ "poetry","run", "uwsgi", "--http", ":8051", "--check-static", "/home/templates/resources", "--mime-file", "/etc/nginx/mime.types","--wsgi-file", "main.py"]