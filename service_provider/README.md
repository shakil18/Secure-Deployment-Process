## Client Application
This directory contains the application source-codes for the service provider side.

## Requirements
- [Docker <a href="https://docs.docker.com/get-docker/"> </a>](python_download)
- Access to the registry: **registry.scontain.com:5050/sconecuratedimages/**
- [Minikube <a href="https://minikube.sigs.k8s.io/docs/start/"> </a>](Minikube)
- [Helm-charts <a href="https://helm.sh/docs/intro/install/"> </a>](Helm_charts)

## Directory Structure

Here's the service provider side's directory structure:

```text
service_provider
├── automated_evaluation.sh         # for automated deployment without client interaction via web
├── bundle_scripts.sh               # bundle-several scripts for execution
├── cleanup_system.sh               # clean-up system from old deployments
├── Dockerfile-pull-repo            # Docker-image to run binary-fs
├── env_global.sh                   # system environments variable
├── helm-charts                     # directory, helm-charts
│   └── client-app                  # kubernetes client-app deployemt
│   └── las                         # kubernetes las deployemt
├── kubernetes_deploy.sh            # script for deploying client-app into kubernetes 
├── libbinary-fs.so                 # binary-fs for pulling client-repo
├── pull_repo-binary-fs-creation    # directory, contains binary-fs creation file
├── README.md                       # Service_provider's documentation
├── service_las.sh                  # starts docker las container
├── service_pull_repo.sh            # starts docker container to pull client-repo
└── session-template.yml            # Template for client's session 

```


## Workflow
The **bundle_scripts.sh** combines different scripts. </br>
First it pulls all the necessary docker images and checks if SGX device exists by executing the **env_global.sh** script. Then it attests CAS before uploading the client's session file.
Next, it builds docker image (**pull_repo**) for pulling client-repo by using **Dockerfile-pull-repo**.
A **client-session.yml** file is created by using the **session-template.yml** file. 
Finally, a file with environment variables is created as **env_session**.
