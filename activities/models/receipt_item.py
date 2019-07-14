from django.db import models
from django.core.validators import MinValueValidator
from activities.models.receipt import Receipt
from profiles.models.supply_type import SupplyType


class ReceiptItem(models.Model):
    """
    Model for receipt_item
    """
    supply_type = models.ForeignKey(
        SupplyType,
        on_delete=models.CASCADE,
        related_name='receipts',
        related_query_name='receipts'
    )
    quantity = models.DecimalField(
        decimal_places=2,
        max_digits=12,
        validators=[MinValueValidator(0.0)]
    )
    receipt = models.ForeignKey(
        Receipt,
        on_delete=models.CASCADE,
        related_name='receipts',
        related_query_name='receipts'
    )

    def __str__(self):
        return self.supply_type.name
