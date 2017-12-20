#!/bin/sh -e
tag='latest'
[[ -n "$1" ]] && tag="$1"
docker login
docker tag app-pyenv jmanoel7/app-pyenv:$tag
exec docker push jmanoel7/app-pyenv:$tag
