#!/bin/bash

# run a container of "las" image

set -a -e

source env_session

#docker rm -f las
if docker ps -a | grep 'las'; then
        docker rm -f las
fi

#docker network rm if already exist old/same-name, create service_provider
if docker network ls | grep 'service_provider'; then
        docker network rm service_provider;
        docker network create service_provider
else
        docker network create service_provider
fi

docker run \
-d \
--network service_provider \
--name las \
--device=$DEVICE \
$SCONE_LAS_IMAGE