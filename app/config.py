import os

# as this file executes in the 'app' directory, move up one dir to get to the project root
ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) + '/../'

service = {
    'domain': 'explore-topics.readitlater.com' if os.getenv(
        'ENVIRONMENT') == 'production' else 'explore-topics.getpocket.dev'
}

dynamodb = {
    'endpoint_url': os.getenv('AWS_DYNAMODB_ENDPOINT_URL', None),
    'explore_topics_metadata_table': os.getenv('EXPLORE_TOPICS_METADATA_TABLE', 'explore_topics_metadata'),
    'explore_topics_candidates_table': os.getenv('EXPLORE_TOPICS_CANDIDATES_TABLE', 'explore_topics_candidates'),
    'explore_topics_clickdata_table': os.getenv('EXPLORE_TOPICS_CLICKDATA_TABLE', 'explore_topics_clickdata')
}

sentry = {
    'dsn': os.getenv('SENTRY_DSN', 'https://examplePublicKey@o0.ingest.sentry.io/0'),
    'release': os.getenv('GIT_SHA', '1234'),
    'environment': os.getenv('ENVIRONMENT', 'local')
}
