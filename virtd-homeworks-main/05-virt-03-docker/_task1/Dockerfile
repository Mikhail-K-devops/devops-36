FROM nginx:latest

MAINTAINER Mikhail K <mk_0@bk.ru>

ENV TZ=Europe/Moscow

RUN apt -y full-upgrade

RUN    echo "daemon off;" >> /etc/nginx/nginx.conf

COPY index.html /usr/share/nginx/html/index.html

WORKDIR /usr/share/nginx/html/

CMD [ "cat", "index.html" ]

CMD [ "nginx" ]
