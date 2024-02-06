FROM python:3.11.5-slim

ENV PYTHONUNBUFFERED 1

RUN python -m pip install --upgrade pip

COPY ./requirements.txt /requirements.txt
RUN python -m pip install -r requirements.txt

RUN mkdir /backend
COPY . /backend
WORKDIR /backend