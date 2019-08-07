from django.contrib import admin
from activities.models.receipt_item import ReceiptItem


class ReceiptItemInlineAdmin(admin.TabularInline):
    model = ReceiptItem
    extra = 1
