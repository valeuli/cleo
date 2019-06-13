import random

from faker.providers import BaseProvider

from activities.models.receipt_item import ENVASES, TAPAS


class SupplyTypeProvider(BaseProvider):
    """
    Provider to generate random supply types for faker.
    """
    @staticmethod
    def supply_type():
        return random.choice((ENVASES, TAPAS))
