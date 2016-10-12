FROM zhiyuli/ubuntu:16.04-onbuild
#FROM python:2.7-onbuild

### Begin - App-specific Additions ###
#RUN pip install xmltodict==0.10.2
#RUN pip install hs_restclient
RUN pip install gunicorn==19.6.0
### END - App-specific Additions ###

RUN mkdir /tethys
WORKDIR /tethys

