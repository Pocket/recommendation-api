import graphene

from app.graphql.topic import Topic
from app.graphql.update_user_content_profile_input import UpdateUserContentProfileInput
from app.models.topic import TopicModel


class UpdateUserContentProfile(graphene.Mutation):
    class Arguments:
        input = UpdateUserContentProfileInput(required=True)

    preferred_topics = graphene.List(Topic, description="Topics that the user expressed interest in")

    async def mutate(root, info, input):
        topics = await TopicModel.get_all()
        input_topic_ids = {t.id for t in input.preferredTopics}
        output_topics = [t for t in topics if t.id in input_topic_ids]

        return UpdateUserContentProfile(preferred_topics=output_topics)
