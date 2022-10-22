FROM python:3.10-slim-buster

WORKDIR /camagru

COPY pyproject.toml pyproject.toml
RUN pip3 install poetry
RUN poetry install

COPY . .

CMD [ "python3", "srcs/main.py"]