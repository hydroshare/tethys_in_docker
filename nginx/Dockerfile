FROM ubuntu:16.04

RUN apt-get update
RUN apt-get install --no-install-recommends --no-install-suggests --fix-missing -y \
						ca-certificates \
						nginx-extras \
						luajit \
						lua-cjson \
						gettext-base \
						vim \
                        net-tools \
                        iputils-ping \
                        nmap \
                        telnet \
                        netcat

RUN rm -rf /var/lib/apt/lists/*

# forward request and error logs to docker log collector
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
	&& ln -sf /dev/stderr /var/log/nginx/error.log

EXPOSE 80 443

CMD ["nginx", "-g", "daemon off;"]