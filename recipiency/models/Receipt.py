from django.db import models


class Receipt(models.Model):
    """
    Model for Receipt
    """
    date = models.DateField(
        unique=False
    )
    observations = models.TextField(
        unique=False,
        null=True
    )

    def __str__(self):
        return '{} - {}'.format(self.date,self.observations)

    """
    Faltan otras cosas
    """