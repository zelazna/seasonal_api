from factory.django import DjangoModelFactory
from factory import Faker
import factory.fuzzy
from api.models import Company


class CompanyFactory(DjangoModelFactory):
    class Meta:
        model = Company

    name = Faker('company')
    address = Faker('address')

    @factory.post_generation
    def jobs(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for job in extracted:
                self.jobs.add(job)
