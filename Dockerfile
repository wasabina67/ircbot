FROM python:3.10-alpine

WORKDIR /usr/src

COPY /src .
COPY requirements.txt .
