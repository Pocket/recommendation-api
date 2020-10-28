#!/bin/bash
set -e

pip3 install awscli-local

for Script in .docker/localstack/*.sh ; do
    bash "$Script"
done
