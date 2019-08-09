from django.urls import path
from profiles.views import supply_type_prices


urlpatterns = [path('view_s/', supply_type_prices.view_s, name='view_s'),
               path('modification_s/', supply_type_prices.modification_s, name='modification_s'),
               ]
