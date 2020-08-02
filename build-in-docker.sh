#!/bin/bash

CONTAINER="ubuntu:focal"
BUILDSCRIPT="docker-build-script.sh"

if [ -z "$BUILD_TAG" ]
then
  CONTAINERNAME='tmp_build_app_'$(date +"%H%S")
else
  CONTAINERNAME=$BUILD_TAG
fi

#echo $CONTAINERNAME
docker run -v $PWD/:/data --name $CONTAINERNAME $CONTAINER /data/$BUILDSCRIPT
#docker rm $CONTAINERNAME
