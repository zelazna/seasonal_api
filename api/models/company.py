from django.db import models

from api.models import Job


class Company(models.Model):
    address = models.CharField(unique=True, max_length=100)
    name = models.CharField(unique=True, max_length=100)
    jobs = models.ManyToManyField(Job)

    class Meta:
        verbose_name_plural = "companies"

    def __str__(self):
        return self.name
