from django.test import TestCase
from django.utils import timezone

from faker import Faker

from activities.models.receipt import Receipt
from activities.models.receipt_item import ReceiptItem
from activities.tests.faker_providers import SupplyTypeProvider

from profiles.models.person import Person
from profiles.models.provider import Provider
from profiles.tests.faker_providers import DocumentProvider, PhoneProvider


class ReceiptItemTestCase(TestCase):
    """
    Test case for ReceiptItem model.
    """

    @classmethod
    def setUpTestData(cls):
        """
        Prepare initial data.
        """
        fake = Faker()
        fake.add_provider(DocumentProvider)
        fake.add_provider(PhoneProvider)
        fake.add_provider(SupplyTypeProvider)
        personal_data = Person.objects.create(
            document_type=fake.document_type(),
            document_code=fake.document_code(),
            name=fake.name(),
            mobile_phone=fake.mobile_phone(),
            home_phone=fake.home_phone()
        )
        provider = Provider.objects.create(
            personal_data=personal_data,
            email=fake.email()
        )
        receipt = Receipt.objects.create(
            provider=provider,
            date=timezone.now(),
            observations='Text for test.'
        )
        cls.receipt_code = receipt.pk
        cls.q1 = fake.pydecimal(left_digits=3, right_digits=2, positive=True)
        cls.q2 = fake.pydecimal(left_digits=3, right_digits=2, positive=True)
        ReceiptItem.objects.create(
            receipt=receipt,
            supply_type=fake.supply_type(),
            quantity=cls.q1
        )

    def test_create(self):
        """
        Test object was created.
        """
        n = ReceiptItem.objects.all().count()
        self.assertEqual(n, 1)
        r = ReceiptItem.objects.get(receipt__pk=self.receipt_code)
        self.assertEqual(r.quantity, self.q1)

    def test_update(self):
        """
        Test update data.
        """
        r1 = ReceiptItem.objects.get(receipt__pk=self.receipt_code)
        self.assertEqual(r1.quantity, self.q1)
        r1.quantity = self.q2
        r1.save()
        r2 = ReceiptItem.objects.get(receipt__pk=self.receipt_code)
        self.assertEqual(r2.quantity, self.q2)
        n = ReceiptItem.objects.all().count()
        self.assertEqual(n, 1)

    def test_delete(self):
        """
        Test delete data.
        """
        r = ReceiptItem.objects.get(receipt__pk=self.receipt_code)
        r.delete()
        n = ReceiptItem.objects.all().count()
        self.assertEqual(n, 0)


