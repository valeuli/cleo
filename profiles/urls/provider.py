from django.urls import path
from profiles.views import provider


urlpatterns = [path('list_provider/', provider.list_provider, name='list_provider'),
               path('view/<int:_id>/', provider.view, name='view_po'),
               path('registration/', provider.registration, name='registration_po'),
               ]
