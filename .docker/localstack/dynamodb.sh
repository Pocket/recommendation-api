#!/bin/bash
set -x

TABLE_DEFINITIONS=(
  'recommendation_api_metadata'
  'recommendation_api_candidates'
)

for json_file in "${TABLE_DEFINITIONS[@]}"; do
  #start fresh and delete the table if it exists
  awslocal dynamodb delete-table --table-name ${json_file} || true
  awslocal dynamodb create-table --cli-input-json file://$(dirname "${BASH_SOURCE[0]}")/dynamodb/${json_file}.json
  awslocal dynamodb batch-write-item --request-items file://$(dirname "${BASH_SOURCE[0]}")/dynamodb/${json_file}_data.json
done

set +x
