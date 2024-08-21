import os

# as this file executes in the 'app' directory, move up one dir to get to the project root
ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) + '/../'
JSON_DIR = os.path.join(ROOT_DIR, 'app/json')
TRANSLATIONS_DIR = os.path.join(ROOT_DIR, 'app/translations')

ENV_LOCAL = "local"
ENV_DEV = "development"
ENV_PROD = "production"

ENV = os.getenv("ENVIRONMENT", ENV_DEV)

VERSION = '1'  # RecommendationAPI is not configured to have automatically incrementing versions, so just set it to 1.

log_level = os.getenv("LOG_LEVEL", 'INFO').upper()

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

qdrant = {
    'host': os.getenv('QDRANT_HOST', 'qdrant.readitlater.com'),
    'port': os.getenv('QDRANT_PORT', 443),
    'https': os.getenv('QDRANT_HTTPS', 'true') == 'true',
    'collection': os.getenv('QDRANT_COLLECTION', 'articlesprod_v3')
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

# For running Open Telemetry locally, set `OTEL_DAEMON_ADDRESS`, otherwise defaults to production value.
otel_daemon_address = os.getenv('OTEL_DAEMON_ADDRESS', 'http://127.0.0.1:4317')

DEFAULT_TOPICS = [
    '25c716f1-e1b2-43db-bf52-1a5553d9fb74',  # Technology
    'c6242e35-4ef7-494f-ae9f-51f95b836424',  # Entertainment
    '45f8e740-42e0-4f54-8363-21310a084f1f',  # Self-improvement
]

# German Home shows different topics by default
GERMAN_HOME_TOPICS = [
    '25c716f1-e1b2-43db-bf52-1a5553d9fb74',  # Technology
    '1bf756c0-632f-49e8-9cce-324f38f4cc71',  # Business
    '058011b8-c70d-4a25-92e5-478e3ff0f0e6',  # Science
    '45f8e740-42e0-4f54-8363-21310a084f1f',  # Self-improvement
]

EN_GB_HOME_TOPICS = [
    'b0d0c28b-a2b4-4142-ac5b-8f2ac69766eb',  # Technology
    'f24c8da6-11d1-40de-9bf7-27dfde0bed9f',  # Business
    '963d5c09-052a-4649-8d36-097766de068f',  # Science
    '5d8e5764-77d7-4686-887e-84aaddcf482c',  # Self-improvement
]

FR_FR_HOME_TOPICS = [
    '19a95471-02b4-4133-81e6-21a7e66b247d',  # Technology
    'd2a31a31-3498-4f0a-8ca3-fbd29ed7c6c2',  # Business
    'c8e5f613-161f-411b-bb13-b3a590cae80c',  # Science
    'd77168b1-68a9-4942-91ea-bed18defca02',  # Self-improvement
]

IT_IT_HOME_TOPICS = [
    '052eb916-b15e-480e-b9f8-b06bc8070b15',  # Technology
    'ce8b6f8e-e5cc-4c1f-a280-32556a6ab902',  # Business
    'dbc6fbd2-6c2e-4bb2-98f5-fccc3b05835a',  # Science
    'a91654c2-b78d-4377-90ea-4f1252ff60c9',  # Self-improvement
]

ES_ES_HOME_TOPICS = [
    '177d3d8d-7733-402d-bf76-39eb9c2e24cd',  # Technology
    'e6e1696e-571a-49a6-ac27-1de508fc1f31',  # Business
    'bd983eba-0b4a-4916-82dd-d3a212ce934b',  # Science
    'b3c241b0-3651-4460-977c-568cbfbef2c3',  # Self-improvement
]

# Changes the slate lineups for home and removes thompson sampling for a new version of home
POCKET_HOME_PRIDE_FEATURE_FLAG = 'temp.recommendation-api.pride'
POCKET_HOME_V4_FEATURE_FLAG = 'temp.recommendation-api.pocket-home-v4'