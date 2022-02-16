from builtins import function

from app.rankers.algorithms import *


class ExperimentSchema:
    def __init__(
            self,
            description: str,
            candidate_sets: [str],
            rankers: [function]
    ):
        self.description = description
        self.candidate_sets = candidate_sets
        self.rankers = rankers


class SlateSchema:
    def __init__(
            self,
            displayName: str,
            description: str,
            internalDescription: str,
            experiments: [ExperimentSchema],
    ):
        self.displayName = displayName
        self.description = description
        self.internalDescription = internalDescription
        self.experiments = experiments


class SlateProvider:
    @classmethod
    def get(cls, slate_id):
        return cls.slates.get(slate_id)

    slates = {
        "f99178fb-6bd0-4fa1-8109-cda181b697f6": SlateSchema(
            displayName="New Tab Recommendations",
            description="A selection of content for display on the Firefox new tab",
            internalDescription="en-US New Tab recommendation items for today",
            experiments=[
                ExperimentSchema(
                    description="default",
                    candidate_sets=[
                        "493a5556-9800-449f-8f8c-c27bb6c8c810"
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
                    candidate_sets=[
                        "493a5556-9800-449f-8f8c-c27bb6c8c810"
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
                    candidate_sets=[
                        "493a5556-9800-449f-8f8c-c27bb6c8c810"
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
                    candidate_sets=[
                        "c66a1485-6c87-4c68-b29e-e7e838465ff7"
                    ],
                    rankers=[
                        top30,
                        firefox_thompson_sampling_1day
                    ]
                )
            ]
        )
    }
