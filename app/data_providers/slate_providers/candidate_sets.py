from app.models.localemodel import LocaleModel

# Map Corpus topic (keys) to the Corpus candidate set id (values).
# TODO: Instead of hardcoding these values, consider moving them to the Sagemaker Feature Store, or a database.
_TOPIC_CANDIDATE_SETS = {
    # SELECT
    #     corpus_topic_id as "CORPUS_TOPIC_ID",
    #     curated_corpus_candidate_set_id as "CORPUS_CANDIDATE_SET_ID"
    # FROM analytics.dbt.static_corpus_candidate_set_topics;
    LocaleModel.en_US: {
        'SELF_IMPROVEMENT': '78f23805-66e7-46d5-9cfc-ff10a0335265',
        'POLITICS': '0a024f6e-b7e7-4be2-bc86-b603c26fc351',
        'BUSINESS': 'dd57c71e-049e-4f3a-b003-9d44d693d8c4',
        'HEALTH_FITNESS': 'ec9cd333-b136-419e-a091-d1f9ae573f27',
        'SCIENCE': 'cdc738bb-bf71-4794-b95f-cf4e0ea77572',
        'PARENTING': 'b09945d0-b211-44e6-afc8-c3f44997937d',
        'EDUCATION': '30a4f4e6-f4ec-4c8a-99f7-d75c147539ec',
        'CORONAVIRUS': '7d5b18b4-417d-47a5-8e55-a53ab7edea7b',
        'TECHNOLOGY': '2c657e89-3690-47fb-b08f-7930a87211c0',
        'FOOD': '952c8207-0112-46bc-ad06-a2d2c0163422',
        'ENTERTAINMENT': '079b190b-ad77-4be9-bf87-7261416c909e',
        'PERSONAL_FINANCE': '5e30b37b-e167-43a0-ac12-8c7b2cc78599',
        'CAREER': 'c5b8933f-83b5-4867-95af-9a025fe69115',
        'TRAVEL': 'e062d6dc-3fb9-4bbd-8ff4-6728a2054ffb',
        'SPORTS': '6f3ed598-0720-471a-bffc-3021aab2464c',
        'GAMING': '465cadb7-638d-41b7-8914-3d6c42f53b57',
    },
    # SELECT
    #     corpus_topic_id as "CORPUS_TOPIC_ID",
    #     german_curated_corpus_candidate_set_id as "CORPUS_CANDIDATE_SET_ID"
    # FROM analytics.dbt.static_corpus_candidate_set_topics;
    LocaleModel.de_DE: {
        'BUSINESS': 'c6a5ce54-5382-4a7a-be89-40c694196d66',
        'CAREER': '090c7706-c596-4302-ac0f-42093f0e04dc',
        'CORONAVIRUS': '5aceef18-7dbf-43ad-bfd3-a519dba41bee',
        'EDUCATION': 'ea554ee5-5da6-41bc-86c5-1bccb009d158',
        'ENTERTAINMENT': '0d902fea-7bf2-470e-a8a7-781259757111',
        'FOOD': '52dd9f6d-d543-473b-8865-5f60ca32ccf9',
        'GAMING': 'a12d7d55-6b94-4815-acda-d5299696525c',
        'HEALTH_FITNESS': '19444382-e666-4339-b6c3-d8bceadecd20',
        'PARENTING': '53f02075-3331-49d9-b8c8-72e89291a79e',
        'PERSONAL_FINANCE': '015d631b-a718-45d8-9d35-55556a611ac0',
        'POLITICS': '2e9a5251-40a0-4202-ae7b-83dee19b92cf',
        'SCIENCE': '785730ff-442d-4d2b-881a-64b01e97585c',
        'SELF_IMPROVEMENT': '8d2da3af-0ba2-4b9b-836f-a878e081ea5d',
        'SPORTS': '3d427dc4-e741-41e1-b577-710d2bfa584f',
        'TECHNOLOGY': '9951fc34-4f66-4838-88f2-b4e0435f6e29',
        'TRAVEL': '280c14b0-4afb-49d0-b7a5-7a1b156b0c7d',
    }
}


def get_topic_candidate_set(corpus_topic_id: str, locale: LocaleModel) -> str:
    """
    This function encapsulates the topic to candidate set mapping, such that we can move this to a data store,
    without requiring changes to callers.
    :param corpus_topic_id: E.g. 'BUSINESS'
    :param locale: E.g. LocaleModel.en_US
    :return: Corpus candidate set for the given topic and locale
    """
    return _TOPIC_CANDIDATE_SETS[locale][corpus_topic_id]
