from django.db import models
from profiles.models.person import Person
from locations.models.city import City


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
    person = models.OneToOneField(
        Person,
        on_delete=models.CASCADE,
        related_name='address',
        related_query_name='address'
    )
    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        related_name='addresses',
        related_query_name='addresses'
    )

    def __str__(self):
        return '{}, {}, {}'.format(self.sector, self.street, self.number)
