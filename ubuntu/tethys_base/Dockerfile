# This Dockerfile is using the requirements.txt files from Tethys 1.4.0-candidate
# https://github.com/tethysplatform/tethys/commit/2f4f7f7d3a01313a50d5b09d7b9b520ba9475cae

FROM ubuntu:16.04
RUN apt-get update && apt-get upgrade -y && apt-get install -y software-properties-common

RUN apt-get install --fix-missing -y ca-certificates \
                                     apt-utils \
                                     build-essential \
                                     wget \
                                     python-dev \
                                     python-pip \
                                     net-tools \
                                     libpq-dev \
                                     libxml2-dev \
                                     libxslt1-dev \
                                     libssl-dev \
                                     libffi-dev \
                                     git-core \
                                     supervisor \
                                     vim \
                                     postgresql-client \
                                     python-tk \
                                     iputils-ping \
                                     nmap \
                                     telnet \
                                     netcat


ENV PATH /usr/local/bin:$PATH
# update pip
RUN pip install --upgrade pip

# compile and install GDAL and its python wrapper
COPY lib_src/gdal-2.1.2.tar.gz /tmp/
RUN tar xzvf /tmp/gdal-2.1.2.tar.gz --directory /tmp && \
    rm -f /tmp/gdal-2.1.2.tar.gz && \
    cd /tmp/gdal-2.1.2 && \
    ./configure --with-python --prefix=/usr && \
    make && \
    make install && \
    ldconfig && \
    rm -rf /tmp/gdal-2.1.2

# compile and install phreeqc
COPY lib_src/iphreeqc-3.3.3-10424.tar.gz /tmp/
RUN tar xzvf /tmp/iphreeqc-3.3.3-10424.tar.gz --directory /tmp && \
    rm -f /tmp/iphreeqc-3.3.3-10424.tar.gz && \
    cd /tmp/iphreeqc-3.3.3-10424 && \
    ./configure --prefix=/usr && \
    make && \
    make install && \
    ldconfig && \
    rm -rf /tmp/iphreeqc-3.3.3-10424

# install iphreeqc python wrapper
COPY lib_src/phreeqpy-0.2.0.tar.gz /tmp/
RUN tar xzvf /tmp/phreeqpy-0.2.0.tar.gz --directory /tmp && \
    rm -f /tmp/phreeqpy-0.2.0.tar.gz && \
    cd /tmp/phreeqpy-0.2.0 && \
    python setup.py install && \
    rm -rf /tmp/phreeqpy-0.2.0

# link iphreeqc python wrapper to iphreeqc lib
RUN cp /usr/lib/libiphreeqc.so /usr/local/lib/python2.7/dist-packages/phreeqpy-0.2.0-py2.7.egg/phreeqpy/iphreeqc && \
    rm /usr/local/lib/python2.7/dist-packages/phreeqpy-0.2.0-py2.7.egg/phreeqpy/iphreeqc/libiphreeqc.so.0.0.0 && \
    mv /usr/local/lib/python2.7/dist-packages/phreeqpy-0.2.0-py2.7.egg/phreeqpy/iphreeqc/libiphreeqc.so /usr/local/lib/python2.7/dist-packages/phreeqpy-0.2.0-py2.7.egg/phreeqpy/iphreeqc/libiphreeqc.so.0.0.0

# install netCDF4 dependencies
RUN apt-get install --fix-missing -y zlib1g-dev \
                                     libhdf5-serial-dev \
                                     libnetcdf-dev

# fix broken pip installation in requirements.txt
#RUN pip install --no-cache-dir "Paste>=2.0.3, <2.1"
#RUN pip install --no-cache-dir "PasteDeploy>=1.5.2, <1.6"
#RUN pip install --no-cache-dir "PasteScript>=2.0.2, <2.1"
#RUN pip install --no-cache-dir "django-guardian>=1.4.6, <1.5"

# install tethys system requirements.txt
COPY requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt && \
    rm -f /tmp/requirements.txt

# install extra common python libs used by apps
COPY extra_requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/extra_requirements.txt && \
    rm -f /tmp/extra_requirements.txt

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ONBUILD COPY requirements.txt /usr/src/app/
ONBUILD RUN pip install --no-cache-dir -r requirements.txt
