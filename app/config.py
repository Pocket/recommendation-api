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
    'candidate_sets': {
        'table': os.getenv('RECOMMENDATION_API_CANDIDATE_SETS_TABLE', 'recommendation_api_candidate_sets'),
    },
    'recommendation_metrics': {
        'table': os.getenv('MODELD_RECOMMENDATION_METRICS_TABLE', 'MODELD-Local-RecMetrics'),
        'pk': os.getenv('MODELD_RECOMMENDATION_METRICS_PK', 'recommendations_pk'),
    },
    'slate_metrics': {
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
    # Expire time in seconds for engagement metrics
    'metrics_ttl': int(os.getenv('MEMCACHED_METRICS_TTL', 900)),
    # Expire time in seconds for candidate sets
    'candidate_set_ttl': int(os.getenv('MEMCACHED_CANDIDATE_SET_TTL', 900)),
}

recit = {
    'endpoint_url': os.getenv('RECIT_ENDPOINT_URL', 'https://recit.readitlater.com')
}

qdrant = {
   'host': os.getenv('QDRANT_HOST', 'qdrant.readitlater.com'),
   'port': os.getenv('QDRANT_PORT', 443),
   'https': os.getenv('QDRANT_HTTPS', 'true') == 'true'
}


# Slates will be replace for the following set of QA users. See qa_slate_maps below.
qa_user_ids = ['47372502']
# For QA users, slates in keys will be replaced by the slate in the corresponding value.
qa_slate_map = {
    # Editors' Picks -> QA duplicate of this slate
    "2e3ddc90-8def-46d7-b85f-da7525c66fb1": "9dc26792-10ed-4fbe-a13d-6cce3a89b0a1",
    # Curated Personal Finance Slate -> QA duplicate of this slate
    "0c09627b-a409-4768-b87d-7e1d29259785": "e8251442-ef97-422f-ad65-0f28e6f7a0d6",
    # Our most-read Collections -> QA duplicate of this slate
    "0f322865-64e6-472d-8147-b3d6637a7d67": "b70d65c6-9171-40bf-bddb-5a60d42dd03f",
}

# This will redirect to the slate lineup value if the slate lineup id raises a PersonalizationError exception
personalization_fallback_slate_lineup = {
    # Web Home - Personalized Curated --> Web Home - Fallback Curated
    '05027beb-0053-4020-8bdc-4da2fcc0cb68': '249850f0-61c0-46f9-a16a-f0553c222800',
}
