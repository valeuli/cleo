from django.db import models


class City(models.Model):
    """
    Model for city
    """
    name = models.CharField(
        max_length=50
    )
