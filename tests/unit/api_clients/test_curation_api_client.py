from app.data_providers.corpus.curated_corpus_api_client import CuratedCorpusAPIClient


def test_get_ranked_corpus_items():
    try:
        CuratedCorpusAPIClient.get_ranked_corpus_items("example-corpus-id", start_date="bad-date-string")

        assert False, "Calling this method with a start_date that is not an appropriately formatted date should raise an exception"
    except:
        pass
