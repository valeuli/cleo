from django.urls import path
from profiles.views import supply_type_prices


urlpatterns = [path('view/', supply_type_prices.view),
               path('modification/', supply_type_prices.modification),
               ]
