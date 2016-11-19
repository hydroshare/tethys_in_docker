FROM zhiyuli/tethys_base:1.4-rc-1.0
RUN apt-get update && apt-get upgrade -y

#RUN apt-get install --fix-missing -y iputils-ping

# update pip
RUN pip install --upgrade pip

ENV GDAL_DATA /usr/share/gdal

ONBUILD COPY requirements.txt /usr/src/app/
ONBUILD RUN pip install --no-cache-dir -r requirements.txt