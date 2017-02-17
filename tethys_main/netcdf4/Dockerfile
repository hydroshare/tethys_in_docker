FROM ubuntu:16.04
RUN apt-get update && apt-get upgrade -y && apt-get install -y software-properties-common

RUN apt-get install --fix-missing -y ca-certificates \
                                     apt-utils \
                                     build-essential \
                                     wget \
                                     vim \
                                     m4 \
                                     mpich
WORKDIR /tmp

# build mpe
RUN cd /tmp && \
    wget ftp://ftp.mcs.anl.gov/pub/mpi/mpe/mpe2-2.4.9b.tgz && \
    tar xvzf mpe2-2.4.9b.tgz && \
    rm -vf mpe2-2.4.9b.tgz && \
    cd mpe2* && \
    ./configure CC=/usr/bin/gcc MPI_CC=/usr/bin/mpicc --disable-f77 --prefix=/usr/local && \
    make -j8 && \
    make install

# compile zlib
RUN cd /tmp && \
    wget http://www.zlib.net/zlib-1.2.11.tar.gz && \
    tar xvzf zlib-1.2.11.tar.gz && \
    rm -vf zlib-1.2.11.tar.gz && \
    cd zlib-1.2.11 && \
    ./configure --prefix=/usr/local && \
    make -j8 && \
    make install

# compile szip
RUN cd /tmp && \
    wget https://support.hdfgroup.org/ftp/lib-external/szip/2.1.1/src/szip-2.1.1.tar.gz && \
    tar xvzf szip-2.1.1.tar.gz && \
    rm -vf szip-2.1.1.tar.gz && \
    cd szip-2.1.1 && \
    ./configure --prefix=/usr/local && \
    make -j8 && \
    make install

# compile hdf5
RUN cd /tmp && \
    wget https://support.hdfgroup.org/ftp/HDF5/releases/hdf5-1.10/hdf5-1.10.0-patch1/src/hdf5-1.10.0-patch1.tar && \
    tar xvf hdf5-1.10.0-patch1.tar && \
    rm -f hdf5-1.10.0-patch1.tar && \
    cd hdf5-1.10.0-patch1 && \
    CC=/usr/bin/mpicc ./configure --prefix=/usr/local --with-szlib --enable-parallel && \
    make -j8 && \
    make install

## compile parallel-netcdf
#RUN cd /tmp && \
#    wget http://cucis.ece.northwestern.edu/projects/PnetCDF/Release/parallel-netcdf-1.8.1.tar.gz && \
#    tar xvzf parallel-netcdf-1.8.1.tar.gz && \
#    rm -f parallel-netcdf-1.8.1.tar.gz && \
#    cd parallel-netcdf-1.8.1 && \
#    ./configure && \
#    make -j8 && \
#    make install

# compile netcdf4
RUN cd /tmp && \
    wget ftp://ftp.unidata.ucar.edu/pub/netcdf/netcdf-4.4.1.1.tar.gz && \
    tar xvzf netcdf-4.4.1.1.tar.gz && \
    rm -f netcdf-4.4.1.1.tar.gz && \
    cd netcdf-4.4.1.1 && \
    CC=mpicc ./configure --prefix=/usr/local --enable-shared --disable-pnetcdf --enable-parallel-tests && \
    make -j8 && \
    make install

ENV PATH /usr/local/bin:$PATH
RUN ldconfig

CMD ['/bin/bash']
