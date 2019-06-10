from django.db import models
from profiles.models.provider import Provider


class Receipt(models.Model):
    """
    Model for Receipt
    """
    date = models.DateField()
    observations = models.TextField(
        null=True
    )
    provider = models.ForeignKey(
        Provider,
        on_delete=models.CASCADE,
        related_name='receipts',
        related_query_name='receipts'
    )

    def __str__(self):
        return '{}'.format(self.date)
