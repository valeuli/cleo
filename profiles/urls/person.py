from django.urls import path
from profiles.views import person


urlpatterns = [path('list_persons/', person.list_persons, name='list_persons'),
               path('views/', person.view, name='views_p'),
               path('registration/', person.registration, name='registration_p'),
               ]

