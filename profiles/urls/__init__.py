from django.urls import path, include


urlpatterns = [path('person/', include('profiles.urls.person')),
               ('provider/', include('profiles.urls.provider')),
               ('supply_type_prices/', include('profiles.urls.supply_type_prices')),
               ]
