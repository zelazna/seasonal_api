from django.db import models

from api.models.job import Job
from api.models.user import User


class Candidate(User):
    year_exp = models.IntegerField()
    available_at = models.DateTimeField('available_at')
    profile_view_count = models.IntegerField(default=0)
    wage_claim = models.IntegerField()
    profile_picture_url = models.CharField(blank=True,
                                           default='',
                                           max_length=255)
    description = models.TextField(blank=True)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)

    def __str__(self):
        return "Candidate"

    def __repr__(self):
        return "Candidate"
