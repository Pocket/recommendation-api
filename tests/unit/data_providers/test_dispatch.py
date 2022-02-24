from typing import List, Any

import pytest

from app.data_providers.curation_api_client import CurationAPIFetchable
from app.data_providers.dispatch import Dispatch
from app.data_providers.metrics_client import MetricsFetchable
from app.data_providers.slate_provider import SlateProvidable
from app.data_providers.slate_provider_schemata import ExperimentSchema, SlateSchema
from app.data_providers.snowplow_client import SnowplowFetchable
from app.graphql.corpus_item import CorpusItem
from app.models.corpus_item_model import CorpusItemModel
from app.models.ranked_corpus_items_instance import RankedCorpusItemsInstance
from app.rankers.algorithms import top5, top15


class MockMetricsClient(MetricsFetchable):
    async def get_engagement_metrics(self, ranked_items, ranker):
        return {}

class MockSlateProvider(SlateProvidable):
    def __init__(self):
        self.schema = SlateSchema(displayName="World's Fakest Slate", description="A selection of fake content for testing",
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
            CorpusItemModel(id="https://chelseatroy.com/2021/09/22/critique-the-internet-and-you/"),
        ],
    )

    async def get_ranked_corpus_slate(cls, corpus_id: str, start_date: str = None,
                                         user_id=None) -> List[CorpusItem]:
        return cls.mock_corpus.corpusItems

class MockSnowplowClient(SnowplowFetchable):
    def __init__(self):
        self.event_log_call_count = 0

    async def log_event(self, user_id: int, items: [Any]) -> None:
        self.event_log_call_count += 1

@pytest.mark.asyncio
async def test_get_ranked_items__no_rankers():
    mock_curation_api_client = MockCurationAPIClient()
    ranked_items_response = await Dispatch(
        api_client=mock_curation_api_client,
        slate_provider=MockSlateProvider(),
        metrics_client=MockMetricsClient(),
        snowplow_client=MockSnowplowClient()
    ).get_ranked_corpus_slate("example-corpus-id")

    ranked_items = ranked_items_response.corpusItems
    # The TestSlateProvider specifies that the top5 ranker be applied.
    assert len(ranked_items) == 8

    # Establish order sameness
    assert [item.id for item in ranked_items] == [item.id for item in mock_curation_api_client.mock_corpus.corpusItems]

@pytest.mark.asyncio
async def test_get_ranked_items__one_item_set__one_ranker():
    mock_slate_provider = MockSlateProvider()

    #Add a ranker to the mock object
    mock_slate_provider.schema.experiments[0].rankers.append(top5)

    ranked_items_response = await Dispatch(
        api_client = MockCurationAPIClient(),
        slate_provider = mock_slate_provider,
        metrics_client=MockMetricsClient(),
        snowplow_client=MockSnowplowClient()
    ).get_ranked_corpus_slate("example-corpus-id")

    ranked_items = ranked_items_response.corpusItems

    # The TestSlateProvider specifies that the top5 ranker be applied.
    assert len(ranked_items) == 5

    #All the items in the return value should be CorpusItemModels
    assert all([type(item) == CorpusItemModel for item in ranked_items])

    #check the id on one cursory item
    assert ranked_items[0].id == "https://chelseatroy.com/2022/02/10/adding-error-productions-to-the-lox-compiler/"

@pytest.mark.asyncio
async def test_get_ranked_items__multiple_item_sets__one_ranker():
    mock_slate_provider = MockSlateProvider()

    mock_slate_provider.schema.experiments[0].eligible_corpora.append("CHELSEAS_AWESOME_CORPUS_AGAIN")
    mock_slate_provider.schema.experiments[0].rankers.append(top15)

    ranked_items_response = await Dispatch(
        api_client = MockCurationAPIClient(),
        slate_provider = mock_slate_provider,
        metrics_client=MockMetricsClient(),
        snowplow_client=MockSnowplowClient()
    ).get_ranked_corpus_slate("example-corpus-id")

    ranked_items = ranked_items_response.corpusItems

    # If the number > 15, dispatch didn't apply the top15 ranker.
    # If the number < 15, dispatch didn't fetch multiple corpora.
    assert len(ranked_items) == 15

    #All the items in the return value should be CorpusItemModels
    assert all([type(item) == CorpusItemModel for item in ranked_items])

@pytest.mark.asyncio
async def test_get_ranked_items__logs_to_snowplow():
    mock_snowplow_client = MockSnowplowClient()
    await Dispatch(
        api_client=MockCurationAPIClient(),
        slate_provider=(MockSlateProvider()),
        metrics_client=MockMetricsClient(),
        snowplow_client=mock_snowplow_client
    ).get_ranked_corpus_slate("example-corpus-id")

    assert mock_snowplow_client.event_log_call_count == 1

