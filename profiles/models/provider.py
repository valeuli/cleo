from django.db import models

from profiles.models.person import Person


class Provider(models.Model):
    """
    Model for Provider
    """
    personal_data = models.OneToOneField(
        Person,
        on_delete=models.CASCADE
    )
    email = models.CharField(
        unique=True,
        max_length=59
    )

    def __str__(self):
        return self.personal_data.name

