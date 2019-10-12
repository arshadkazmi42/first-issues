FROM ubuntu:16.04

MAINTAINER Arshad Kazmi

RUN apt-get dist-upgrade
RUN apt-get update
RUN apt-get install -y software-properties-common python-software-properties
RUN add-apt-repository ppa:jonathonf/python-3.6
RUN apt-get update

RUN apt-get install -y git vim cron python3.6 python3-pip build-essential libssl-dev libffi-dev libxml2-dev libxslt1-dev zlib1g-dev python3.6-dev python3.6-venv

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

