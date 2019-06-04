from django.db import models


class Receipt(models.Model):
    """
    Model for Receipt
    """
    date = models.DateField()
    observations = models.TextField(
        null=True
    )

    def __str__(self):
        return '{}'.format(self.date)
