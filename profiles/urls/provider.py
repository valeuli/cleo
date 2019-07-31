from django.urls import path
from profiles.views import provider


urlpatterns = [path('list_provider/', provider.list_provider, name='list_provider'),
               path('views/', provider.view, name='views_po'),
               path('registration/', provider.registration, name='registration_po'),
               ]
