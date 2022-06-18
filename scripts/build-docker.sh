#!/bin/bash -xe
#This script will build a local docker image running on your local machine
clear

# Get an initial name from the builder
if [ -z "$1" ]; then
    DOCKERFILE=Dockerfile
    DEBUG=""
else
    DOCKERFILE=$1
    DEBUG="-debug"
fi

# main settings
VERSION=0.1.0
LATEST=latest 
PACKAGE=template-grpc$DEBUG
PORT=5534

if ! docker images -q $PACKAGE:$VERSION; then
    docker image rm $PACKAGE:$VERSION #remove old image         
fi   

docker build -t $PACKAGE:$VERSION -f $DOCKERFILE .    
docker tag $PACKAGE:$VERSION $PACKAGE:$LATEST
docker image ls $PACKAGE

echo "TEST RUN: docker run -it -p $PORT:$PORT $PACKAGE:$LATEST"