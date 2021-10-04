#!/bin/bash

# Kubernetes deployment script

set -a -e

# set ENVIRONMENT_VARIABLES from env_global.sh file
source env_session

start=$(date +%s%3N)
# start minikube
minikube delete
minikube start

end=$(date +%s%3N)
seconds=$(echo "$end - $start" | bc)
echo '=====> Minikube start time:' $seconds 'milliseconds <====='
echo -e 'Minikube start time: ' $seconds 'milliseconds' >> automated_dep_eval.txt

start=$(date +%s%3N)
# mount client-app repo files to minikube (using nohup allows you to run a command in the background and keep it running even when the terminal is off)
nohup minikube  mount "$CLIENT_APP_PATH:/host" &>/dev/null &

# use local docker images with Minikube
# pull docker image if not exist already
docker pull $SCONE_LAS_IMAGE
docker pull $CLIENT_INT_IMAGE

# cache docker image in minikube
minikube cache add $SCONE_LAS_IMAGE
minikube cache add $CLIENT_INT_IMAGE

# update client-app helm values
cd helm-charts/las
rm -rf values.yaml
envsubst '$SCONE_LAS_IMAGE $DEVICE' < generic-values.yaml > values.yaml
cd ..

# update client-app helm values
cd client-app
rm -rf values.yaml
envsubst '$CLIENT_INT_IMAGE $SCONE_CAS_ADDR $SESSION $DEVICE' < generic-values.yaml > values.yaml
cd ..

# deploy las to k8s
helm install las las
sleep 15

# deploy client-app to k8s
helm install client-app client-app
cd ..

end=$(date +%s%3N)
seconds=$(echo "$end - $start" | bc)
echo '=====> Kubernetes Deployed: ' $seconds 'milliseconds <====='
echo -e 'Kubernetes Deployed: ' $seconds 'milliseconds' >> automated_dep_eval.txt
echo -e '========================================' >> automated_dep_eval.txt
