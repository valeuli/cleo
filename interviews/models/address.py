from django.db import models


class Address(models.Model):
    """
    Model for Address
    """
    street = models.CharField(
        max_length=20,
    )
    number = models.CharField(
        max_length=10
    )
    sector = models.CharField(
        max_length=30
    )
    reference = models.TextField(
        null=True
    )
    details = models.TextField(
        null=True
    )

    def __str__(self):
        return '{}, {}, {}'.format(self.sector, self.street, self.number)
