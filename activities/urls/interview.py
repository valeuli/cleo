from django.urls import path
from activities.view import interview


urlpatterns = [path('view/', interview.view),
               path('list_interviews', interview.list_interviews),
               path('registration/', interview.registration),
               ]
