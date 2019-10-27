#!/bin/bash
app="marcoprivate/assignements1"
docker build -t ${app} .
docker run -d -p 56733:80 --name=${app} ${app}
