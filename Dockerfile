FROM python:3.9.0

WORKDIR /web_api_test

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt
RUN pip install -r requirements.txt

COPY ..