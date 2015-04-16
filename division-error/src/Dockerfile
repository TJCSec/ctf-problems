FROM ubuntu
RUN apt-get -q -y update
RUN apt-get -q -y install python-pip
RUN pip install Flask gunicorn
RUN useradd -m app
WORKDIR /home/app
CMD sudo -u app /usr/local/bin/gunicorn -b 127.0.0.1:5000 -w 4 app:app
ADD ./ /home/app/
