from django.db import models
from profiles.models.person import Person


ID_CARD = 'c.i.'
TAX_INFORMATION_REGISTRY = 'r.i.f.'

DOCUMENT_TYPE_CHOICES = (
    (ID_CARD, 'C.I.'),
    (TAX_INFORMATION_REGISTRY, 'R.I.F.'),
)


class Provider(models.Model):
    """
    Model for Provider
    """
    personal_data = models.OneToOneField(
        Person,
        on_delete=models.CASCADE
    )
    email = models.EmailField(
        unique=True
    )
    document_code = models.CharField(
        unique=True, max_length=15
    )
    document_type = models.CharField(
        max_length=6, choices=DOCUMENT_TYPE_CHOICES
    )

    def __str__(self):
        return self.personal_data.name

