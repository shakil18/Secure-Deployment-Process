#!/bin/bash

# Script for automated deployment whole system

set -a -e

for i in 1 2 3 4 5 6 7 8 9 10
do
  start=$(date +%s%3N)
  echo " "
  echo "====================> Welcome $i times <===================="
  echo " "
  source cleanup_system.sh
  source bundle_scripts.sh
  cp client-session.yml ../client/
  cd ../client
  python3 create_client_session.py
  cd ../web_service
  python3 automated_service_provider.py
  cd ../service_provider

  sleep 60
  echo "====================> slept 60s <===================="
  kubectl logs $(kubectl get pods --template '{{range .items}}{{.metadata.name}}{{"\n"}}{{end}}' | grep client-app)

  end=$(date +%s%3N)
  seconds=$(echo "$end - $start" | bc)
  echo '=====> Total deployment time:' $seconds 'milliseconds <====='
done
