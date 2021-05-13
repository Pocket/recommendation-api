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

# TODO: Structure each table as an object with table and pk, and drop the recommendation_api_ prefix.
dynamodb = {
    'endpoint_url': os.getenv('AWS_DYNAMODB_ENDPOINT_URL', None),
    'recommendation_api_metadata_table': os.getenv('RECOMMENDATION_API_METADATA_TABLE', 'recommendation_api_metadata'),
    'recommendation_api_candidates_table': os.getenv('RECOMMENDATION_API_CANDIDATES_TABLE', 'recommendation_api_candidates'),
    'recommendation_api_clickdata_table': os.getenv('RECOMMENDATION_API_CLICKDATA_TABLE', 'recommendation_api_clickdata'),
    'recommendation_clickdata': {
        'table': os.getenv('RECOMMENDATION_API_CLICKDATA_TABLE', 'recommendation_api_clickdata'),
        'pk': os.getenv('RECOMMENDATION_API_CLICKDATA_PK', 'mod_item'),
    },
    'slate_clickdata': {
        'table': os.getenv('RECOMMENDATION_API_CLICKDATA_TABLE', 'recommendation_api_slate_clickdata'),
        'pk': os.getenv('RECOMMENDATION_API_CLICKDATA_PK', 'pk_slate'),
    },
    'recommendation_api_candidate_sets_table': os.getenv('RECOMMENDATION_API_CANDIDATE_SETS_TABLE', 'recommendation_api_candidate_sets')
}

sentry = {
    'dsn': os.getenv('SENTRY_DSN', 'https://examplePublicKey@o0.ingest.sentry.io/0'),
    'release': os.getenv('GIT_SHA', '1234'),
    'environment': ENV
}

elasticache = {
    # Convert comma-separated string MEMCACHED_SERVERS to list.
    'servers': os.getenv('MEMCACHED_SERVERS', '001.example.com:11211,002.example.com:11211').split(','),
    # Expire time in seconds for clickdata
    'clickdata_ttl': int(os.getenv('MEMCACHED_CLICKDATA_TTL', 900)),
    # Expire time in seconds for candidate sets
    'candidate_set_ttl': int(os.getenv('MEMCACHED_CANDIDATE_SET_TTL', 900)),
}

recit = {
    'endpoint_url': os.getenv('RECIT_ENDPOINT_URL', 'http://recit.readitlater.com')
}
