from django.contrib import admin
from profiles.models.bank_account import BankAccount


class BankAccountInlineAdmin(admin.StackedInline):
    model = BankAccount
