#!/bin/bash

CONTAINER="ubuntu:focal"
CONTAINERNAME='tmp_build_app_'$(date +"%H%S")
BUILDSCRIPT="docker-build-script.sh"

#echo $CONTAINERNAME
docker run -it -v $PWD/:/data --name $CONTAINERNAME $CONTAINER /data/$BUILDSCRIPT
docker rm $CONTAINERNAME
