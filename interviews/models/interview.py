from django.db import models


class Interview(models.Model):
    """
    Model for Interview
    """
    date = models.DateField()
    observations = models.TextField(
        null=True
    )

    def __str__(self):
        return '{}'.format(self.date)
