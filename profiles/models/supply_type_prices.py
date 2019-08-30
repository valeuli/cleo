from django.db import models

from profiles.models import SupplyType

A_TYPE = 'Tipo A'
B_TYPE = 'Tipo B'

MATERIAL_TYPE_CHOICES = (
    (A_TYPE, 'TIPO A'),
    (B_TYPE, 'TIPO B')
)


class SupplyTypePrices(models.Model):
    """
    Model for supply type prices
    """
    amount = models.DecimalField(
        decimal_places=2,
        max_digits=10,
    )
    quantity = models.DecimalField(
        decimal_places=1,
        max_digits=4,
    )
    supply_type = models.ForeignKey(
        SupplyType,
        on_delete=models.CASCADE,
        related_name='prices',
        related_query_name='prices'
    )

    def __str__(self):
        return '{} - {}'.format( self.quantity)
