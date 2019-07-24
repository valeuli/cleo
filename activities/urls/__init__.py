from django.urls import path, include


urlpatterns = [path('interview/', include('activities.urls.interview')),
               path('receipt_item/', include('activities.urls.receipt_item')),
               ]
