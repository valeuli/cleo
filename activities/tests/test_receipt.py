from django.test import TestCase
from django.utils import timezone

from faker import Faker

from activities.models.receipt import Receipt

from profiles.models.person import Person
from profiles.models.provider import Provider
from profiles.tests.faker_providers import DocumentProvider, PhoneProvider


class ReceiptTestCase(TestCase):
    """
    Test case for Receipt model.
    """

    @classmethod
    def setUpTestData(cls):
        """
        Prepare initial data.
        """
        fake = Faker()
        fake.add_provider(DocumentProvider)
        fake.add_provider(PhoneProvider)
        cls.doc_code = fake.document_code()
        personal_data = Person.objects.create(
            document_type=fake.document_type(),
            document_code=cls.doc_code,
            name=fake.name(),
            mobile_phone=fake.mobile_phone(),
            home_phone=fake.home_phone()
        )
        provider = Provider.objects.create(
            personal_data=personal_data,
            email=fake.email()
        )
        Receipt.objects.create(
            provider=provider,
            date=timezone.now(),
            observations='Text for test.'
        )

    def test_create(self):
        """
        Test object was created.
        """
        n = Receipt.objects.all().count()
        self.assertEqual(n, 1)
        r = Receipt.objects.get(
            provider__personal_data__document_code=self.doc_code
        )
        self.assertEqual(r.observations, 'Text for test.')

    def test_update(self):
        """
        Test update data.
        """
        r1 = Receipt.objects.get(
            provider__personal_data__document_code=self.doc_code
        )
        self.assertEqual(r1.observations, 'Text for test.')
        r1.observations = 'Text modified for test.'
        r1.save()
        r2 = Receipt.objects.get(
            provider__personal_data__document_code=self.doc_code
        )
        self.assertEqual(r2.observations, 'Text modified for test.')
        n = Receipt.objects.all().count()
        self.assertEqual(n, 1)

    def test_delete(self):
        """
        Test delete data.
        """
        r = Receipt.objects.get(
            provider__personal_data__document_code=self.doc_code
        )
        r.delete()
        n = Receipt.objects.all().count()
        self.assertEqual(n, 0)


