FROM zhiyuli/tethys_base:1.4-rc-1.1
RUN apt-get update && apt-get upgrade -y

RUN apt-get install --fix-missing -y iputils-ping \
                                     nmap \
                                     telnet \
                                     netcat

# update pip
RUN pip install --upgrade pip


ONBUILD COPY requirements.txt /usr/src/app/
ONBUILD RUN pip install --no-cache-dir -r requirements.txt