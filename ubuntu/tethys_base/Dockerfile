# This Dockerfile is using the requirements.txt of Tethys 1.4.0-candidate
# https://github.com/tethysplatform/tethys/commit/2f4f7f7d3a01313a50d5b09d7b9b520ba9475cae

FROM ubuntu:16.04
RUN apt-get update && apt-get upgrade -y

RUN apt-get install --fix-missing -y apt-utils python-dev python-pip libpq-dev \
    libxml2-dev libxslt1-dev libssl-dev libffi-dev git-core supervisor

ENV PATH /usr/local/bin:$PATH

RUN pip install --upgrade pip

COPY requirements.txt /
RUN pip install -r /requirements.txt && \
    rm -f /requirements.txt

RUN pip install gunicorn==19.6.0

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ONBUILD COPY requirements.txt /usr/src/app/
ONBUILD RUN pip install --no-cache-dir -r requirements.txt
