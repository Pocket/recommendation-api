from typing import List

import numpy as np
from pymoo.algorithms.soo.nonconvex.ga import GA
from pymoo.core.problem import Problem
from pymoo.operators.crossover.pntx import TwoPointCrossover
from pymoo.operators.mutation.bitflip import BitflipMutation
from pymoo.operators.sampling.rnd import BinaryRandomSampling
from pymoo.optimize import minimize

from app.models.prospect_model import ProspectModel


DEFAULT_DUPLICATE_LIMIT = 2


class ArticleSelectionProblem(Problem):
    def __init__(self, articles: List[ProspectModel], n_articles=30):
        n_items = len(articles)
        self.P = np.array([a.quality_score for a in articles])

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

        self.duplicate_limit = DEFAULT_DUPLICATE_LIMIT  # Maximum duplicate topics and publishers

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


def select_articles(prospects: List[ProspectModel], n_gen=100) -> List[ProspectModel]:
    problem = ArticleSelectionProblem(prospects)
    algorithm = ArticleSelectionAlgorithm(prospects)
    res = minimize(problem, algorithm, verbose=True, termination=('n_gen', n_gen))
    return [article for article, is_selected in zip(prospects, res.X) if is_selected]
