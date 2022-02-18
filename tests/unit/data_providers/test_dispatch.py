from typing import List

import pytest

from app.data_providers.curation_api_client import CurationAPIFetchable
from app.data_providers.dispatch import Dispatch
from app.data_providers.metrics_client import MetricsFetchable
from app.data_providers.slate_provider import SlateProvider, SlateProvidable
from app.data_providers.slate_provider_schemata import ExperimentSchema, SlateSchema
from app.graphql.corpus_item import CorpusItem
from app.models.corpus_item_model import CorpusItemModel
from app.models.ranked_corpus_items_instance import RankedCorpusItemsInstance
from app.rankers.algorithms import top5

class MockMetricsClient(MetricsFetchable):
    async def get_engagement_metrics(self, ranked_items, ranker):
        return {}

class MockSlateProvider(SlateProvidable):
    schema = SlateSchema(displayName="World's Fakest Slate", description="A selection of fake content for testing",
                         internalDescription="We made this for our unit tests", experiments=[
            ExperimentSchema(description="default", eligible_corpora=["CHELSEAS_AWESOME_CORPUS"], rankers=[])])

    def get(self, slate_id) -> SlateSchema:
        #offers up this slate regardless of the slate_id sent in. We test the SlateSchema logic in that class's tests.
        return self.schema

class MockCurationAPIClient(CurationAPIFetchable):
    mock_corpus = RankedCorpusItemsInstance(
        id="CHELSEAS_AWESOME_CORPUS",
        description="I mean, pretty sure the id covers it ;)",
        corpusItems=[
            CorpusItemModel(id="https://chelseatroy.com/2022/02/10/adding-error-productions-to-the-lox-compiler/"),
            CorpusItemModel(id="https://chelseatroy.com/2022/01/02/emulating-objects-in-functionally-oriented-languages-the-real-midwives-of-haskell/"),
            CorpusItemModel(id="https://chelseatroy.com/2022/01/31/deployment-security-for-android-and-ios/"),
            CorpusItemModel(id="https://chelseatroy.com/2021/12/10/notes-and-illustrations-grokking-machine-learning/"),
            CorpusItemModel(id="https://chelseatroy.com/2021/11/10/rubyconf-2021-workshop-tackling-technical-debt-an-analytical-approach/"),
            CorpusItemModel(id="https://chelseatroy.com/2021/10/29/a-rubric-for-evaluating-team-members-contributions-to-a-maintainable-code-base/"),
            CorpusItemModel(id="https://chelseatroy.com/2021/09/14/the-art-of-documentation/"),
        ],
    )

    async def get_ranked_corpus_slate(cls, corpus_id: str, start_date: str = None,
                                         user_id=None) -> List[CorpusItem]:
        return cls.mock_corpus.corpusItems

@pytest.mark.asyncio
async def test_get_ranked_items__no_rankers():
    mock_curation_api_client = MockCurationAPIClient()
    ranked_items_response = await Dispatch(
        api_client=mock_curation_api_client,
        slate_provider=MockSlateProvider(),
        metrics_client=MockMetricsClient()
    ).get_ranked_corpus_slate("example-corpus-id")

    ranked_items = ranked_items_response.corpusItems
    # The TestSlateProvider specifies that the top5 ranker be applied.
    assert len(ranked_items) == 7

    # Establish order sameness
    assert [item.id for item in ranked_items] == [item.id for item in mock_curation_api_client.mock_corpus.corpusItems]

@pytest.mark.asyncio
async def test_get_ranked_items__nominal():
    mock_slate_provider = MockSlateProvider()

    #Add a ranker to the mock object
    mock_slate_provider.schema.experiments[0].rankers.append(top5)

    ranked_items_response = await Dispatch(
        api_client = MockCurationAPIClient(),
        slate_provider = mock_slate_provider,
        metrics_client=MockMetricsClient()
    ).get_ranked_corpus_slate("example-corpus-id")

    ranked_items = ranked_items_response.corpusItems

    # The TestSlateProvider specifies that the top5 ranker be applied.
    assert len(ranked_items) == 5

    #All the items in the return value should be CorpusItemModels
    assert all([type(item) == CorpusItemModel for item in ranked_items])

    #check the id on one cursory item
    assert ranked_items[0].id == "https://chelseatroy.com/2022/02/10/adding-error-productions-to-the-lox-compiler/"
