from django.db import models
from interviews.models.person import Person


class Interview(models.Model):
    """
    Model for Interview
    """
    date = models.DateField()
    observations = models.TextField(
        null=True
    )
    person = models.OneToOneField(
        Person,
        on_delete=models.CASCADE,
        related_name='interview',
        related_query_name='interview',
    )

    def __str__(self):
        return '{}'.format(self.date)
