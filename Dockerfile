# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app

COPY Pipfile Pipfile.lock
RUN pip3 install pipenv
RUN pipenv install Pipfile

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]