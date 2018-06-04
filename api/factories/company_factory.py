from factory.django import DjangoModelFactory
from factory import Faker
import factory.fuzzy
from api.models import Company, Job

JOBS = [x for x in Job.objects.all()]


class CompanyFactory(DjangoModelFactory):
    class Meta:
        model = Company

    name = Faker('company')
    address = Faker('address')
    job = factory.fuzzy.FuzzyChoice(JOBS)
