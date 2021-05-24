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
    'metadata': {
        'table': os.getenv('RECOMMENDATION_API_METADATA_TABLE', 'recommendation_api_metadata'),
    },
    'candidates': {
        'table': os.getenv('RECOMMENDATION_API_CANDIDATES_TABLE', 'recommendation_api_candidates'),
    },
    'candidate_sets': {
        'table': os.getenv('RECOMMENDATION_API_CANDIDATE_SETS_TABLE', 'recommendation_api_candidate_sets'),
    },
    'recommendation_clickdata': {
        'table': os.getenv('MODELD_RECOMMENDATION_METRICS_TABLE', 'recommendation_api_clickdata'),
        'pk': os.getenv('MODELD_RECOMMENDATION_METRICS_PK', 'mod_item'),
    },
    'slate_clickdata': {
        'table': os.getenv('MODELD_SLATE_METRICS_TABLE', 'MODELD-Local-SlateMetrics'),
        'pk': os.getenv('MODELD_SLATE_METRICS_PK', 'slates_pk'),
    },
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
    'clickdata_ttl': int(os.getenv('MEMCACHED_CLICKDATA_TTL', 3)), # TODO: Undo debug change. Reset this to 900.
    # Expire time in seconds for candidate sets
    'candidate_set_ttl': int(os.getenv('MEMCACHED_CANDIDATE_SET_TTL', 3)), # TODO: Undo debug change. Reset this to 900.
}

recit = {
    'endpoint_url': os.getenv('RECIT_ENDPOINT_URL', 'http://recit.readitlater.com')
}
