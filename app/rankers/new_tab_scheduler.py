from typing import List, Dict

import numpy as np
from pymoo.algorithms.soo.nonconvex.ga import BGA
from pymoo.core.problem import Problem
from pymoo.operators.crossover.pntx import TwoPointCrossover, PointCrossover
from pymoo.optimize import minimize

from app.models.prospect_model import ProspectModel


class ArticleSelectionProblem(Problem):
    def __init__(
            self,
            articles: List[ProspectModel],
            topic_duplicate_limits: Dict[str, int],
            topic_duplicate_limit_fallback: int,
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
        self.duplicate_limit = np.array(
            [topic_duplicate_limits.get(topic, topic_duplicate_limit_fallback) for topic in all_topics] +
            [publisher_duplicate_limit] * len(all_publishers)
        )

        super().__init__(n_var=n_items, n_obj=1, n_ieq_constr=n_constraints, xl=0, xu=1, vtype=bool)

    def _evaluate(self, x, out, *args, **kwargs):
        """
        @param x: Numpy array with shape (pop_size, n_var). This is a batch of potential solutions to be evaluated.
        @param out["F"]: cost function values of shape (pop_size,)
        @param out["G"]: constraint value array of shape (pop_size, n_constraints)
        """
        out["F"] = -np.sum(self.P * x, axis=1)
        out["G"] = np.dot(x, self.W) - self.duplicate_limit


class SchedulingGA(BGA):
    def __init__(self):
        super().__init__(
            pop_size=50,
            crossover=PointCrossover(n_points=2),
        )


DEFAULT_TOPIC_LIMITS = {
    'ENTERTAINMENT': 5,
    'FOOD': 5,
    'SCIENCE': 4,
    'HEALTH_FITNESS': 4,
    'SELF_IMPROVEMENT': 4,
    'EDUCATION': 3,
    'POLITICS': 3,
    'TECHNOLOGY': 2,
    'PERSONAL_FINANCE': 2,
    'BUSINESS': 2,
    'CAREER': 2,
    'TRAVEL': 2,
    'PARENTING': 2,
    'SPORTS': 1,
}


def select_articles(
        prospects: List[ProspectModel],
        topic_duplicate_limits=None,
        topic_duplicate_limit_fallback: int = 2,
        publisher_duplicate_limit: int = 2,
        n_gen: int = 100,
) -> List[ProspectModel]:
    """
    @param topic_duplicate_limits: Dictionary of maximum number of items with the same topics to select
    @param topic_duplicate_limit_fallback: Fallback maximum number duplicate topics, for topics not present in the dict
    @param publisher_duplicate_limit: Maximum number of items to select with the same publisher
    @param prospects: List of all available candidate items
    @param n_gen: Number of generations
    @return: a subset of prospects optimized for quality_score sum, with constraints on duplicate topics and publishers.
    """
    if topic_duplicate_limits is None:
        topic_duplicate_limits = DEFAULT_TOPIC_LIMITS

    problem = ArticleSelectionProblem(
        prospects,
        topic_duplicate_limits=topic_duplicate_limits,
        topic_duplicate_limit_fallback=topic_duplicate_limit_fallback,
        publisher_duplicate_limit=publisher_duplicate_limit,
    )
    algorithm = SchedulingGA()
    res = minimize(problem, algorithm, verbose=True, termination=('n_gen', n_gen))
    return [article for article, x in zip(prospects, res.X) if float(x) > 0.5]
