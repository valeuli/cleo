from django.urls import path
from activities.views import receipt_item


urlpatterns = [path('view/', receipt_item.view, name='view_ri'),
               path('list_receipt_item', receipt_item.list_receipt_item, name='list_receipt_item'),
               path('registration/', receipt_item.registration, name='registration_ri'),
               ]
