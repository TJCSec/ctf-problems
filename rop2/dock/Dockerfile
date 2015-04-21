FROM ubuntu
RUN dpkg --add-architecture i386
RUN apt-get -q -y update
RUN apt-get -q -y install xinetd libc6:i386
RUN useradd -m app
WORKDIR /home/app
CMD sudo xinetd -dontfork
RUN echo 'ctf       1337/tcp' >> /etc/services
ADD ./etc/ /etc/
ADD ./ /home/app/

