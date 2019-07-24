from django.urls import path
from profiles.views import provider


urlpatterns = [path('list_provider/', provider.list_provider),
               path('views/', provider.view),
               path('registration/', provider.registration),
               ]
