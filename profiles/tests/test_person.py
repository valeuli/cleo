from django.test import TestCase

from profiles.models.person import Person
from profiles.tests.faker_providers import DocumentProvider, PhoneProvider

from faker import Faker


class PersonTestCase(TestCase):
    """
    Test case for Person model.
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
        cls.name1 = fake.name()
        cls.name2 = fake.name()
        Person.objects.create(
            document_type=fake.document_type(),
            document_code=cls.doc_code,
            name=cls.name1,
            mobile_phone=fake.mobile_phone(),
            home_phone=fake.home_phone()
        )

    def test_create(self):
        """
        Test object was created.
        """
        n = Person.objects.all().count()
        self.assertEqual(n, 1)
        p = Person.objects.get(document_code=self.doc_code)
        self.assertEqual(p.name, self.name1)

    def test_update(self):
        """
        Test update data.
        """
        p1 = Person.objects.get(document_code=self.doc_code)
        self.assertEqual(p1.name, self.name1)
        p1.name = self.name2
        p1.save()
        p2 = Person.objects.get(document_code=self.doc_code)
        self.assertEqual(p2.name, self.name2)
        n = Person.objects.all().count()
        self.assertEqual(n, 1)

    def test_delete(self):
        """
        Test delete data.
        """
        p = Person.objects.get(document_code=self.doc_code)
        p.delete()
        n = Person.objects.all().count()
        self.assertEqual(n, 0)
