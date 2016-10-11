FROM ubuntu:14.04
RUN apt-get update && apt-get upgrade -y

RUN apt-get install -y python-dev libpq-dev \
    libxml2-dev libxslt1-dev libffi-dev git-core wget python-setuptools

RUN apt-get purge python-pip
RUN mkdir -p /src

# https://pypi.python.org/packages/e7/a8/7556133689add8d1a54c0b14aeff0acb03c64707ce100ecd53934da1aa13/pip-8.1.2.tar.gz
COPY pip-8.1.2.tar.gz /src/pip-8.1.2.tar.gz

RUN cd /src  && \
    tar -xzvf pip-8.1.2.tar.gz && \
    cd pip-8.1.2  && \
    python setup.py install  && \
    cd /  && \
    rm -rvf /src

ENV PATH /usr/local/bin:$PATH

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ONBUILD COPY requirements.txt /usr/src/app/
ONBUILD RUN pip install --no-cache-dir -r requirements.txt
