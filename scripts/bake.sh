#!/bin/bash
set -o allexport

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd $DIR/..

if [ -e .env ]; then
	source .env
fi
echo $TESTPYTHONRESOURCE_DOCKER_IMAGE_LOCAL

docker build -t $TESTPYTHONRESOURCE_DOCKER_IMAGE_LOCAL:$TESTPYTHONRESOURCE_IMAGE_VERSION . 
