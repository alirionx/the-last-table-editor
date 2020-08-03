#!/bin/bash

#CONTAINER="ubuntu:focal"
CONTAINER="dockereg.app-scape.lab/nodejs"
BUILDSCRIPT="docker-build-script.sh"

if [ -z "$BUILD_TAG" ]
then
  CONTAINERNAME='tmp_build_app_'$(date +"%H%S")
else
  CONTAINERNAME=$BUILD_TAG
fi

#echo $CONTAINERNAME
docker run -it -v $PWD/:/the-last-table-editor --name $CONTAINERNAME $CONTAINER /the-last-table-editor/$BUILDSCRIPT
#docker rm $CONTAINERNAME
