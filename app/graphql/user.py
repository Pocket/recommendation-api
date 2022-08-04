import graphene

from graphene_federation import external, extend


@extend(fields='id')
class User(graphene.ObjectType):
    id = external(graphene.ID(required=True))
    rec_name = graphene.String(required=True)

    def __resolve_reference(self, info, **kwargs):
        return User(id=self.id, rec_name=f'user_{self.id}')

