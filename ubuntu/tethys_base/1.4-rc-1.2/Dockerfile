# This Dockerfile is using the requirements.txt files from Tethys 1.4.0-candidate
# https://github.com/tethysplatform/tethys/commit/2f4f7f7d3a01313a50d5b09d7b9b520ba9475cae

FROM zhiyuli/tethys_base:1.4-rc-1.1
RUN apt-get update && apt-get upgrade -y

RUN apt-get install --fix-missing -y iputils-ping \
                                     nmap \
                                     telnet \
                                     netcat

# update pip
RUN pip install --upgrade pip

# install extra common python libs used by apps
COPY extra_requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/extra_requirements.txt && \
    rm -f /tmp/extra_requirements.txt


ONBUILD COPY requirements.txt /usr/src/app/
ONBUILD RUN pip install --no-cache-dir -r requirements.txt