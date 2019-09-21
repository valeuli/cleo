from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Person(models.Model):
    """
    Model for Person
    """
    class Meta:
        verbose_name_plural = 'people'

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
