FROM ubuntu
RUN dpkg --add-architecture i386
RUN apt-get -q -y update
RUN apt-get -q -y install python
RUN useradd -m app
WORKDIR /home/app
CMD sudo -u app /home/app/wrapper
ADD ./ /home/app/

