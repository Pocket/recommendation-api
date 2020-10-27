#!/bin/bash
set -e

sudo apt-get update && sudo apt-get install -y python3-pip
pip3 install awscli-local

for Script in .docker/localstack/*.sh ; do
    bash "$Script"
done
