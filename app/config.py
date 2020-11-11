import os

# as this file executes in the 'app' directory, move up one dir to get to the project root
ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) + '/../'

aws = {
    'endpoint_url': os.getenv('AWS_DYNAMODB_ENDPOINT_URL', 'http://localstack:4566')
}

dynamodb = {
    'explore_topics_metadata_table': os.getenv('EXPLORE_TOPICS_METADATA_TABLE', 'explore_topics_metadata'),
    'explore_topics_candidates_table': os.getenv('EXPLORE_TOPICS_CANDIDATES_TABLE', 'explore_topics_candidates')
}

sentry = {
    # TODO add this as a SSM or secrets manager param and inject it as an ENV variable
    'dsn': os.getenv('SENTRY_DSN', 'https://examplePublicKey@o0.ingest.sentry.io/0'),
    'release': os.getenv('GIT_SHA', '1234'),
    'environment': os.getenv('ENVIRONMENT', 'local')
}
