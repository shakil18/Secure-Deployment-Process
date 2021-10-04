#!/bin/bash

# run container of "pull_repo" image

set -a -e

source env_session

#docker volume rm genesis
if docker volume ls | grep 'genesis'; then
        docker volume rm genesis
fi

mkdir -p $CLIENT_APP_PATH

docker run \
--rm \
--network service_provider \
--name python \
--device=$DEVICE \
--user $(id -u):$(id -g) \
--mount type=bind,source="$CLIENT_APP_PATH",target=/home/client-app \
-i pull_repo \
sh -c "SCONE_ALLOW_DLOPEN=2 SCONE_VERSION=1 SCONE_LOG=0 SCONE_LAS_ADDR=las SCONE_HEAP=256M SCONE_CAS_ADDR=$SCONE_CAS_ADDR SCONE_CONFIG_ID=$SESSION/pull_repo python3"
