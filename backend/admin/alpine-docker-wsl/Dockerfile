# The base image
FROM alpine:3.14

# Non-root user
ARG USER
ARG PASS

# Install applications
RUN apk update && \
        apk upgrade --available && \
        apk add --no-cache \
        openssl \
        ca-certificates \
        sudo \
	curl \
	docker \
        docker-compose

# Setup non-root user 
COPY ./conf/profile /home/${USER}/.profile
RUN /bin/ash -c 'adduser -h /home/${USER} -s /bin/ash -g ${USER} ${USER}; echo "${USER}:${PASS}" | chpasswd; \
                 addgroup ${USER} wheel; \
                 addgroup ${USER} docker; \
                 chown ${USER}:${USER} /home/${USER}/.profile; \
                 echo "%wheel ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers'

# Add Zscaler CAs
COPY ./ca/* /usr/local/share/ca-certificates/
RUN update-ca-certificates --fresh

# Add wsl config file
COPY ./conf/wsl.conf /etc/wsl.conf
RUN /bin/ash -c 'echo "default = ${USER}" >> /etc/wsl.conf'
