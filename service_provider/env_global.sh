#!/bin/bash

# Global environments

set -a -e

start=$(date +%s%3N)

export SCONE_CAS_ADDR="5-4-0.scone-cas.cf"
export DEVICE="/dev/sgx"

# downloaded client-app repo path
export CLIENT_APP_PATH="$HOME/client-app"

# Not nessecarily access to CAS image, add default
export SCONE_CAS_IMAGE="registry.scontain.com:5050/sconecuratedimages/services:cas-scone5.4"
export CAS_MRENCLAVE=`(docker pull $SCONE_CAS_IMAGE > /dev/null ; docker run -i --rm -e "SCONE_HASH=1" $SCONE_CAS_IMAGE cas) || echo a7b31d8833d03c0deb4a1e72dc87cdad22b3fbb4173ba07cbcad33dedf553ead`  # compute MRENCLAVE for current CAS

# LAS image
export SCONE_LAS_IMAGE="registry.scontain.com:5050/sconecuratedimages/services:las-scone5.4"

# Interpreter for client's source code deployment
# Python-Interpreter
export CLIENT_INT_IMAGE="registry.scontain.com:5050/sconecuratedimages/python:3.9.0-alpine3.12-scone5.4"
export CLIENT_INT_MRENCLAVE=`docker pull $CLIENT_INT_IMAGE > /dev/null ; docker run -i --rm -e "SCONE_HEAP=256M" -e "SCONE_HASH=1" -e "SCONE_ALPINE=1" -e "SCONE_ALLOW_DLOPEN=2" $CLIENT_INT_IMAGE python3`

# Node.js-Interpreter
#export CLIENT_INT_IMAGE="registry.scontain.com:5050/sconecuratedimages/apps:node-10.14-alpine"
#export CLIENT_INT_MRENCLAVE=`docker pull $CLIENT_INT_IMAGE > /dev/null ; docker run -i --rm -e "SCONE_HEAP=256M" -e "SCONE_HASH=1" -e "SCONE_ALPINE=1" -e "SCONE_ALLOW_DLOPEN=2" $CLIENT_INT_IMAGE node`

## Lua-Interpreter
#export CLIENT_INT_IMAGE="registry.scontain.com:5050/sconecuratedimages/apps:lua-5.3.5-alpine-scone5.4.0"
#export CLIENT_INT_MRENCLAVE=`docker pull $CLIENT_INT_IMAGE > /dev/null ; docker run -i --rm -e "SCONE_HEAP=256M" -e "SCONE_HASH=1" -e "SCONE_ALPINE=1" -e "SCONE_ALLOW_DLOPEN=2" $CLIENT_INT_IMAGE lua`

# R-Interpreter
#export CLIENT_INT_IMAGE="registry.scontain.com:5050/sconecuratedimages/apps:R"
#export CLIENT_INT_MRENCLAVE=`docker pull $CLIENT_INT_IMAGE > /dev/null ; docker run -i --rm -e "SCONE_HEAP=256M" -e "SCONE_HASH=1" -e "SCONE_ALPINE=1" -e "SCONE_ALLOW_DLOPEN=2" $CLIENT_INT_IMAGE R`

# Java Development Kit
#export CLIENT_INT_IMAGE="registry.scontain.com:5050/sconecuratedimages/apps:17-ea-jdk-alpine"
#export CLIENT_INT_MRENCLAVE=`docker pull $CLIENT_INT_IMAGE > /dev/null ; docker run -i --rm -e "SCONE_HEAP=256M" -e "SCONE_HASH=1" -e "SCONE_ALPINE=1" -e "SCONE_ALLOW_DLOPEN=2" $CLIENT_INT_IMAGE java`

# Need CLI IMAGE to attest SCONE CAS, create a session, update, and verify that session
export CLI_IMAGE="registry.scontain.com:5050/sconecuratedimages/sconecli:alpine-scone5.4"

# ensure that we have an up-to-date image
docker pull $CLI_IMAGE

# check if SGX device exists
if [[ ! -c "$DEVICE" ]] ; then
    export DEVICE_O="DEVICE"
    export DEVICE="/dev/isgx"
    if [[ ! -c "$DEVICE" ]] ; then
        echo "Neither $DEVICE_O nor $DEVICE exist"
        exit 1
    fi
fi

end=$(date +%s%3N)
seconds=$(echo "$end - $start" | bc)
touch automated_dep_eval.txt
echo -e 'Environments setup:' $seconds 'milliseconds' >> automated_dep_eval.txt
echo '=====> Environments setup:' $seconds 'milliseconds <====='