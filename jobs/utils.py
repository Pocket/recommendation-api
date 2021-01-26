import logging
import sys
import os

from metaflow import namespace, Flow


def setup_logger():
    root = logging.getLogger()
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.INFO)
    ch.setFormatter(
        logging.Formatter(
            '{ "time": "%(asctime)s", "name": "%(name)s", "level": "%(levelname)s", "message": %(message)s }'
        )
    )
    root.setLevel(logging.DEBUG)
    root.addHandler(ch)


def convert_to_days(scale: str) -> str:
    """
    convert time window string from weeks to days as needed for ES queries
    :param scale: input time window string in days or weeks
    :return: time window string in days
    """
    if _check_timescale(scale, 'w'):
        scale2 = '%dd' % (int(scale.partition('w')[0]) * 7)
    elif _check_timescale(scale, 'd'):
        scale2 = scale
    else:
        raise ('{} is not a valid time range'.format(scale))
    return scale2


def _check_timescale(qstr: str, splitter: str = "w") -> bool:
    """
    this routine checks to see if timescale is in weeks
    :param qstr: the timescale string
    :param splitter: "w" splits on weeks
    :return: boolean indicating if timescale is in units determined by qstr
    """
    return qstr.partition(splitter)[0].isdigit() and qstr.partition(splitter)[1] == splitter


def elasticsearch_connect(es_endpoint: str):
    """
    this routine establishes a connection to elasticsearch and returns the client
    :param flowname: this is the name of the flow and is used for logging
    :param es_endpoint: this is the URL for the elasticsearch cluster
    :return: elasticsearch client for subsequent queries
    """
    # metaflow imports by step, thus they appear below
    import boto3
    from elasticsearch import Elasticsearch, RequestsHttpConnection
    from requests_aws4auth import AWS4Auth

    session = boto3.Session()
    credentials = session.get_credentials()
    region = os.environ.get('AWS_REGION', 'us-east-1')
    awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, region, "es",
                       session_token=credentials.token)
    es = Elasticsearch(
        hosts=[{'host': es_endpoint, 'port': 443}],
        http_auth=awsauth,
        use_ssl=True,
        verify_certs=True,
        connection_class=RequestsHttpConnection
    )

    return es


def load_generic_approval_ranker(model_training_flow: str = "ExploreTopicTrainingFlow"):
    """
    this routine loads the generic approval model trained in the ExploreTopicTrainingFlow
    :param model_training_flow: this string identifies the flow that generated the desired model
    :return: the run_id for the model, the featurizer, and the model

    Here we need to change the namespace to the production one of the corresponding model we are looking to pull
    Once https://github.com/Netflix/metaflow/issues/384 is merged and the topic model training has the right tags
    added we will be able to change this to just "production" and pull it from AWS Secrets Manager
    """
    namespace("production:exploretopictrainingflow-0-eins")

    training_run = Flow(model_training_flow).latest_successful_run
    model_run_id = training_run.id
    # get vectorizer, one hot mappings for google categories and domains
    featurizer = training_run.data.featurizer

    # get generic approval model
    approval_model = training_run.data.generic_classifier

    return model_run_id, featurizer, approval_model


def query_elasticsearch(es_query, score_fcns, domain_allowlist, es_client, es_path,
                        topic_predictor, approval_model, featurizer, approval_threshold,
                        limit, min_score=0.01):
    """
    this routine issues function score queries to elasticsearch
    :param es_query:
    :param score_fcns:
    :param domain_allowlist:
    :param es_client:
    :param es_path:
    :param topic_predictor:
    :param approval_model:
    :param featurizer:
    :param approval_threshold:
    :param limit:
    :param min_score:
    :return:
    """

    from elasticsearch_dsl import Search
    from elasticsearch.exceptions import NotFoundError, RequestError, AuthorizationException
    from query import postprocess_search_results
    from ranking import apply_rankers

    logger = logging.getLogger()
    try:
        s = Search(using=es_client, index=es_path).query("function_score",
                                                         query=es_query,
                                                         min_score=min_score,
                                                         functions=score_fcns)

        # get extra results in case some are duplicates or filtered downstream
        total = min(900, limit * 9)
        s = s[:total]
        search_results = postprocess_search_results(s.execute().to_dict(),
                                                         domain_allowlist,
                                                         limit * 6)

    except (NotFoundError, RequestError, AuthorizationException) as err:
        logger.error("ElasticSearch " + str(err))
        sys.exit(1)

    logger.info("Metaflow says its time to get apply ranking models to elasticsearch results")
    results = apply_rankers(search_results,
                            topic_predictor=topic_predictor,
                            approval_model=approval_model,
                            count=limit,
                            featurizer=featurizer,
                            approval_percentile=approval_threshold)

    return results
