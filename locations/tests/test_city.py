from django.test import TestCase

from faker import Faker

from locations.models.state import State
from locations.models.city import City


class CityTestCase(TestCase):
    """
    Test case for City model.
    """
    @classmethod
    def setUpTestData(cls):
        """
        Prepare initial data.
        """
        fake = Faker()
        cls.name1 = fake.city()
        cls.name2 = fake.city()
        state = State.objects.create(
            name=fake.state(),
            country=fake.country_code()
        )
        City.objects.create(
            name=cls.name1,
            state=state
        )

    def test_create(self):
        """
        Test object was created.
        """
        n = State.objects.all().count()
        self.assertEqual(n, 1)
        n = City.objects.all().count()
        self.assertEqual(n, 1)
        c = City.objects.all()[0]
        self.assertEqual(c.name, self.name1)

    def test_update(self):
        """
        Test update data.
        """
        c1 = City.objects.get(name=self.name1)
        c1.name = self.name2
        c1.save()
        c2 = City.objects.all()[0]
        self.assertEqual(c2.name, self.name2)
        n = City.objects.all().count()
        self.assertEqual(n, 1)

    def test_delete(self):
        """
        Test delete data.
        """
        c = City.objects.all()[0]
        c.delete()
        n = City.objects.all().count()
        self.assertEqual(n, 0)
