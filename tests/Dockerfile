FROM python:3
RUN apk --update add bash nano git
COPY ./requirements.txt /tmp/requirements.txt
COPY testolino1.py /tmp
RUN pip install -r /tmp/requirements.txt
