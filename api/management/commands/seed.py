from django.core.management.base import BaseCommand

from api.factories import CandidateFactory, ProfessionalFactory

# https://stackoverflow.com/questions/33024510/populate-django-database
from api.models import Job


class Command(BaseCommand):
    help = 'Seeds the database.'

    def add_arguments(self, parser):
        parser.add_argument('--users',
                            default=10,
                            type=int,
                            help='The number of fake users to create.')

    def handle(self, *args, **options):
        for job_name in ['serveur', 'plongeur', 'réceptioniste']:
            Job.objects.get_or_create(name=job_name)
        for _ in range(options['users']):
            CandidateFactory.create()
            ProfessionalFactory.create()
