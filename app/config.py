import os

# as this file executes in the 'app' directory, move up one dir to get to the project root
ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) + '/../'
JSON_DIR = os.path.join(ROOT_DIR, 'app/json')

ENV_LOCAL = "local"
ENV_DEV = "development"
ENV_PROD = "production"

ENV = os.getenv("ENVIRONMENT", ENV_DEV)

service = {
    'domain': 'recommendation-api.readitlater.com' if ENV == ENV_PROD else 'recommendation-api.getpocket.dev'
}

dynamodb = {
    'endpoint_url': os.getenv('AWS_DYNAMODB_ENDPOINT_URL', None),
    'recommendation_api_metadata_table': os.getenv('RECOMMENDATION_API_METADATA_TABLE', 'recommendation_api_metadata'),
    'recommendation_api_candidates_table': os.getenv('RECOMMENDATION_API_CANDIDATES_TABLE', 'recommendation_api_candidates'),
    'recommendation_api_clickdata_table': os.getenv('RECOMMENDATION_API_CLICKDATA_TABLE', 'recommendation_api_clickdata'),
    'recommendation_api_candidate_sets_table': os.getenv('RECOMMENDATION_API_CANDIDATE_SETS_TABLE', 'recommendation_api_candidate_sets')
}

sentry = {
    'dsn': os.getenv('SENTRY_DSN', 'https://examplePublicKey@o0.ingest.sentry.io/0'),
    'release': os.getenv('GIT_SHA', '1234'),
    'environment': ENV
}
