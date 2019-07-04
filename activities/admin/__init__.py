from django.contrib import admin

from activities.models.interview import Interview
from activities.models.receipt import Receipt
from activities.admin.receipt import ReceiptAdmin


admin.site.register(Interview)
admin.site.register(Receipt, ReceiptAdmin)
