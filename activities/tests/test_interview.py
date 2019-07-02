from django.test import TestCase
from django.utils import timezone

from faker import Faker

from activities.models.interview import Interview

from profiles.models.person import Person
from profiles.tests.faker_providers import DocumentProvider, PhoneProvider


class InterviewTestCase(TestCase):
    """
     Test case for Interview model.
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

        person = Person.objects.create(
            document_type=fake.document_type(),
            document_code=cls.doc_code,
            name=fake.name(),
            mobile_phone=fake.mobile_phone(),
            home_phone=fake.home_phone(),
        )
        Interview.objects.create(
            date=timezone.now(),
            person=person,
            observations='Text for test.'
        )

    def test_create(self):
        """
        Test object was created.
        """
        n = Interview.objects.all().count()
        self.assertEqual(n, 1)
        interview = Interview.objects.get(person__document_code=self.doc_code)
        self.assertEqual(interview.observations, 'Text for test.')

    def test_update(self):
        """
        Test update data.
        """
        i1 = Interview.objects.get(person__document_code=self.doc_code)
        self.assertEqual(i1.observations, 'Text for test.')
        i1.observations = 'Text modified for test.'
        i1.save()
        i2 = Interview.objects.get(person__document_code=self.doc_code)
        self.assertEqual(i2.observations, 'Text modified for test.')
        n = Interview.objects.all().count()
        self.assertEqual(n, 1)

    def test_delete(self):
        """
        Test delete data.
        """
        interview = Interview.objects.get(person__document_code=self.doc_code)
        interview.delete()
        n = Interview.objects.all().count()
        self.assertEqual(n, 0)
