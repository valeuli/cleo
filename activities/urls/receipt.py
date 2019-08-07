from django.urls import path
from activities.views import receipt


urlpatterns = [path('view/<int:_id>', receipt.view, name='view_ri'),
               path('list_receipt', receipt.list_receipt, name='list_receipts'),
               path('registration/', receipt.registration, name='registration_ri'),
               ]
