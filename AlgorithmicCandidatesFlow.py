from metaflow import FlowSpec, step, Parameter, schedule

@schedule(hourly=True)
class AlgorithmicCandidatesFlow(FlowSpec):
    recommendations = Parameter('recommendations',
                                help="The number of items to recommend in "
                                     "the topic.",
                                default=5)

    """
    A flow where Metaflow generates algorithmic candidates.
    """
    @step
    def start(self):
        """
        This is the 'start' step. All flows must have a step named 'start' that
        is the first step in the flow.
        """
        print("AlgorithmicCandidatesFlow is starting.")
        # TODO: Grab topics from the api
        self.topics = ['Business',
                       'Finance',
                       'Health']
        self.next(self.get_query, foreach='topics')

    @step
    def get_query(self):
        """
        A step for metaflow to get the topic query
        """
        self.topic = self.input

        # TODO: Get the query for each topic from the api to use
        # TODO: Hit Elasticsearch?
        print("Metaflow says its time to get the query for: ", self.topic)

        self.next(self.hit_elasticsearch)

    @step
    def hit_elasticsearch(self):
        """
        A step for metaflow to hit elasticsearch
        """

        # TODO: Hit Elasticsearch?
        print("Metaflow says its time to get some elasticsearch results for: ", self.topic)

        self.next(self.generate_candidates)

    @step
    def generate_candidates(self):
        """
        A step for metaflow to generate candidates from a model
        """

        # TODO: Pull the model from the metaflow_client
        # TODO: use the model!
        print("Metaflow says its time to generate candidates for", self.topic, "with", self.recommendations, "recs")

        self.next(self.join)

    @step
    def join(self, inputs):
        self.results = [input.topic for input in inputs]
        print("Metaflow says its time to join the results for: ", self.results)
        # TODO: Dump these results
        self.next(self.end)

    @step
    def end(self):
        """
        This is the 'end' step. All flows must have an 'end' step, which is the
        last step in the flow.
        """
        print("AlgorithmicCanidatesFlow is all done.")


if __name__ == '__main__':
    AlgorithmicCandidatesFlow()
