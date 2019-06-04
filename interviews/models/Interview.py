from django.db import models


class Interview(models.Model):
    """
    Model for Interview
    """
    date=models.DateField(
        unique=False
    )
    observations = models.TextField(
        unique=False,
        null=True
    )

    def __str__(self):
        return '{} - {}'.format(self.date)
    """
    Faltaria el nombre
    """