FROM ubuntu
RUN apt-get -q -y update
RUN apt-get -q -y install nodejs npm
RUN npm install ws
RUN useradd -m app
WORKDIR /home/app
CMD sudo -u app /usr/bin/nodejs server.js 
ADD ./ /home/app/
RUN chmod -R ugo-w /home/app
