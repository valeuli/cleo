from django.test import TestCase

from faker import Faker

from locations.models.state import State
from locations.models.city import City
from locations.models.address import Address

from profiles.models.person import Person
from profiles.tests.faker_providers import DocumentProvider, PhoneProvider


class AddressTestCase(TestCase):
    """
    Test case for Address model.
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
        person = Person.objects.create(
            document_type=fake.document_type(),
            document_code=cls.doc_code,
            name=fake.name(),
            mobile_phone=fake.mobile_phone(),
            home_phone=fake.home_phone()
        )
        state = State.objects.create(
            name=fake.state(),
            country=fake.country_code()
        )
        city = City.objects.create(
            name=fake.city(),
            state=state
        )
        cls.street1 = fake.street_name()
        cls.street2 = fake.street_name()
        Address.objects.create(
            person=person,
            city=city,
            street=cls.street1,
            number=fake.building_number(),
            sector=fake.street_suffix()
        )

    def test_create(self):
        """
        Test object was created.
        """
        n = Address.objects.all().count()
        self.assertEqual(n, 1)
        a = Address.objects.get(person__document_code=self.doc_code)
        self.assertEqual(a.street, self.street1)

    def test_update(self):
        """
        Test update data.
        """
        a1 = Address.objects.get(person__document_code=self.doc_code)
        self.assertEqual(a1.street, self.street1)
        a1.street = self.street2
        a1.save()
        a2 = Address.objects.get(person__document_code=self.doc_code)
        self.assertEqual(a2.street, self.street2)
        n = Address.objects.all().count()
        self.assertEqual(n, 1)

    def test_delete(self):
        """
        Test delete data.
        """
        a = Address.objects.get(person__document_code=self.doc_code)
        a.delete()
        n = Address.objects.all().count()
        self.assertEqual(n, 0)
