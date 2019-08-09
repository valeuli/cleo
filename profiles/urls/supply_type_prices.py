from django.urls import path
from profiles.views import suppy_type


urlpatterns = [path('view_s/', suppy_type.list_s, name='view_s'),
               ]
