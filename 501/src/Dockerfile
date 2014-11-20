FROM ubuntu
RUN apt-get -q -y update
RUN apt-get -q -y install python-pip
RUN pip install Flask pyotp
RUN useradd -m app
WORKDIR /home/app
CMD sudo -u app /usr/bin/python /home/app/app.py
ADD ./ /home/app/
