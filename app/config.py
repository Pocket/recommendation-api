import os

# as this file executes in the 'app' directory, move up one dir to get to the project root
ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) + '/../'

service = {
    'domain': 'recommendation_api.readitlater.com' if os.getenv(
        'ENVIRONMENT') == 'production' else 'recommendation_api.getpocket.dev'
}

dynamodb = {
    'endpoint_url': os.getenv('AWS_DYNAMODB_ENDPOINT_URL', None),
    'recommendation_api_metadata_table': os.getenv('RECOMMENDATION_API_METADATA_TABLE', 'recommendation_api_metadata'),
    'recommendation_api_candidates_table': os.getenv('RECOMMENDATION_API_CANDIDATES_TABLE', 'recommendation_api_candidates')
}

sentry = {
    'dsn': os.getenv('SENTRY_DSN', 'https://examplePublicKey@o0.ingest.sentry.io/0'),
    'release': os.getenv('GIT_SHA', '1234'),
    'environment': os.getenv('ENVIRONMENT', 'local')
}
