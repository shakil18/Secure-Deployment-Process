This directory contains the application source-codes for the web-service.


## Requirements
- [Python interpreter >= Python 3.6 <a href="https://www.python.org/downloads/"> </a>](python_download)
- ```pip install Flask```


## Directory Structure

Here's the web-service side's directory structure:

```text
web_service        
    ├── service_provider_session_handling.py        # application's source code
    ├── session_files                               # contains session file for client's download
    ├── templates                                   
    │   └── index.html                              # web_service home page
    └── README.md                                   # Documentation
```


## Workflow

Execute **service_provider_session_handling.py**. It runs the web-service. 
When client ask to download the client-session file, it executes the service_provider's **bundle_scripts.sh** script to generate the session file.
After generating the session file, it sends the session file to the client for the download. 
Finally, when client submit the session-id, it executes the service_provider's **kubernetes_deploy.sh** script to complete the deployment into the kubernetes.
