#!/bin/bash

vol_name=bookapi_vol_mg
cont_name=bookapi_cnt_mg
image_name=bookapi_img_mg

echo "Launching app in docker"
echo "Image name will be: $image_name"
echo "Volume name will be: $vol_name"
echo "Containter name will be: $cont_name"

###CLEANUP
echo "Stoping container $cont_name in case it is running"
docker-compose -f docker-compose.yml --project-directory . down

echo "Deleting container if it already exists" 
###docker container rm $cont_name 

echo "Removing image if it exists" 
###docker image rm $image_name

echo "Removing volume if it exists"
###docker volume rm $vol_name

###REBUILD
#echo "Building image"
docker-compose -f docker-compose.yml --project-directory . build

#echo "Instanciating image and launching container"
docker-compose -f docker-compose.yml --project-directory . up -d
