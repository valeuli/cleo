from django.db import models


class State(models.Model):
    """
    Model for state
    """
    name = models.CharField(
        max_length=50
    )
