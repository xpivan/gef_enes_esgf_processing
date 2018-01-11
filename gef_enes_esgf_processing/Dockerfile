FROM ubuntu:latest
MAINTAINER Xavier Pivan <xavier.pivan.ds@gmail.com>

ENV HOME /root
ENV HDF5_DIR /usr/local/hdf5

LABEL "eudat.gef.service.name"="esgf-usecase"
LABEL "eudat.gef.service.description"="Download a subset and average the selected data" 
LABEL "eudat.gef.service.version"="1.0"
LABEL "eudat.gef.service.input.1.name"="Input Directory" 
LABEL "eudat.gef.service.input.1.path"="/root/input"
LABEL "eudat.gef.service.input.1.type"="string"
LABEL "eudat.gef.service.input.1.filename"="/root/input/"
LABEL "eudat.gef.service.output.1.name"="Output Directory" 
LABEL "eudat.gef.service.output.1.path"="/root/output"

RUN apt-get update && apt-get install -y --no-install-recommends apt-utils && \
                                apt-get -yq install gcc \
								build-essential \
								wget \
								libhdf5-serial-dev \
								tar \
								bzip2 \
								m4 \
								zlib1g-dev \
								libopenmpi-dev


COPY hdf5-1.10.0-patch1.tar.bz2 hdf5-1.10.0-patch1.tar.bz2
RUN wget ftp://ftp.unidata.ucar.edu/pub/netcdf/netcdf-4.4.1.1.tar.gz;

#Build HDF5

RUN tar xjvf hdf5-1.10.0-patch1.tar.bz2 && \
    cd hdf5-1.10.0-patch1 && \
    CC=mpicc ./configure --enable-parallel --prefix=/usr/local/hdf5 && \
    make -j4 && \
    make install && \
    cd .. && \
rm -rf /hdf5-1.10.0-patch1 /hdf5-1.10.0-patch1.tar.bz2

RUN tar xzvf netcdf-4.4.1.1.tar.gz && \
	cd netcdf-4.4.1.1 && \
    ./configure --prefix=/usr/local/netcdf \ 
                CC=mpicc \
                LDFLAGS=-L/usr/local/hdf5/lib \
                CFLAGS=-I/usr/local/hdf5/include && \
    make -j4 && \
    make install && \
    cd .. && \
rm -rf netcdf-4.4.1.1 netcdf-4.4.1.1.tar.gz

RUN apt-get -y install python git && \
    apt-get -y install python-pip python-dev build-essential && \
    pip install --upgrade pip && \
    pip install numpy Cython \
    netCDF4 requests lxml 

RUN git clone https://github.com/cerfacs-globc/icclim $HOME/icclim && cd $HOME/icclim && \
    gcc -fPIC -g -c -Wall ./icclim/libC.c -o ./icclim/libC.o && \
    gcc -shared -o ./icclim/libC.so ./icclim/libC.o && \
    python setup.py install --user 

RUN git clone https://github.com/ESGF/esgf-compute-api $HOME/esgf-compute-api && \
    cd $HOME/esgf-compute-api && python setup.py install 

RUN git clone https://github.com/xpivan/gef_enes_esgf_processing $HOME/gef_enes_esgf_processing 

CMD python $HOME/gef_enes_esgf_processing/gef_enes_esgf_processing/example_esgf_processing.py --api_key dqPRtgPIInYV8ljvVEiz1qBZ5cDO2obpG6l423PKs3ivI2QQRolLjApDG21f715y






