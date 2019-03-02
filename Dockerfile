FROM python:3.7-alpine
MAINTAINER Astromeen Ltd

 ENV PYTHONUNBUFFERED 1

 COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
RUN pip install python --upgrade

 RUN mkdir /app
WORKDIR /app
COPY ./app /app

 RUN adduser -D user
USER user