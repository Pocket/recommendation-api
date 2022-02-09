import uuid

from app.models.corpus_slate_instance import CorpusSlateInstance

class CurationAPIClient(object):
    @classmethod
    async def get_corpus_slate(cls, corpus_slate_id, user_id=None):
        return CorpusSlateInstance(
            id=str(uuid.UUID(int=sum([ord(char) for char in "IAmTheWalrus"]))),
            description="I am the corpus slate, coo coo ca choo",
            recommendations = [],
        )