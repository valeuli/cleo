from django.contrib import admin

from locations.models.state import State
from locations.models.city import City

admin.site.register(State)
admin.site.register(City)
