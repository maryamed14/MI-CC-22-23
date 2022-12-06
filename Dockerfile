# syntax=docker/dockerfile:1

FROM python:3.11-slim-buster

WORKDIR /skincare

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "doit", "test"]
