#!/bin/bash

#export DEBIAN_FRONTEND=noninteractive
#apt update
#apt install -y nodejs npm
#apt install -y curl
#curl -sL https://deb.nodesource.com/setup_14.x -o nodesource_setup.sh
#bash nodesource_setup.sh
#apt install -y nodejs

#npm install -g @vue/cli

cd /the-last-table-editor
npm install
npm run build
mkdir webapp
cp -R run-app.sh webapp/
cp -R dist/ webapp/
cp -R backend/ webapp/

tar -zcvf webapp.tar.gz webapp
rm -R webapp