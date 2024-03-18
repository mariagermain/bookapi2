#!/bin/bash

export PYTHONPATH=$PWD/project/
echo python path is: 
echo $PYTHONPATH

echo running the following python program
echo $@
python3 "$@"
