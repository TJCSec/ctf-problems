FROM ubuntu
RUN apt-get -q -y update
RUN apt-get -q -y install xinetd python
RUN useradd -m app
WORKDIR /home/app
CMD sudo xinetd -dontfork
RUN echo 'ctf       1337/tcp' >> /etc/services
ADD ./etc/ /etc/
ADD ./app.py /home/app/

