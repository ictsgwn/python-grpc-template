# Usage Purpose
This is a just template gRPC written for Python to upload files for cloud (azure) storage. Customize the servicer for your own purpose.

For more information regarding gRPC and how it works, refer to [gRPC documentation](https://grpc.io/docs/).

# Getting Started
1. Install packages required: `pip install -r requirements.txt`
1. Generate protobuffs: `bash scripts/build-proto.sh` (*Everytime the protobuff contract is changed, you have to regenerate the helpers.*)
1. Run the app: `bash scripts/startserver.sh`

## Project Structure
Main function that starts the server is `app/main.py`.
```
|__ app/
   |__ __init__.py
   |__ main.py 
   |__ servicer.py (Logic class that implement service for gRPC)
|__ proto/ (Contract for gRPC, defines functions that will be used and data structures for requests and responses)
   |__ example.proto
|__ scripts/ (helper scripts)
```

To mock a client request to the gRPC server:
1. Run the mock client: `python3 mock_client.py`

### Local Docker Build
1. For Windows 10 Professional, MacOS and Linux, install [Docker Desktop](https://www.docker.com/products/docker-desktop)
1. For Windows Home, [follow this link](https://docs.docker.com/docker-for-windows/install-windows-home/)
1. Edit the params in script `scripts/build-docker.sh` and build the image using Bash shell 
