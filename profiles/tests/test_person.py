import random

from django.utils.crypto import get_random_string
from string import digits

from django.test import TestCase

from profiles.models.person import (
    Person, ID_CARD, TAX_INFORMATION_REGISTRY
)

from faker.providers import BaseProvider
from faker import Faker


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


class PersonTestCase(TestCase):
    """
    Test case for Person model.
    """
    def setUp(self):
        self.fake = Faker()
        self.fake.add_provider(DocumentProvider)
        self.fake.add_provider(PhoneProvider)

    def test_person_creation(self):
        person = Person.objects.create(
            document_type=self.fake.document_type(),
            document_code=self.fake.document_code(),
            name='{} {}'.format(
                self.fake.first_name(), self.fake.last_name()
            ),
            mobile_phone=self.fake.mobile_phone(),
            home_phone=self.fake.home_phone()
        )
        self.assertIsInstance(person, Person)
