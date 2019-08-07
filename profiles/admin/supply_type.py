from django.contrib import admin
from profiles.admin.supply_type_prices import SupplyTypePricesInlineAdmin
from profiles.models.supply_type import SupplyType


class SupplyTypeAdmin(admin.ModelAdmin):
    inlines = (SupplyTypePricesInlineAdmin, )
    model = SupplyType

