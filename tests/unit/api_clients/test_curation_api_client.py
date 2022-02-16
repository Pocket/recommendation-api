from app.api_clients.curation_api_client import CurationAPIClient

def test_get_ranked_corpus_slate():
    try:
        CurationAPIClient.get_ranked_corpus_slate("example-corpus-id", start_date="bad-date-string")

        assert False, "Calling this method with a start_date that is not an appropriately formatted date should raise an exception"
    except:
        pass
