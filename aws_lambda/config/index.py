import os

topic_types = {
    'CuratedCandidatesFlow': 'curated',
    'AlgorithmicCandidatesFlow': 'algorithmic',
    'CoronavirusPageFlow': 'collection',
}

secrets = {
    'metaflow': os.getenv('METAFLOW_SECRET_NAME', 'CodeBuild/Metaflow')
}

dynamodb = {
    'endpoint_url': os.getenv('AWS_DYNAMODB_ENDPOINT_URL', None),
    'recommendation_api_candidates_table':
        os.getenv('RECOMMENDATION_API_CANDIDATES_TABLE', 'recommendation_api_candidates'),
    'recommendation_api_candidate_sets_table':
        os.getenv('RECOMMENDATION_API_CANDIDATE_SETS_TABLE', 'recommendation_api_candidate_sets'),
}

sentry = {
    'dsn': os.getenv('SENTRY_DSN', 'https://examplePublicKey@o0.ingest.sentry.io/0'),
    'release': os.getenv('GIT_SHA', '1234'),
    'environment': os.getenv('ENVIRONMENT', 'local')
}

# 'runtime:step-functions' is a tag present only on production flow runs. This should be regarded as temporary!!!
# We are going with this option because attempts to add a tag when the step function is created during code build
# failed. An issue has been filed with metaflow's git repo: https://github.com/Netflix/metaflow/issues/384
metaflow = {
    'tag': os.getenv('METAFLOW_DEPLOY_TAG', 'runtime:step-functions'),
    'service_url': os.getenv('METAFLOW_SERVICE_INTERNAL_URL', 'http://local')
}
