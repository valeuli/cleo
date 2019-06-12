from django.test import TestCase

from profiles.models.person import Person
from profiles.models.provider import Provider
from profiles.models.bank_account import (
    BankAccount, CURRENT_ACCOUNT, SAVINGS_ACCOUNT
)
from profiles.tests.faker_providers import (
    DocumentProvider, PhoneProvider, BankAccountProvider
)

from faker import Faker


class BankAccountTestCase(TestCase):
    """
    Test case for Provider model.
    """
    @classmethod
    def setUpTestData(cls):
        """
        Prepare initial data
        """
        fake = Faker()
        fake.add_provider(DocumentProvider)
        fake.add_provider(PhoneProvider)
        fake.add_provider(BankAccountProvider)
        personal_data = Person.objects.create(
            document_type=fake.document_type(),
            document_code=fake.document_code(),
            name='{} {}'.format(
                fake.first_name(), fake.last_name()
            ),
            mobile_phone=fake.mobile_phone(),
            home_phone=fake.home_phone()
        )
        provider = Provider.objects.create(
            personal_data=personal_data,
            email=fake.email()
        )
        cls.account_number = fake.bank_account_code()
        BankAccount.objects.create(
            bank=fake.bank_name(),
            account_type=CURRENT_ACCOUNT,
            account_number=cls.account_number,
            name='{} {}'.format(
                fake.first_name(), fake.last_name()
            ),
            document_code=fake.document_code(),
            provider=provider
        )

    def test_create(self):
        """
        Test object was created.
        """
        n = Person.objects.all().count()
        self.assertEqual(n, 1)
        n = Provider.objects.all().count()
        self.assertEqual(n, 1)
        n = BankAccount.objects.all().count()
        self.assertEqual(n, 1)
        b = BankAccount.objects.get(account_number=self.account_number)
        self.assertEqual(b.account_type, CURRENT_ACCOUNT)

    def test_update(self):
        """
        Test update data.
        """
        b1 = BankAccount.objects.get(account_number=self.account_number)
        self.assertEqual(b1.account_type, CURRENT_ACCOUNT)
        b1.account_type = SAVINGS_ACCOUNT
        b1.save()
        b2 = BankAccount.objects.get(account_number=self.account_number)
        self.assertEqual(b2.account_type, SAVINGS_ACCOUNT)
        n = BankAccount.objects.all().count()
        self.assertEqual(n, 1)

    def test_delete(self):
        """
        Test delete data.
        """
        p = BankAccount.objects.get(account_number=self.account_number)
        p.delete()
        n = BankAccount.objects.all().count()
        self.assertEqual(n, 0)
