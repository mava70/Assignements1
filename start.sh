#!/bin/bash
app="assignement1.test"
docker build -t ${app} .
docker run -d -p 56733:80 \
  --name=${app} \
  -v /$PWD:/var/www ${app}
