from django.http import HttpResponse
from django.shortcuts import render
from profiles.models.supply_type_prices import SupplyTypePrices
from django.shortcuts import get_object_or_404


def view_s(request, id):
    price = get_object_or_404(SupplyTypePrices)
    data = {'prices': price}
    return render(request, 'profiles/view_p.html', context=data)


def modification_s(request):
    return HttpResponse('Modificar tabla de incentivo')
