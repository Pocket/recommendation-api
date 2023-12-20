from pymoo.core.problem import ElementwiseProblem


class ArticleSelectionProblem(ElementwiseProblem):
    def __init__(self, articles, n_articles=30):
        super().__init__(n_var=len(articles), n_obj=1, n_constr=1 + 2 * len(set([a.topic for a in articles])))
        self.articles = articles
        self.n_articles = n_articles

    def _evaluate(self, x, out, *args, **kwargs):
        selected_articles = [article for article, flag in zip(self.articles, x) if flag == 1]

        # Objective: Maximize total quality score
        total_quality_score = sum(article.quality_score for article in selected_articles)
        out["F"] = -total_quality_score  # Negative because we want to maximize

        # Constraints
        topic_count = {}
        publisher_count = {}
        for article in selected_articles:
            topic_count[article.topic] = topic_count.get(article.topic, 0) + 1
            publisher_count[article.publisher] = publisher_count.get(article.publisher, 0) + 1

        # Constraint: No more than 2 articles from the same topic or publisher
        topic_constraints = [count - 2 for count in topic_count.values()]
        publisher_constraints = [count - 2 for count in publisher_count.values()]

        # Constraint: Exactly 30 articles
        article_count_constraint = [len(selected_articles) - self.n_articles]

        out["G"] = topic_constraints + publisher_constraints + article_count_constraint
