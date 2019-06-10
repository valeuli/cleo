from django.db import models
from interviews.models.person import Person
from interviews.models.city import City


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
        related_name='address',
        related_query_name='address'
    )

    def __str__(self):
        return '{}, {}, {}'.format(self.sector, self.street, self.number)
