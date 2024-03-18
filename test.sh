#!/bin/bash

echo "Running unittest"
coverage run --omit /home/lubuntu/.local/*,/usr/lib/*,*/test_*,*__init__.py -m unittest discover -s project -v
if [ $? -ne 0 ]
then
	echo "unittest failed, aborting"
	exit 1
fi

echo "Generating coverage report"
coverage html -d ./test/coverage/html
coverage report > ./test/coverage/coverageReport.txt

echo "Launching container"
./startDocker.sh
sleep 2

echo "Running deploiement tests"
python3 -m unittest discover -s project -v -p dtest_*.py

echo "Stopping container"
docker-compose -f docker-compose.yml --project-directory . down
