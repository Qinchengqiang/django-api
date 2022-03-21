import graphene

from graphene_django import DjangoObjectType, DjangoListField
from .models import Person, Address


class PersonType(DjangoObjectType):
    class Meta:
        model = Person
        fields = ("id", "name", "email", "address")


class AddressType(DjangoObjectType):
    class Meta:
        model = Address
        fields = ("id", "number", "street", "city", "state", "persons")


class Query(graphene.ObjectType):
    all_persons = graphene.List(PersonType)
    person_by_name = graphene.Field(PersonType, name=graphene.String(required=True))
    address_by_id = graphene.Field(AddressType, address_id=graphene.Int(required=True))

    def resolve_all_persons(self, info, **kwargs):
        return Person.objects.select_related("address").all()

    def resolve_person_by_name(self, info, name):
        try:
            return Person.objects.select_related("address").get(name=name)
        except Person.DoesNotExist:
            return None

    def resolve_address_by_id(self, info, address_id):
        try:
            return Address.objects.get(pk=address_id)
        except Address.DoesNotExist:
            return None


# mutations
class PersonInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String(required=True)
    email = graphene.String(required=True)


class AddressInput(graphene.InputObjectType):
    id = graphene.ID()
    number = graphene.String(required=True)
    street = graphene.String(required=True)
    city = graphene.String(required=True)
    state = graphene.String()

'''
pending for mutation setting
'''

schema = graphene.Schema(query=Query)