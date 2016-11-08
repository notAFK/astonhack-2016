# Get ARCH LINUX
FROM alpine:latest
MAINTAINER Alexandru-Paul Copil, copil.alexander@gmail.com

# Get project files.
COPY . /fwgsim

# Update and Upgrade
RUN apk update && apk upgrade

# Install bash and curl
RUN apk add --update bash
RUN apk add --update curl

# Install Python
RUN apk add --no-cache --update \
    python \
    py-pip
RUN pip install --upgrade pip

# Install crate, googlemaps for Python
RUN pip install crate
RUN pip install googlemaps

# Install crate database.
RUN bash -c "$(curl -L install.crate.io)"

RUN rm -rf /var/cache/apk/*
