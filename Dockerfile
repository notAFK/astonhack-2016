# Get ARCH LINUX
FROM alpine:latest
MAINTAINER Alexandru-Paul Copil, copil.alexander@gmail.com

# Get project files.
COPY . /fwgsim

# Update and Upgrade
RUN apk update && apk upgrade

# Install Python
RUN apk add --no-cache --update \
    python \
    py-pip \
