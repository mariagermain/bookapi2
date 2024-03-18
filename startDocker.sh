#!/bin/bash

vol_name=bookapi_cb_vol
cont_name=bookapi_cb_cnt
image_name=bookapi_cb_img

echo "Launching app in docker"
echo "Image name will be: $image_name"
echo "Volume name will be: $vol_name"
echo "Containter name will be: $cont_name"

###CLEANUP
echo "Stoping container $cont_name in case it is running"
docker stop $cont_name

echo "Deleting container if it already exists" 
docker container rm $cont_name 

echo "Removing image if it exists" 
docker image rm $image_name

echo "Removing volume if it exists"
docker volume rm $vol_name


###REBUILD
echo "Creating volume."
docker volume create --name $vol_name --opt device=$PWD --opt o=bind --opt type=none

echo "Building image"
docker build -t $image_name -f ./project/docker/Dockerfile .

echo "Instanciating image and launching container"
docker run -d -p 15555:5555 --mount source=$vol_name,target=/mnt/app/ --name $cont_name $image_name
