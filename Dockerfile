FROM ubuntu:18.04

RUN apt update
RUN apt install -y software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt update
RUN apt install -y python3.8 python3.8-distutils python3.8-venv python3.8-dev python3-pip
RUN apt install -y libpq-dev

WORKDIR /workarea
COPY . /workarea/

RUN python3.8 -m pip install -r /workarea/requirements.txt 
RUN python3.8 -m pip install -r /workarea/requirements-dev.txt
RUN python3.8 -m pip install -e .
