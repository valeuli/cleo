import random

from django.utils.crypto import get_random_string
from string import digits

from faker.providers import BaseProvider
from profiles.models.person import ID_CARD, TAX_INFORMATION_REGISTRY
from profiles.models.bank_account import CURRENT_ACCOUNT, SAVINGS_ACCOUNT


class DocumentProvider(BaseProvider):
    """
    Provider to generate random identity document for Faker.
    """
    def __init__(self, generator):
        super(DocumentProvider, self).__init__(generator)
        self._doc_type = None

    def _generate_document_type(self):
        document_types = (ID_CARD, TAX_INFORMATION_REGISTRY)
        self._doc_type = random.choice(document_types)

    def document_type(self):
        if self._doc_type is None:
            self._generate_document_type()
        return self._doc_type

    def document_code(self):
        dt = self.document_type()
        if dt == ID_CARD:
            cs = ['V', 'E']
        else:
            cs = ['J', 'G']

        c = random.choice(cs)

        length = 8 if dt == ID_CARD else 9

        n = get_random_string(length=length, allowed_chars=digits)
        return c + '0' + n


class PhoneProvider(BaseProvider):
    """
    Provider to generate random phone numbers for Faker.
    """
    @staticmethod
    def _generate_number(cod):
        num = get_random_string(length=7, allowed_chars=digits)
        return '+58' + cod + num

    def mobile_phone(self):
        cods = ('416', '426', '414', '424', '412')
        return self._generate_number(random.choice(cods))

    def home_phone(self):
        if random.random() < 0.7:
            return None
        cods = ('274', '251')
        return self._generate_number(random.choice(cods))


class BankAccountProvider(BaseProvider):
    """
    Provider to generate random bank accounts for Faker.
    """
    @staticmethod
    def bank_account_type():
        account_types = (CURRENT_ACCOUNT, SAVINGS_ACCOUNT)
        return random.choice(account_types)

    @staticmethod
    def bank_account_code():
        return get_random_string(length=20, allowed_chars=digits)

    @staticmethod
    def bank_name():
        names = (
            'Banco de Venezuela',
            'Provincial BBVA',
            'Banesco',
            'Banco Occidental de Descuento',
            'Banco Mercantil'
        )
        return random.choice(names)
