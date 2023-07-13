# Describes Data models that we'll provide to graphql server and fetch those data.

import graphene
from graphene_django import DjangoObjectType
from .models import ToDo

# Describing the model we want to use and the data we want collect
class typeTodo(DjangoObjectType):
    class Meta:
        model = ToDo
        fields = ("title", "description", "time")

class Query(graphene.ObjectType):
    all_Todo = graphene.List(typeTodo)

    def resolve_all_Todo(root, info):
        return ToDo.objects.all()

schema = graphene.Schema(query=Query)