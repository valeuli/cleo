from django.urls import path
from activities.views import receipt_item


urlpatterns = [path('view/', receipt_item.view),
               path('list_receipt_item', receipt_item.list_receipt_item),
               path('registration/', receipt_item.registration),
               ]
