from abc import ABC, abstractmethod

from app.data_providers.corpus.corpus_feature_group_client import CorpusFeatureGroupClient
from app.data_providers.slate_provider_schemata import SlateSchema
from app.rankers.algorithms import *

class SlateProvidable(ABC):
    @abstractmethod
    def get(self, slate_id) -> SlateSchema:
        return NotImplemented

class InvalidIdError(Exception):
    message = "No Slate Schema with that id!"

class SlateProvider:
    def get(self, slate_id):
        slate_schema = self.slates.get(slate_id)
        if not slate_schema:
            raise InvalidIdError
        return slate_schema

    slates = {
        "f99178fb-6bd0-4fa1-8109-cda181b697f6": SlateSchema(
            displayName="New Tab Recommendations",
            description="A selection of content for display on the Firefox new tab",
            internalDescription="en-US New Tab recommendation items for today",
            experiments=[
                ExperimentSchema(
                    description="default",
                    eligible_corpora=[
                        "NEW_TAB_EN_US"
                    ],
                    rankers=[
                        top30,
                        firefox_thompson_sampling_1day
                    ]
                )
            ]
        ),
        "f4c3076c-2184-44ac-9272-0e7387f88fa6": SlateSchema(
            displayName="New Tab Recommendations",
            description="A selection of content for display on the Firefox new tab",
            internalDescription="en-GB New Tab recommendation items for today",
            experiments=[
                ExperimentSchema(
                    description="default",
                    eligible_corpora=[
                        "NEW_TAB_EN_GB"
                    ],
                    rankers=[
                        top30,
                        firefox_thompson_sampling_1day
                    ]
                )
            ]
        ),
        "d9b55d46-f909-43a2-876c-30784e90093a": SlateSchema(
            displayName="New Tab Recommendations",
            description="A selection of content for display on the Firefox new tab",
            internalDescription="en-INTL New Tab recommendation items for today",
            experiments=[
                ExperimentSchema(
                    description="default",
                    eligible_corpora=[
                        "NEW_TAB_EN_INTL"
                    ],
                    rankers=[
                        top30,
                        firefox_thompson_sampling_1day
                    ]
                )
            ]
        ),
        "79655eb2-47a1-4a26-9235-29e4768ff0a1": SlateSchema(
            displayName="New Tab Recommendations",
            description="A selection of content for display on the Firefox new tab",
            internalDescription="de-DE New Tab recommendation items for today",
            experiments=[
                ExperimentSchema(
                    description="default",
                    eligible_corpora=[
                        "NEW_TAB_DE_DE"
                    ],
                    rankers=[
                        top30,
                        firefox_thompson_sampling_1day
                    ]
                )
            ]
        ),
        "2d6bd5a3-fbd5-454c-9eac-cd39780b18fc": SlateSchema(
            displayName="Save an article you find interesting",
            description="Save one article",
            internalDescription="Stories shown during Setup Moment onboarding",
            experiments=[
                ExperimentSchema(
                    description="default",
                    eligible_corpora=[
                        CorpusFeatureGroupClient.SETUP_MOMENT_CORPUS_CANDIDATE_SET_ID,
                    ],
                    rankers=[
                        top30,
                    ]
                )
            ]
        )
    }
