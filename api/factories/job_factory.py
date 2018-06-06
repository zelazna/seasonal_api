from factory.django import DjangoModelFactory
import factory

from api.models import Job


class JobFactory(DjangoModelFactory):
    class Meta:
        model = Job
        django_get_or_create = ('name',)

    name = factory.Iterator(['serveur', 'plongeur', 'réceptioniste'])
