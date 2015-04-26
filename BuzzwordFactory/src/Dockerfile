FROM ubuntu
RUN apt-get -q -y update
RUN apt-get -q -y install xinetd openjdk-7-jre
RUN useradd -m app
WORKDIR /home/app
CMD sudo xinetd -dontfork
RUN echo 'ctf       1337/tcp' >> /etc/services
ADD ./etc/ /etc/
ADD ./ /home/app/
RUN chmod -R ugo-w /home/app

