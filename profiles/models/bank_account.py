from django.db import models
from profiles.models.provider import Provider
from profiles.models.person import DOCUMENT_TYPE_CHOICES

SAVINGS_ACCOUNT = 'ahorro'
CURRENT_ACCOUNT = 'corriente'

ACCOUNT_TYPE = (
    (SAVINGS_ACCOUNT, 'AHORRO'),
    (CURRENT_ACCOUNT, 'CORRIENTE')
)


class BankAccount(models.Model):
    """
    Model for bank_account
    """
    bank = models.CharField(
        unique=False, max_length=59
    )
    account_type = models.CharField(
        max_length=9, choices=ACCOUNT_TYPE
    )
    account_number = models.CharField(
        unique=True, max_length=20
    )
    name = models.CharField(
        max_length=100
    )
    document_code = models.CharField(
        max_length=15
    )
    document_type = models.CharField(
        max_length=6, choices=DOCUMENT_TYPE_CHOICES
    )
    provider = models.OneToOneField(
        Provider,
        on_delete=models.CASCADE,
        related_name='bank_account',
        related_query_name='bank_account'
    )

    def __str__(self):
        return '{} - {}'.format(self.document_code, self.account_number)
