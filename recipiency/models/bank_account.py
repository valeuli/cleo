from django.db import models
from recipiency.models.provider import Provider

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

    provider = models.OneToOneField(
        Provider,
        on_delete=models.CASCADE,
        related_name='BankAccount',
        related_query_name='BankAccount',
        null=True
    )

    def __str__(self):
        return '{} - {}'.format(self.document_code, self.account_number)
