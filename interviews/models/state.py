from django.db import models
from django_countries.fields import CountryField


class State(models.Model):
    """
    Model for state
    """
    name = models.CharField(
        max_length=50
    )
    country = CountryField()

    def __str__(self):
        return self.name

