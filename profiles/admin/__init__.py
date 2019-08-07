from django.contrib import admin

from profiles.models.person import Person
from profiles.models.provider import Provider
from profiles.admin.person import PersonAdmin
from profiles.admin.provider import ProviderAdmin
from profiles.admin.supply_type import SupplyTypeAdmin
from profiles.models.supply_type import SupplyType

admin.site.register(Person, PersonAdmin,)
admin.site.register(Provider, ProviderAdmin)
admin.site.register(SupplyType, SupplyTypeAdmin)