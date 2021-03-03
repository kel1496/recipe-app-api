FROM python:3.7-alpine
MAINTAINER Kevin App Ltd

ENV PYTHONUNBUFFERED 1

RUN echo http://nl.alpinelinux.org/alpine/v3.9/main > /etc/apk/respositories; echo http://nl.alpinelinux.org/alpine/v3.9/community >> /etc/apk/respositories

COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps gcc libc-dev linux-headers postgresql-dev
RUN pip install -r /requirements.txt
RUN Apk del .tmp-build-deps

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user
