#!/bin/bash
set -x

TABLE_DEFINITIONS=(
  'MODELD-Local-SlateMetrics'
  'recommendation_api_metadata'
  'recommendation_api_candidates'
  'recommendation_api_clickdata'
  'recommendation_api_candidate_sets'
)

for json_file in "${TABLE_DEFINITIONS[@]}"; do
  #start fresh and delete the table if it exists
  awslocal dynamodb delete-table --table-name ${json_file} || true
  awslocal dynamodb create-table --cli-input-json file://$(dirname "${BASH_SOURCE[0]}")/dynamodb/${json_file}.json
  awslocal dynamodb batch-write-item --request-items file://$(dirname "${BASH_SOURCE[0]}")/dynamodb/${json_file}_data.json
done

# Enable TTL on CandidateSets (recommendation_api_candidate_sets) table to mimic production table
awslocal dynamodb update-time-to-live --table-name recommendation_api_candidate_sets --time-to-live-specification "Enabled=true, AttributeName=expires_at"

set +x
