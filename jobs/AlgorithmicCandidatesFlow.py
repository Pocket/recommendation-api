from metaflow import FlowSpec, step, Parameter

class AlgorithmicCanidatesFlow(FlowSpec):

    topic = Parameter('topic',
                      help="Filter a particular topic",
                      default='finance')

    recommendations = Parameter('recommendations',
                                help="The number of items to recommend in "
                                     "the topic.",
                                default=5)

    """
    A flow where Metaflow prints 'Hi'.
    Run this flow to validate that Metaflow is installed correctly.
    """
    @step
    def start(self):
        """
        This is the 'start' step. All flows must have a step named 'start' that
        is the first step in the flow.
        """
        print("AlgorithmicCanidatesFlow is starting.")
        self.next(self.hello)

    @step
    def hello(self):
        """
        A step for metaflow to introduce itself.
        """
        print("Metaflow says: Hi!")
        self.next(self.end)

    @step
    def end(self):
        """
        This is the 'end' step. All flows must have an 'end' step, which is the
        last step in the flow.
        """
        print("AlgorithmicCanidatesFlow is all done.")


if __name__ == '__main__':
    AlgorithmicCanidatesFlow()