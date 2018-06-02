from django.db import models

from api.models.company import Company
from api.models.user import User


class Professional(User):
    company = models.ForeignKey(Company,
                                related_name='employees',
                                on_delete=models.CASCADE)

    def __str__(self):
        return "Professional"

    def __repr__(self):
        return "Professional"
