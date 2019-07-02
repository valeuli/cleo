from django.contrib import admin
from activities.admin.receipt_item import ReceiptItemInlineAdmin


class ReceiptAdmin(admin.ModelAdmin):
    inlines = (ReceiptItemInlineAdmin,)
