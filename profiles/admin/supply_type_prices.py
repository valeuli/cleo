from django.contrib import admin
from profiles.models.supply_type_prices import SupplyTypePrices


class SupplyTypePricesInlineAdmin(admin.TabularInline):
    model = SupplyTypePrices
    extra = 1
