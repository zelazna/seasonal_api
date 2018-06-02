from django.db import models

from api.models import Company, User


class Professional(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    company = models.ForeignKey(Company,
                                related_name='employees',
                                on_delete=models.CASCADE)

    def __str__(self):
        return "Professional"
