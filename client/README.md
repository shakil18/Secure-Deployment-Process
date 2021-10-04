## Client Application
This directory contains the application's source-code for the client side deployment. The script is written in python3 and Shell script.

## Requirements
- [Python-interpreter >= Python 3.6 <a href="https://www.python.org/downloads/"> </a>](python_download)


## Directory Structure

Here's the client side application's directory structure:

```text
client
├── client_certificate          # script generates client's public certificate and key              
├── clientcertreq.conf          # client's certificates config file          
├── create_client_session.py    # client's side application (source-code)      
└── README.md                   # Documentation
```


## Deployment

1. **client-session.yml** file should be present in the root path (client/client-session.yml).
2. run ```$ python3 create_client_session.py```