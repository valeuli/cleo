from django.urls import path, include


urlpatterns = [path('person/', include('profiles.urls.person')),
               path('provider/', include('profiles.urls.provider')),
               path('supply_type_prices/', include('profiles.urls.supply_type_prices')),
               ]
