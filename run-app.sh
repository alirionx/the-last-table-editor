#!/bin/bash

if python3 --version > /dev/null 2>&1; then
  PYCMD='python3'
elif 
  python --version > /dev/null 2>&1; then
  PYCMD='python'
else  echo 'Can not detect Python3 on your system, exiting.'
fi

#echo $PYCMD

$PYCMD backend/app-server.py