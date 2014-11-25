FROM tutum/apache-php
RUN rm -rf /app/*
ADD . /app
RUN chmod -R ugo-w /app
RUN chmod -R ug+w /app/uploads
