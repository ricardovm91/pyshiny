# pull official base image
FROM python:3.6-slim

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .

RUN \
 apt-get -y update && \
 apt-get -y install libpq-dev gcc

RUN pip install -r requirements.txt

# copy project
COPY . .