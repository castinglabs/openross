FROM nginx:1.9.10

ADD nginx.conf /etc/nginx/nginx.conf

RUN apt-get update \
	&& apt-get install -y \
		python \
		python-pip \
		python-dev \
		libgraphicsmagick++-dev \
		libboost-python-dev \
		libssh-dev \
		libffi-dev \
	&& rm -rf /var/lib/apt/lists/*

RUN pip install -U \
		pip \
		setuptools \
	  https://github.com/castinglabs/openross/releases/download/v0.1.0/openross-0.1.0-py2-none-any.whl

RUN mkdir -p /srv/http/cache \
	&& chown -R nginx /srv/http/cache

CMD cd /usr/local/lib/python2.7/dist-packages/openross \
	&& twistd --syslog --uid=$(id -u nginx) --gid=$(id -u nginx) openross \
	&& nginx -g "daemon off;"
