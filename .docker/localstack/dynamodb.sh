#!/bin/bash
set -x

TABLE_DEFINITIONS=(
  'explore_topics_metadata.json'
  'explore_topics_candidates.json'
)

for json_file in "${TABLE_DEFINITIONS[@]}"; do
  awslocal dynamodb create-table --cli-input-json file://$(dirname "${BASH_SOURCE[0]}")/dynamodb/${json_file}
done

set +x
