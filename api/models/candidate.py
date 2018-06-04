from django.db import models

from api.models import User, Job


class Candidate(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    year_exp = models.IntegerField()
    available_at = models.DateTimeField('available_at', null=True)
    profile_view_count = models.IntegerField(default=0)
    wage_claim = models.IntegerField()
    profile_picture_url = models.URLField(blank=True,
                                          default='',
                                          max_length=255)
    description = models.TextField(blank=True)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)

    def __str__(self):
        return "Candidate"
