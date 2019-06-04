from django.db import models


class Address(models.Model):
    """
    Model for Address
    """

    street = models.CharField(
        unique=False,
        max_length=20,
    )
    number = models.CharField(
        unique=False,
        max_length=10
    )
    sector = models.CharField(
        unique=False,
        max_length=30
    )
    reference = models.TextField(
        unique=False,
        null=True
    )
    details = models.TextField(
        unique=False,
        null=True
    )
    def __str__(self):
        return '{} - {}'.format(self.sector, self.street,self.number)