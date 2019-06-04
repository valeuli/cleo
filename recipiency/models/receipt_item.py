from django.db import models
from django.core.validators import MinValueValidator

TAPAS = 'tapas'
ENVASES = 'envases'

SUPPLY_TYPE_CHOICES = (
    (TAPAS, 'TAPAS'),
    (ENVASES,'ENVASES')
)

validators = [MinValueValidator(0.0)]


class ReceiptItem(models.Model):
    """
    Model for receipt_item
    """
    supply_type = models.CharField(
        max_length=7,  choices=SUPPLY_TYPE_CHOICES
    )
    quantity = models.DecimalField(
        decimal_places=2,
        max_digits=5
    )
