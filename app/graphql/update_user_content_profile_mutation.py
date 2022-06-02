import graphene

from app.graphql.topic import Topic
from app.graphql.topic_input import TopicInput
from app.models.topic import TopicModel


class UpdateUserContentProfile(graphene.Mutation):
    class Arguments:
        preferredTopics = graphene.List(
            TopicInput,
            required=True,
            description="Topics that the user expressed interest in"
        )

    preferred_topics = graphene.List(Topic, description="Topics that the user expressed interest in")

    async def mutate(root, info, preferredTopics):
        topics = await TopicModel.get_all()
        input_topic_ids = {t.id for t in preferredTopics}
        output_topics = [t for t in topics if t.id in input_topic_ids]

        return UpdateUserContentProfile(preferred_topics=output_topics)
