from factory.django import DjangoModelFactory
from factory import Faker
import factory.fuzzy

from api.models import Company, Job


class CompanyFactory(DjangoModelFactory):
    class Meta:
        model = Company

    name = Faker('company')
    address = Faker('address')
    job = factory.fuzzy.FuzzyChoice(Job.objects.all())
