FROM python:3
COPY ./requirements.txt /tmp/requirements.txt
COPY testolino1.py /tmp
COPY chromedriver /usr/bin
RUN pip install -r /tmp/requirements.txt
RUN apt install chrome
