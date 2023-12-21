from typing import List

import numpy as np
from pymoo.algorithms.soo.nonconvex.ga import GA
from pymoo.core.problem import Problem
from pymoo.operators.crossover.pntx import TwoPointCrossover
from pymoo.operators.mutation.bitflip import BitflipMutation
from pymoo.operators.sampling.rnd import BinaryRandomSampling
from pymoo.optimize import minimize

from app.models.prospect_model import ProspectModel


class ArticleSelectionProblem(Problem):
    def __init__(
            self,
            articles: List[ProspectModel],
            topic_duplicate_limit: int,
            publisher_duplicate_limit: int
    ):
        n_items = len(articles)
        self.P = np.array([a.quality_score for a in articles])  # profit

        all_topics = sorted({a.topic for a in articles})
        all_publishers = sorted({a.publisher for a in articles})

        # Create topic matrix
        topic_matrix = np.zeros((n_items, len(all_topics)))
        for i, article in enumerate(articles):
            topic_index = all_topics.index(article.topic)
            topic_matrix[i, topic_index] = 1

        # Create publisher matrix
        publisher_matrix = np.zeros((n_items, len(all_publishers)))
        for i, article in enumerate(articles):
            publisher_index = all_publishers.index(article.publisher)
            publisher_matrix[i, publisher_index] = 1

        # Concatenate topic and publisher matrices
        self.W = np.hstack((topic_matrix, publisher_matrix))
        n_constraints = self.W.shape[1]  # equal to len(all_topics) + len(all_publishers)

        # Create a vector for duplicate limits
        self.duplicate_limit = np.array([topic_duplicate_limit] * len(all_topics) +
                                        [publisher_duplicate_limit] * len(all_publishers))

        super().__init__(n_var=n_items, n_obj=1, n_ieq_constr=n_constraints, xl=0, xu=1, vtype=bool)

    def _evaluate(self, x, out, *args, **kwargs):
        out["F"] = -np.sum(self.P * x, axis=1)
        out["G"] = np.dot(x, self.W) - self.duplicate_limit


class ArticleSelectionAlgorithm(GA):
    def __init__(self, articles):
        super().__init__(
            pop_size=len(articles),
            sampling=BinaryRandomSampling(),
            crossover=TwoPointCrossover(),
            mutation=BitflipMutation(),
            eliminate_duplicates=True)


def select_articles(
        prospects: List[ProspectModel],
        topic_duplicate_limit: int = 2,
        publisher_duplicate_limit: int = 2,
        n_gen: int = 100,
) -> List[ProspectModel]:
    """
    @param topic_duplicate_limit: Maximum number of items to select with the same topic
    @param publisher_duplicate_limit: Maximum number of items to select with the same publisher
    @param prospects: List of all available candidate items
    @param n_gen: Number of generations
    @return: a subset of prospects optimized for quality_score sum, with constraints on duplicate topics and publishers.
    """
    problem = ArticleSelectionProblem(
        prospects,
        topic_duplicate_limit=topic_duplicate_limit,
        publisher_duplicate_limit=publisher_duplicate_limit,
    )
    algorithm = ArticleSelectionAlgorithm(prospects)
    res = minimize(problem, algorithm, verbose=True, termination=('n_gen', n_gen))
    return [article for article, is_selected in zip(prospects, res.X) if is_selected]
