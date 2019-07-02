from django.contrib import admin
from profiles.admin.bank_account import BankAccountInlineAdmin


class ProviderAdmin(admin.ModelAdmin):
    inlines = (BankAccountInlineAdmin,)
