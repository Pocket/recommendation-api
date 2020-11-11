import os

secrets = {
    'metaflow': os.getenv('METAFLOW_SECRET_NAME', 'CodeBuild/Metaflow')
}

dynamodb = {
    'endpoint_url': os.getenv('AWS_DYNAMODB_ENDPOINT_URL', 'http://localstack:4566'),
    'explore_topics_candidates_table': os.getenv('EXPLORE_TOPICS_CANDIDATES_TABLE', 'explore_topics_candidates')
}