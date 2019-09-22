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
        null=False,
        unique=True,
        verbose_name="mobile",
    )
    home_phone = PhoneNumberField(
        blank=True,
        null=True,
        unique=False,
        default='',
        verbose_name="phone",
    )

    def __str__(self):
        return '{} - {}'.format(self.document_code, self.name)
