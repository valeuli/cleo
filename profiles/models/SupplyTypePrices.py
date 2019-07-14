from django.db import models


class SupplyTypePrices(models):
    """
            Model for SUpplyTypePrices
    """
    amount = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        unique=False
    )
    quantity = models.DecimalField(
        decimal_places=1,
        max_digits=4,
        unique=False
    )

