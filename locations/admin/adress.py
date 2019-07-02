from django.contrib import admin
from locations.models.address import Address


class AddressInlineAdmin(admin.StackedInline):
    model = Address
