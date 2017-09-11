FROM zhiyuli/tethys_base:1.5-release-1.2

### Begin - App-specific Additions/Changes ###
RUN apt-get update

### Install other libs
#RUN pip install XXXX

### END - App-specific Additions/Changes ###

# Enable rabbitmq api
RUN rabbitmq-plugins enable rabbitmq_management

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
