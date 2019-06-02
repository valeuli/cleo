from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


ID_CARD = 'c.i.'
TAX_INFORMATION_REGISTRY = 'r.i.f.'

DOCUMENT_TYPE_CHOICES = (
    (ID_CARD, 'C.I.'),
    (TAX_INFORMATION_REGISTRY, 'R.I.F.'),
)


class Person(models.Model):
    """
    Model for Persom
    """
    class Meta:
        verbose_name_plural = 'people'

    document_code = models.CharField(
        unique=True, max_length=15
    )
    document_type = models.CharField(
        max_length=6, choices=DOCUMENT_TYPE_CHOICES
    )
    name = models.CharField(
        max_length=100
    )
    mobile_phone = PhoneNumberField(
        blank=False,
        null=False,
        default="+00000000000",
        unique=True,
        verbose_name="mobile",
    )
    home_phone = PhoneNumberField(
        blank=False,
        null=True,
        unique=False,
        default="+00000000000",
        verbose_name="phone",
    )

    def __str__(self):
        return '{} - {}'.format(self.document_code, self.name)
