from django.db import models


class SupplyType(models):
    """
        Model for SupplyType
        """
    name = models.CharField(
        max_length=50
    )

    def __str__(self):
        return self.name
