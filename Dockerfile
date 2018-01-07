FROM ubuntu:latest
MAINTAINER Xavier Pivan <xavier.pivan.ds@gmail.com>

ENV HOME /root
ENV HDF5_DIR /usr/local/hdf5

LABEL "eudat.gef.service.name"="nco-lib"
LABEL "eudat.gef.service.description"="Execute nco command on ncdf" 
LABEL "eudat.gef.service.version"="1.0"
LABEL "eudat.gef.service.input.1.name"="Input Directory" 
LABEL "eudat.gef.service.input.1.path"="/root/input"
LABEL "eudat.gef.service.input.1.type"="string"
LABEL "eudat.gef.service.output.1.name"="Output Directory" 
LABEL "eudat.gef.service.output.1.path"="/root/output"

CMD ls