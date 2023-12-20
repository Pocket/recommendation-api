import json
import os

from pymoo.optimize import minimize
from pymoo.algorithms.soo.nonconvex.ga import GA

from app.config import ROOT_DIR
from app.models.prospect_model import ProspectModel
from app.rankers.new_tab_scheduler import ArticleSelectionProblem


def test_new_tab_scheduler():
    with open(os.path.join(ROOT_DIR, 'tests/assets/json/get_prospects.json')) as fp:
        data = json.load(fp)

    articles = [ProspectModel(**a) for a in data['data']['getProspects']]

    problem = ArticleSelectionProblem(articles)

    algorithm = GA(pop_size=len(articles))  # JSON fixture has 50 articles

    res = minimize(problem, algorithm, termination=('n_gen', 50))

    # Decode the solution
    selected_articles = [article for article, flag in zip(articles, res.X) if flag == 1]
    print(selected_articles)
