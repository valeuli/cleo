from django.shortcuts import render
from profiles.models.supply_type import SupplyType


def list_s(request):
    supply_types = SupplyType.objects.all()
    data = {'supply_types': supply_types}
    return render(request, 'profiles/view_s.html', context=data)
