from factory.django import DjangoModelFactory
from factory import Faker, SubFactory
import factory.fuzzy
from api.factories import UserFactory
from api.models import Candidate, Job
from random import randint
import os


class CandidateFactory(DjangoModelFactory):
    class Meta:
        model = Candidate

    user = SubFactory(UserFactory)
    year_exp = randint(1, 15)
    # TODO : fix naive datetime format
    available_at = Faker('date_time')
    profile_view_count = randint(0, 400)
    wage_claim = randint(10000, 50000)
    profile_picture_url = f"{os.environ.get('HEROKU_URL')}/media/uploads/placeholder.png"
    description = Faker('sentence')
    job = factory.fuzzy.FuzzyChoice(Job.objects.all())
