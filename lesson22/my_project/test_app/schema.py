import graphene
from graphene_django.types import DjangoObjectType

from .models import DataDocument


class DataDocumentType(DjangoObjectType):
    class Meta:
        model = DataDocument
        fields = '__all__'


class CreateDataDocument(graphene.Mutation):
    class Arguments:
        title = graphene.String()
        description = graphene.String()

    data_document = graphene.Field(DataDocumentType)

    def mutate(self, info, title, description):
        new_document = DataDocument(title=title, description=description)
        new_document.save()
        return CreateDataDocument(data_document=new_document)


class Query(graphene.ObjectType):
    all_data_documents = graphene.List(DataDocumentType)

    # def resolve_all_data(self, info):
    #     return DataDocument.search.execute()

    def resolve_all_data_documents(self, info):
        return DataDocument.objects.all()


class Mutation(graphene.ObjectType):
    create_data_document = CreateDataDocument.Field()

    # class Arguments:
    #     title = graphene.String()
    #     description = graphene.String()
    #
    # success = graphene.Boolean()
    #
    # def mutate(self, title, description):
    #     data = DataDocument(title=title, description=description)
    #     data.save()
    #     return Mutation(success=True)

    def resolve_create_data_document(self, title, description):
        new_document = DataDocument.objects.create(title=title, description=description)
        return new_document


schema = graphene.Schema(query=Query, mutation=Mutation)
