# Get ARCH LINUX
FROM crate:latest
MAINTAINER Alexandru-Paul Copil <copil.alexander@gmail.com>

# Get project files.
COPY . /fwgsim

# Update and Upgrade
RUN apk update && apk upgrade

# Install bash
RUN apk add --update bash

# Install and upgrade PiP
RUN apk add --update py-pip
RUN pip install --upgrade pip

# Install crate, googlemaps for Python
RUN pip install -r /fwgsim/requirements.txt

# Install crate database.
RUN rm -rf /var/cache/apk/*
