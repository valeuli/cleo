from django.urls import path
from profiles.views import person


urlpatterns = [path('list_persons/', person.list_persons),
               path('views/', person.views),
               path('registration/', person.registration),
               ]
