#!/bin/bash

# - stop running docker containers
# - delete newly created/unnecessary files

set -a -e

# remove las docker-container if exist
if docker ps -a | grep 'las'; then
        docker rm -f las;
fi

# remove docker-network if already exist(old)
if docker network ls | grep 'service_provider'; then
        docker network rm service_provider;
fi

# remove docker-volume genesis if already exist
if docker volume ls | grep 'genesis'; then
        docker volume rm genesis
fi

# clean kubernetes
minikube delete

pwd_path=$(pwd)
rm -rf $HOME/client-app
rm -rf cas-ca.pem env_session client-session.yml
rm -rf helm-charts/client-app/values.yaml helm-charts/las/values.yaml
cd ../client/ && rm -rf session.yml client-key.pem client.pem client-session.yml
cd ../web_service/session_files && rm -rf *.*
cd $pwd_path
