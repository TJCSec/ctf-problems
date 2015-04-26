FROM ubuntu
RUN apt-get -q -y update
RUN apt-get -q -y install nodejs-legacy npm
RUN npm install ws
RUN useradd -m app
WORKDIR /home/app
CMD while true; do sudo -u app /usr/bin/nodejs server.js; done
ADD ./ /home/app/
RUN chmod -R ugo-w /home/app
