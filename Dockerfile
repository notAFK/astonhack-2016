# Get ARCH LINUX
FROM crate:latest
MAINTAINER Alexandru-Paul Copil, copil.alexander@gmail.com

# Get project files.
COPY . /fwgsim

# Update and Upgrade
RUN apk update && apk upgrade

# Install and upgrade PiP
RUN apk add --update py-pip
RUN pip install --upgrade pip

# Install crate, googlemaps for Python
RUN pip install crate
RUN pip install googlemaps

# Install crate database.
RUN rm -rf /var/cache/apk/*
