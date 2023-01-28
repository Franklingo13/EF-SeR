#! /bin/bash

DOCKER_USER=burp
DOCKER_HOME=/home/$DOCKER_USER

## GUI Support (https://stackoverflow.com/a/25280523)
XSOCK=/tmp/.X11-unix
XAUTH=/tmp/.docker.xauth
touch $XAUTH
xauth nlist :0 | sed -e 's/^..../ffff/' | xauth -f $XAUTH nmerge -

## BURP Dir
burp_dir=$HOME/.java/.userPrefs:$DOCKER_HOME/.java/.userPrefs
burp_conf=$HOME/.BurpSuite:$DOCKER_HOME/.BurpSuite

## -u flag = https://github.com/moby/moby/issues/3206#issuecomment-152682860
sudo docker run -it --rm -h burpdock --name burpdock \
    -u $(id -u):$(id -g) \
    -v $XSOCK:$XSOCK -v $XAUTH:$XAUTH -e XAUTHORITY=$XAUTH \
    -v $burp_dir -v $burp_conf \
    -p 8080:8080 \
    --env="DISPLAY" \
    burpdock
