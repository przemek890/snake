#!/bin/bash

if [ "$(docker ps -a -q)" ]; then
  docker stop $(docker ps -a -q)
  docker rm $(docker ps -a -q)
fi

if [ "$(docker images -q)" ]; then
  docker rmi $(docker images -q)
fi

docker ps -a
docker images

cd Snake_files
if [ ! -d "log" ]; then
  mkdir log
fi
