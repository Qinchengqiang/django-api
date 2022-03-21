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
    person = graphene.List(PersonType)
    person_by_name = graphene.Field(PersonType, name=graphene.String(required=True))
    address_by_id = graphene.Field(AddressType, address_id=graphene.Int(required=True))

    def resolve_person(self, info, **kwargs):
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


schema = graphene.Schema(query=Query)
