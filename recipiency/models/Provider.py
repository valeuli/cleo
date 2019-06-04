from django.db import models

class Provider(models.Model):
    """
    Model for Provider
    """

    email = models.CharField(
        unique=True,
        max_length=30
    )

    def __str__(self):
        return '{} - {}'.format(self.email)

