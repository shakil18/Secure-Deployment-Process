## Pull-repo Binary-fs creation
This directory contains the application's source-code for the client side deployment. The script is written in python3 and Shell script.

## Requirements
- [Docker <a href="https://docs.docker.com/get-docker/"> </a>](python_download)
- Access to the registry: **registry.scontain.com:5050/sconecuratedimages/**

## Directory Structure

```text
pull_repo-binary-fs-creation
├── Dockerfile-binary-fs-creation   # Docker image for binary-fs creation              
├── git-scone-libgit_1_1_0.patch    # patch for libgit2 library          
├── pull_repo.py                    # source-code      
└── README.md                       # Documentation
```

## Image-creation

1. `docker build -f Dockerfile-binary-fs-creation -t binary-fs .`
2. `docker run -it binary-fs bash`
3. `docker cp <container-id>:/libbinary-fs.so .`

