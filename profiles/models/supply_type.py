from django.db import models


class SupplyType(models.Model):
    """
    Model for SupplyType
    """
    name = models.CharField(
        max_length=50,
        null=True,
    )

    def __str__(self):
        return self.name
