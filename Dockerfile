FROM ubuntu:16.04

RUN apt-get dist-upgrade
RUN apt-get update
RUN apt-get install -y software-properties-common python-software-properties
RUN add-apt-repository ppa:jonathonf/python-3.6
RUN apt-get update

RUN apt-get install -y git vim openjdk-8-jdk python3.6 python3-pip build-essential libssl-dev libffi-dev libxml2-dev libxslt1-dev zlib1g-dev enchant python3.6-dev python3.6-venv gettext

RUN git clone https://github.com/arshadkazmi42/first-issues

CMD ["./createCron.sh"]

