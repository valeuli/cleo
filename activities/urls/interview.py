from django.urls import path
from activities.views import interview


urlpatterns = [path('view/', interview.view),
               path('list_interviews', interview.list_interviews),
               path('registration/', interview.registration),
               ]
