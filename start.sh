#!/bin/bash
app="assi"
docker build -t ${app} .
docker run -d -p 56733:80 --name=${app} ${app}
