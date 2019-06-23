from django.contrib import admin

from profiles.models.person import Person
from profiles.models.provider import Provider
from profiles.admin.person import PersonAdmin
from profiles.admin.provider import ProviderAdmin

admin.site.register(Person, PersonAdmin,)
admin.site.register(Provider, ProviderAdmin)
