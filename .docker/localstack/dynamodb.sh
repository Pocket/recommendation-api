#!/bin/bash
set -x

TABLE_DEFINITIONS=(
  'explore_topics_metadata'
  'explore_topics_candidates'
)

for json_file in "${TABLE_DEFINITIONS[@]}"; do
  awslocal dynamodb create-table --cli-input-json file://$(dirname "${BASH_SOURCE[0]}")/dynamodb/${json_file}.json
  awslocal dynamodb batch-write-item --request-items file://$(dirname "${BASH_SOURCE[0]}")/dynamodb/${json_file}_data.json
done

set +x
