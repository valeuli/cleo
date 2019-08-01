from django.urls import path
from profiles.views import person


urlpatterns = [path('list_people/', person.list_people, name='list_people'),
               path('views/', person.view, name='views_p'),
               path('registration/', person.registration, name='registration_p'),
               ]

