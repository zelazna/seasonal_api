from factory.django import DjangoModelFactory
import factory

from api.factories import UserFactory, CompanyFactory
from api.models import Professional


class ProfessionalFactory(DjangoModelFactory):
    class Meta:
        model = Professional

    user = factory.SubFactory(UserFactory)
    company = factory.SubFactory(CompanyFactory)
