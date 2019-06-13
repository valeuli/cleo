from django.test import TestCase

from profiles.models.person import Person
from profiles.models.provider import Provider
from profiles.tests.faker_providers import DocumentProvider, PhoneProvider

from faker import Faker


class ProviderTestCase(TestCase):
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
        cls.doc_code = fake.document_code()
        personal_data = Person.objects.create(
            document_type=fake.document_type(),
            document_code=cls.doc_code,
            name=fake.name(),
            mobile_phone=fake.mobile_phone(),
            home_phone=fake.home_phone()
        )
        cls.email1 = fake.email()
        cls.email2 = fake.email()
        Provider.objects.create(
            personal_data=personal_data,
            email=cls.email1
        )

    def test_create(self):
        """
        Test object was created.
        """
        n = Person.objects.all().count()
        self.assertEqual(n, 1)
        n = Provider.objects.all().count()
        self.assertEqual(n, 1)
        p = Provider.objects.get(personal_data__document_code=self.doc_code)
        self.assertEqual(p.email, self.email1)

    def test_update(self):
        """
        Test update data.
        """
        p1 = Provider.objects.get(personal_data__document_code=self.doc_code)
        self.assertEqual(p1.email, self.email1)
        p1.email = self.email2
        p1.save()
        p2 = Provider.objects.get(personal_data__document_code=self.doc_code)
        self.assertEqual(p2.email, self.email2)
        n = Provider.objects.all().count()
        self.assertEqual(n, 1)

    def test_delete(self):
        """
        Test delete data.
        """
        p = Provider.objects.get(personal_data__document_code=self.doc_code)
        p.delete()
        n = Provider.objects.all().count()
        self.assertEqual(n, 0)
