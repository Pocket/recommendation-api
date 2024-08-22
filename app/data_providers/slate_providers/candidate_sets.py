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
    },
    # SELECT CONCAT ('\'', corpus_topic_id, '\' : \'', en_gb_curated_corpus_candidate_set_id, '\',') as data
    # FROM analytics.dbt.static_corpus_candidate_set_topics
    LocaleModel.en_GB: {
        'BUSINESS': 'f24c8da6-11d1-40de-9bf7-27dfde0bed9f',
        'CAREER': 'c2ba50c4-28ae-4bd6-8e07-4b10d2d9bfd6',
        'EDUCATION': 'c49d8d9f-84c8-453b-bb76-46519ba37946',
        'ENTERTAINMENT': 'b8368984-5d69-4d93-947d-d86f11619c3d',
        'FOOD': '6b49125e-8384-4b36-9387-dcda8245f587',
        'GAMING': '268640e4-cebb-44f3-9814-cef8b596671c',
        'HEALTH_FITNESS': 'db740131-bf6d-449a-bd86-4be846d30e36',
        'PARENTING': 'f651806a-12bc-40b4-b1c3-afc63054de04',
        'PERSONAL_FINANCE': '2db6556b-2270-43bb-9bc5-f4daaf72a36b',
        'POLITICS': 'd82898b3-5f7f-466a-b283-d5bfa2958f17',
        'SCIENCE': '963d5c09-052a-4649-8d36-097766de068f',
        'SELF_IMPROVEMENT': '5d8e5764-77d7-4686-887e-84aaddcf482c',
        'SPORTS': '13bba6bd-34a6-499e-97eb-deb67f429474',
        'TECHNOLOGY': 'b0d0c28b-a2b4-4142-ac5b-8f2ac69766eb',
        'TRAVEL': '99b26208-8740-448e-bc2c-3e781e04b941',
    },
    # SELECT CONCAT ('\'', corpus_topic_id, '\' : \'', fr_fr_curated_corpus_candidate_set_id, '\',') as data
    # FROM analytics.dbt.static_corpus_candidate_set_topics
    LocaleModel.fr_FR: {
        'BUSINESS': 'd2a31a31-3498-4f0a-8ca3-fbd29ed7c6c2',
        'CAREER': '80c0d34c-4fa7-432f-844f-49a52e6fbb0e',
        'EDUCATION': 'e609b611-da19-43ea-b1a9-233af9859176',
        'ENTERTAINMENT': '4768e9c7-3f04-42a1-b68d-818f08aace84',
        'FOOD': 'd21dce45-ac82-4e47-929d-26aaf7526279',
        'GAMING': 'a4981bde-2079-4f02-876d-770ff557112b',
        'HEALTH_FITNESS': 'ed0e007b-d9b6-47ed-9013-fefd71698092',
        'PARENTING': '15d1fbae-b17d-4174-a1d3-9f02f41c1e8b',
        'PERSONAL_FINANCE': '5e251580-eb76-47de-b994-6bb7251a82e1',
        'POLITICS': '2bd21444-99cb-49dd-b356-0ec34ba6fd47',
        'SCIENCE': 'c8e5f613-161f-411b-bb13-b3a590cae80c',
        'SELF_IMPROVEMENT': 'd77168b1-68a9-4942-91ea-bed18defca02',
        'SPORTS': 'd1351bc2-9dfa-45db-b5a1-f7c7a85f296b',
        'TECHNOLOGY': '19a95471-02b4-4133-81e6-21a7e66b247d',
        'TRAVEL': '90a3e2a3-3191-4bef-a7f9-1b2aa6f56030',
    },
    # SELECT CONCAT ('\'', corpus_topic_id, '\' : \'', it_it_curated_corpus_candidate_set_id, '\',') as data
    # FROM analytics.dbt.static_corpus_candidate_set_topics
    LocaleModel.it_IT: {
        'BUSINESS': 'ce8b6f8e-e5cc-4c1f-a280-32556a6ab902',
        'CAREER': '7654d4bf-8cc7-4bf5-b717-8d0afa704beb',
        'EDUCATION': '102fc018-60ff-4a53-9b99-ec6ceee55f71',
        'ENTERTAINMENT': '278d95d7-f80b-47cc-a677-55513da93c2b',
        'FOOD': '2d098837-fc18-4e31-82c0-ec6bb8f8e7bf',
        'GAMING': 'ae3ac966-006d-4a75-9dde-6746169db95b',
        'HEALTH_FITNESS': 'd58149b8-efe7-4bd0-914b-326ee034957b',
        'PARENTING': '5f60193e-b120-4043-a693-2905c8f51b9e',
        'PERSONAL_FINANCE': '24dc05ed-8714-44a5-8daf-62f46fafecf1',
        'POLITICS': '426e9110-4ee0-4b4d-98fd-4a30f4304a63',
        'SCIENCE': 'dbc6fbd2-6c2e-4bb2-98f5-fccc3b05835a',
        'SELF_IMPROVEMENT': 'a91654c2-b78d-4377-90ea-4f1252ff60c9',
        'SPORTS': 'd6b548d8-c85c-46e5-8464-7d395e517fe3',
        'TECHNOLOGY': '052eb916-b15e-480e-b9f8-b06bc8070b15',
        'TRAVEL': '3473fe06-99ba-40f2-92d6-fc36685dafd0',
    },
    # SELECT CONCAT ('\'', corpus_topic_id, '\' : \'', es_es_curated_corpus_candidate_set_id, '\',') as data
    # FROM analytics.dbt.static_corpus_candidate_set_topics
    LocaleModel.es_ES: {
        'BUSINESS': 'e6e1696e-571a-49a6-ac27-1de508fc1f31',
        'CAREER': '4aede29c-594e-4c59-8c80-f84c01d5c670',
        'EDUCATION': '8372ee9e-a221-4029-91e0-bd5e34e241a0',
        'ENTERTAINMENT': 'f0218221-f260-4e64-a1bb-f3baf4b4d133',
        'FOOD': '3d633b51-bbe8-4ff4-8d7a-779039a5ac79',
        'GAMING': 'b663fb9e-3ace-493c-a475-d9e3747f119f',
        'HEALTH_FITNESS': '60da1c2b-d850-487e-ae79-90dedb1998fb',
        'PARENTING': '395878cd-8351-4ec0-ac49-2195097e6c01',
        'PERSONAL_FINANCE': '1815defc-c91c-485d-961e-20af48ec0c57',
        'POLITICS': 'ae07cb40-f248-41e2-ba7b-e4059caaa1b6',
        'SCIENCE': 'bd983eba-0b4a-4916-82dd-d3a212ce934b',
        'SELF_IMPROVEMENT': 'b3c241b0-3651-4460-977c-568cbfbef2c3',
        'SPORTS': '85164fb5-2025-42c3-b669-08aff1f86d08',
        'TECHNOLOGY': '177d3d8d-7733-402d-bf76-39eb9c2e24cd',
        'TRAVEL': '79eb69a2-e1e1-453c-b319-35f82cbbb799',
    }
}


def get_topic_candidate_set_id(corpus_topic_id: str, locale: LocaleModel) -> str:
    """
    This function encapsulates the topic to candidate set mapping, such that we can move this to a data store,
    without requiring changes to callers.
    :param corpus_topic_id: E.g. 'BUSINESS'
    :param locale: E.g. LocaleModel.en_US
    :return: Corpus candidate set for the given topic and locale
    """
    return _TOPIC_CANDIDATE_SETS[locale][corpus_topic_id]
