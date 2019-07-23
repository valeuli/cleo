from django.urls import path
from activities.views import receipt_item


urlpatterns = [path('view/', receipt_item.view),
               path('list_interviews', receipt_item.list_interviews),
               path('registration/', receipt_item.registration),
               ]
