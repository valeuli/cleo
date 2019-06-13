from django.test import TestCase

from faker import Faker

from locations.models.state import State


class StateTestCase(TestCase):
    """
    Test case for State model.
    """
    @classmethod
    def setUpTestData(cls):
        """
        Prepare initial data
        """
        fake = Faker()
        cls.name1 = fake.state()
        cls.name2 = fake.state()
        State.objects.create(
            name=cls.name1,
            country=fake.country_code()
        )

    def test_create(self):
        """
        Test object was created.
        """
        n = State.objects.all().count()
        self.assertEqual(n, 1)
        s = State.objects.all()[0]
        self.assertEqual(s.name, self.name1)

    def test_update(self):
        """
        Test update data.
        """
        s1 = State.objects.get(name=self.name1)
        s1.name = self.name2
        s1.save()
        s2 = State.objects.all()[0]
        self.assertEqual(s2.name, self.name2)
        n = State.objects.all().count()
        self.assertEqual(n, 1)

    def test_delete(self):
        """
        Test delete data.
        """
        s = State.objects.get()
        s.delete()
        n = State.objects.all().count()
        self.assertEqual(n, 0)