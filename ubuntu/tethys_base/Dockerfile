FROM ubuntu:16.04
RUN apt-get update && apt-get upgrade -y

RUN apt-get install -y build-essential python-dev python-pip libpq-dev \
    libxml2-dev libxslt1-dev libssl-dev libffi-dev git-core

ENV PATH /usr/local/bin:$PATH

RUN pip install --upgrade pip

COPY requirements.txt /
RUN pip install -r /requirements.txt && \
    rm -f /requirements.txt

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ONBUILD COPY requirements.txt /usr/src/app/
ONBUILD RUN pip install --no-cache-dir -r requirements.txt
