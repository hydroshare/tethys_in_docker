FROM zhiyuli/tethys_base:1.4-release-1.1
# This dockerfile will pip install requirements.txt when it is built

### Begin - App-specific Additions/Changes ###
RUN apt-get update
# install other libs

# change/update libs that are already installed by requirements.txt

# force to re-install libs that are downgraded by tethys requirements.txt
RUN pip install -U hs_restclient==1.2.9
RUN pip install -U pyOpenSSL==17.2.0

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
