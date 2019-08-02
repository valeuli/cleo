from django.urls import path
from activities.views import interview


urlpatterns = [path('view/<int:_id>/', interview.view, name='view_i'),
               path('list_interviews', interview.list_interviews, name='list_interviews'),
               path('registration/', interview.registration, name='registration_i'),
               ]
