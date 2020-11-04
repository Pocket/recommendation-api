import os

dynamodb = {
    'endpoint_url': os.getenv('AWS_DYNAMODB_ENDPOINT_URL', 'http:localstack:4566'),
    'explore_topics_metadata_table': os.getenv('EXPLORE_TOPICS_METADATA_TABLE', 'explore_topics_metadata'),
    'explore_topics_candidates_table': os.getenv('EXPLORE_TOPICS_CANDIDATES_TABLE', 'explore_topics_candidates')
}

sentry = {
    'dsn': os.getenv('SENTRY_DSN', 'https://examplePublicKey@o0.ingest.sentry.io/0'),
    'release': os.getenv('GIT_SHA', '1234'),
    'environment': os.getenv('ENVIRONMENT', 'local')
}
