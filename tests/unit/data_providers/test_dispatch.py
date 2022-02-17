import pytest

from app.data_providers.curation_api_client import CurationAPIFetchable
from app.data_providers.dispatch import Dispatch
from app.data_providers.slate_provider import SlateProvider, SlateProvidable, SlateSchema, ExperimentSchema
from app.models.corpus_item_model import CorpusItemModel
from app.models.ranked_corpus_items_instance import RankedCorpusItemsInstance
from app.rankers.algorithms import RankableListType, top5

class MockSlateProvider(SlateProvidable):
    def get(self, slate_id) -> SlateSchema:
        #offers up this slate regardless of the slate_id sent in. We test the SlateSchema logic in that class's tests.
        return SlateSchema(
            displayName="World's Fakest Slate",
            description="A selection of fake content for testing",
            internalDescription="We made this for our unit tests",
            experiments=[
                ExperimentSchema(
                    description="default",
                    eligible_corpora=[
                        "CHELSEAS_AWESOME_CORPUS"
                    ],
                    rankers=[
                        top5
                    ]
                )
            ]
        )

class MockCurationAPIClient(CurationAPIFetchable):
    async def get_scheduled_corpus_items(cls, corpus_id: str, start_date: str = None,
                                         user_id=None) -> RankedCorpusItemsInstance:
        return RankedCorpusItemsInstance(
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

@pytest.mark.asyncio
async def test_get_ranked_items__nominal():
    ranked_items = await Dispatch(
        api_client = MockCurationAPIClient(),
        slate_provider = MockSlateProvider()
    ).get_ranked_corpus_slate("example-corpus-id")

    # The TestSlateProvider specifies that the top5 ranker be applied.
    assert len(ranked_items) == 5

    #All the items in the return value should be CorpusItemModels
    assert all([type(item) == CorpusItemModel for item in ranked_items])

    #check the id on one cursory item
    assert ranked_items[0].id == "https://chelseatroy.com/2022/02/10/adding-error-productions-to-the-lox-compiler/"
