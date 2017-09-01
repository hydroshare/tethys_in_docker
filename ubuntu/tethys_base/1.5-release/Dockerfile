#tethys_base:1.5-release-1.2

FROM ubuntu:16.04
RUN apt update && apt upgrade -y && apt install -y software-properties-common

RUN apt update && apt install --fix-missing -y ca-certificates \
                                     apt-utils \
                                     build-essential \
                                     wget \
                                     python-dev \
                                     libpq-dev \
                                     libxml2-dev \
                                     libxslt1-dev \
                                     libssl-dev \
                                     libffi-dev \
                                     git-core \
                                     supervisor \
                                     vim \
                                     nano \
                                     postgresql-client \
                                     python-tk \
                                     net-tools \
                                     iputils-ping \
                                     nmap \
                                     telnet \
                                     netcat
# install latest pip
RUN wget -O /tmp/get-pip.py https://bootstrap.pypa.io/get-pip.py  && \
    python /tmp/get-pip.py  && \
    rm -f /tmp/get-pip.py && \
    pip install --upgrade pip

ENV PATH /usr/local/bin:$PATH

# install pre-built gdal binary
ENV GDAL_DATA /usr/share/gdal
# COPY lib_src/gdal-2.1.2-ubuntu16-binary.tar.gz /tmp/
RUN cd /tmp && \
    wget https://www.hydroshare.org/django_irods/download/2fdadb064d6a4d2e925fd9bac3b71a56/data/contents/gdal-2.1.2-ubuntu16-binary.tar.gz && \
    tar xzvf gdal-2.1.2-ubuntu16-binary.tar.gz && \
    rm -f gdal-2.1.2-ubuntu16-binary.tar.gz && \
    cp -rf gdal/bin/* /usr/bin/ && \
    cp -rf gdal/include/* /usr/include/ && \
    cp -rf gdal/share/gdal /usr/share/ && \
    cp -rf gdal/lib/* /usr/lib/ && \
    rm -rf gdal && \
    ldconfig

# install iphreeqc pre-built binary
COPY lib_src/iphreeqc-3.3.9-11951-ubuntu16-binary.tar.gz /tmp/
RUN cd /tmp && \
    tar xzvf iphreeqc-3.3.9-11951-ubuntu16-binary.tar.gz && \
    rm -f iphreeqc-3.3.9-11951-ubuntu16-binary.tar.gz && \
    cp -rf iphreeqc/share/doc/* /usr/share/doc/ && \
    cp -rf iphreeqc/include/* /usr/include/ && \
    cp -rf iphreeqc/lib/* /usr/lib/ && \
    rm -rf iphreeqc && \
    ldconfig

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
RUN apt-get update && apt-get install --fix-missing -y zlib1g-dev \
                                     libhdf5-serial-dev \
                                     libnetcdf-dev \
                                     libproj-dev \
                                     netcdf-bin \
                                     nco \
                                     sqlite3 \
                                     libsqlite3-dev \
                                     libsqlite3-mod-spatialite \
                                     rabbitmq-server
# install grass7.2.1
RUN add-apt-repository ppa:ubuntugis/ubuntugis-unstable -y && apt-get update && apt-get install -y --no-install-recommends grass=7.2.1-1~xenial4


#install icommands
#ENV IRODS_VERSION 4.1.8
#RUN apt-get update && apt-get install -y --no-install-recommends curl libfuse2 && rm -rf /var/lib/apt/lists/* \
#    && curl ftp://ftp.renci.org/pub/irods/releases/4.1.8/ubuntu14/irods-icommands-4.1.8-ubuntu14-x86_64.deb -o irods-icommands.deb \
#    && dpkg -i irods-icommands.deb \
#    && apt-get -f install \
#    && rm irods-icommands.deb \
#    && apt-get purge -y --auto-remove curl

# Install iRODS v.4.2.1
ENV IRODS_VERSION 4.2.1
RUN apt-get update && apt-get install -y apt-transport-https && wget -qO - https://packages.irods.org/irods-signing-key.asc | apt-key add - \
    && echo "deb [arch=amd64] https://packages.irods.org/apt/ trusty main" | \
    tee /etc/apt/sources.list.d/renci-irods.list \
    && apt-get update && apt-get install -y \
    irods-runtime=4.2.1 \
    irods-icommands=4.2.1

# install tethys and other requirements.txt
COPY requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt && \
    rm -f /tmp/requirements.txt

# install sherry's pywps
RUN git clone https://github.com/xhqiao89/pywps.git --branch tethys_fix /tmp/pywps && cd /tmp/pywps && python setup.py install && rm -rf /tmp/pywps


RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ONBUILD COPY requirements.txt /usr/src/app/
ONBUILD RUN pip install --no-cache-dir -r requirements.txt
