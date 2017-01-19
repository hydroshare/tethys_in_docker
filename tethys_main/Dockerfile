FROM zhiyuli/tethys_base:1.4-release-1.0
# This dockerfile will pip install requirements.txt when it is built

### Begin - App-specific Additions/Changes ###
RUN apt-get update
# install other libs

# change/update libs that are already installed by requirements.txt
RUN pip install -U python-social-auth==0.2.21
RUN pip install requests-mock==1.2.0
### END - App-specific Additions/Changes ###

RUN mkdir /tethys

RUN groupadd tethys-group
RUN useradd -g tethys-group tethys-user
RUN mkdir -p /home/tethys-user
RUN chown -R tethys-user:tethys-group /home/tethys-user

WORKDIR /tethys

# persist tethys-platform and apps installed by pip after restarting container(s)
# persist cron jobs
VOLUME  ["/usr/local/lib", "/tmp", "/etc/cron.d"]

CMD ["/bin/bash"]
