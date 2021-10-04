#!/bin/bash

set -a -e

# set ENVIRONMENT_VARIABLES from env_global.sh file
source env_global.sh

# attest cas before uploading the session file, accept CAS running in debug
# mode (-d) and outdated TCB (-G), we accept debug-mode (--only_for_testing-debug)
# since in debug, so ignore signer (--only_for_testing-ignore-signer )
# and also trust any enclave measurement value(--only_for_testing-trust-any)
docker run --device=$DEVICE -i $CLI_IMAGE sh -c "scone cas attest $SCONE_CAS_ADDR --only_for_testing-debug \
--only_for_testing-trust-any --only_for_testing-ignore-signer -G >/dev/null \
&& scone cas show-certificate" > cas-ca.pem

# build PYTHON_CURATED IMAGE with pull_repo.py
docker build -f Dockerfile-pull-repo -t pull_repo .

# Python-interpreter for cloning client's repo
export PULL_REPO_IMAGE="pull_repo"
export PULL_REPO_MRENCLAVE=`docker run -i --rm -e "SCONE_HEAP=256M" -e "SCONE_HASH=1" -e "SCONE_ALPINE=1" -e "LD_LIBRARY_PATH='/'" -e "SCONE_ALLOW_DLOPEN=2" $PULL_REPO_IMAGE python3`

# set environment variable and modify client-session
envsubst '$PULL_REPO_MRENCLAVE $CLIENT_INT_MRENCLAVE' < session-template.yml > client-session.yml

# create file with environment variables
cat > env_session << EOF
export SCONE_CAS_ADDR="$SCONE_CAS_ADDR"
export DEVICE="$DEVICE"
export SCONE_LAS_IMAGE="$SCONE_LAS_IMAGE"
export CLIENT_INT_IMAGE="$CLIENT_INT_IMAGE"
export CLIENT_APP_PATH="$CLIENT_APP_PATH"
EOF

echo "OK"
