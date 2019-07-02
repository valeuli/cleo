from django.contrib import admin
from locations.admin.adress import AddressInlineAdmin


class PersonAdmin(admin.ModelAdmin):
    inlines = (AddressInlineAdmin,)

