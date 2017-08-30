FROM zhiyuli/tethys_base:1.5-release-1.1
# This dockerfile will pip install requirements.txt when it is built

### Begin - App-specific Additions/Changes ###
RUN apt-get update
# install other libs

RUN git clone https://github.com/xhqiao89/pywps.git --branch tethys_fix /tmp/pywps && cd /tmp/pywps && python setup.py install && rm -rf /tmp/pywps
# change/update libs that are already installed by requirements.txt
#RUN apt-get update && apt-get install -y --no-install-recommends sqlite3

# force to re-install libs that have been downgraded by tethys requirements.txt
#RUN pip install hs_restclient==1.2.9

# install other libs
#RUN pip install django-heartbeat==2.0.2

### END - App-specific Additions/Changes ###

## install icommands
#ENV IRODS_VERSION 4.1.8
#RUN apt-get update && apt-get install -y --no-install-recommends curl libfuse2 && rm -rf /var/lib/apt/lists/* \
#    && curl ftp://ftp.renci.org/pub/irods/releases/4.1.8/ubuntu14/irods-icommands-4.1.8-ubuntu14-x86_64.deb -o irods-icommands.deb \
#    && dpkg -i irods-icommands.deb \
#    && apt-get -f install \
#    && rm irods-icommands.deb \
#    && apt-get purge -y --auto-remove curl

RUN mkdir /tethys

RUN groupadd tethys-group
RUN useradd -g tethys-group tethys-user
RUN mkdir -p /home/tethys-user
RUN chown -R tethys-user:tethys-group /home/tethys-user

WORKDIR /tethys

# persist tethys-platform and apps installed by pip after restarting container(s)
# persist /etc/cron jobs and /etc/passwd
VOLUME  ["/usr/local", "/tmp", "/etc"]

CMD ["/bin/bash"]
