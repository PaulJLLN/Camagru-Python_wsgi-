FROM python:3.10-slim-buster

WORKDIR /home

COPY pyproject.toml pyproject.toml
RUN pip3 install poetry
RUN poetry install

CMD [ "poetry","run", "python", "-u", "main.py"]