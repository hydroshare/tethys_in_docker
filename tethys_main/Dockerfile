#FROM zhiyuli/ubuntu:16.04-onbuild
#FROM python:2.7-onbuild
#FROM zhiyuli/tethys_base:1.4.0-candidate
FROM zhiyuli/tethys_base:1.4-rc-1.1

### Begin - App-specific Additions ###
RUN apt-get update && apt-get install --fix-missing -y supervisor
RUN pip install gunicorn==19.6.0
### END - App-specific Additions ###

RUN mkdir /tethys

RUN groupadd tethys-group
RUN useradd -g tethys-group tethys-user
RUN mkdir -p /home/tethys-user
RUN chown -R tethys-user:tethys-group /home/tethys-user

WORKDIR /tethys

CMD ["/bin/bash"]
