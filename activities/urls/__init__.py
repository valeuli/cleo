from django.urls import path, include


urlpatterns = [path('interview/', include('activities.urls.interview')),
               path('receipt/', include('activities.urls.receipt')),
               ]
