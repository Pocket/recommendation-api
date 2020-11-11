import os

topic_types = {
    'CuratedCandidatesFlow': 'curated',
    'AlgorithmicCandidatesFlow': 'algorithmic'
}

secrets = {
    'metaflow': os.getenv('METAFLOW_SECRET_NAME', 'CodeBuild/Metaflow')
}

dynamodb = {
    'endpoint_url': os.getenv('AWS_DYNAMODB_ENDPOINT_URL', None),
    'explore_topics_candidates_table': os.getenv('EXPLORE_TOPICS_CANDIDATES_TABLE', 'explore_topics_candidates')
}

sentry = {
    'dsn': os.getenv('SENTRY_DSN', 'https://examplePublicKey@o0.ingest.sentry.io/0'),
    'release': os.getenv('GIT_SHA', '1234'),
    'environment': os.getenv('ENVIRONMENT', 'local')
}
