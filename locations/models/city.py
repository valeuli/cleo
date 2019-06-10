from django.db import models
from locations.models.state import State


class City(models.Model):
    """
    Model for city
    """
    class Meta:
        verbose_name_plural = 'cities'

    name = models.CharField(
        max_length=50
    )
    state = models.ForeignKey(
        State,
        on_delete=models.CASCADE,
        related_name='cities',
        related_query_name='cities'
    )

    def __str__(self):
        return self.name
