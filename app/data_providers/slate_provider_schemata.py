from typing import Callable, Any, List

from app.graphql.corpus_item import CorpusItem

class ExperimentSchema:
    def __init__(
            self,
            description: str,
            eligible_corpora: [str],
            rankers: [Callable[[Any], List['CorpusItem']]]
    ):
        self.description = description
        self.eligible_corpora = eligible_corpora
        self.rankers = rankers

    def corpus_ids(self):
        return [c for c in self.eligible_corpora]


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
