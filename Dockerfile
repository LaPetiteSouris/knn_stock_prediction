FROM python:2.7

COPY . /src
WORKDIR /src

RUN pip install -r /src/dev-requirements.txt 
