FROM ubuntu
RUN apt-get -q -y update
RUN apt-get -q -y install python
RUN useradd -m app
WORKDIR /home/app
CMD sudo -u app /home/app/app.py
ADD ./ /home/app/
