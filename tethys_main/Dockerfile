FROM zhiyuli/tethys_base:1.4-release-1.0
# This dockerfile will pip install requirements.txt when it is built

### Begin - App-specific Additions/Changes ###
RUN apt-get update
# install other libs

# change/update libs that are already installed by requirements.txt
RUN pip install -U plotly==2.0.0  # 2.0.1 breaks things
RUN pip install -U bokeh==0.12.4
RUN pip install -U python-social-auth==0.2.21
RUN pip install requests-mock==1.2.0
RUN pip install -U hs_restclient==1.2.9
RUN pip install python-irodsclient==0.5.0rc1
### END - App-specific Additions/Changes ###

## install icommands
#ENV IRODS_VERSION 4.1.8
#RUN apt-get update && apt-get install -y --no-install-recommends curl libfuse2 && rm -rf /var/lib/apt/lists/* \
#    && curl ftp://ftp.renci.org/pub/irods/releases/4.1.8/ubuntu14/irods-icommands-4.1.8-ubuntu14-x86_64.deb -o irods-icommands.deb \
#    && dpkg -i irods-icommands.deb \
#    && apt-get -f install \
#    && rm irods-icommands.deb \
#    && apt-get purge -y --auto-remove curl

RUN apt-get update && apt-get install -y --no-install-recommends zlib1g-dev libhdf5-serial-dev libproj-dev libnetcdf-dev netcdf-bin nco

RUN apt-get install -y --no-install-recommends libsqlite3-dev libsqlite3-mod-spatialite
RUN pip install -U pyproj==1.9.5.1
RUN pip install geojson==1.3.5
RUN pip install -U pysqlite==2.8.3
RUN pip install -U fiona==1.7.5
RUN pip install -U shapely==1.5.17
RUN pip install -U netCDF4==1.2.9
RUN pip install -U subset_nwm_netcdf==1.1.7
#RUN pip install GDAL==2.1.3

# Install celery
RUN apt-get install -y --no-install-recommends rabbitmq-server
RUN pip install -U celery==4.1.0
RUN pip install -U django-celery-results==1.0.1
RUN pip install -U django-celery-beat==1.0.1
RUN pip install -U flower

RUN mkdir /tethys

RUN groupadd tethys-group
RUN useradd -g tethys-group tethys-user
RUN mkdir -p /home/tethys-user
RUN chown -R tethys-user:tethys-group /home/tethys-user

WORKDIR /tethys

# persist tethys-platform and apps installed by pip after restarting container(s)
# persist /etc/cron jobs and /etc/passwd
VOLUME  ["/usr/local", "/tmp", "/etc"]
#VOLUME  ["/"]

CMD ["/bin/bash"]
