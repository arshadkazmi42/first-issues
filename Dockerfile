FROM ubuntu:20.04

MAINTAINER Arshad Kazmi

RUN apt-get update
RUN apt-get -y install software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get update

RUN apt-get install -y git vim cron python3.8 python3-pip build-essential libssl-dev libffi-dev libxml2-dev libxslt1-dev zlib1g-dev python3.8-dev python3.8-venv

RUN pip3 install click
RUN pip3 install requests
RUN pip3 install tweepy

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

WORKDIR /home

RUN git clone https://github.com/arshadkazmi42/first-issues
WORKDIR /home/first-issues

RUN chmod +x cron.sh entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]

