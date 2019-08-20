from django.http import HttpResponse
from django.shortcuts import render
from activities.models.receipt_item import Receipt
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST
from profiles.models.supply_type_prices import SupplyTypePrices


def view(request, _id):
    receipt = get_object_or_404(Receipt, pk=_id)
    data = {'receipt': receipt}
    return render(request, 'activities/view_ri.html', context=data)


def list_receipt(request):
    receipts = Receipt.objects.all().order_by('id')
    data = {'receipts': receipts}
    return render(request, 'activities/list_receipt.html', context=data)


def registration(request):
    return render(request, 'activities/register_receipt.html')


@require_POST
def register(request):
    data = {
        'type': SupplyTypePrices}
    return render(request, 'activities/register_receipt.html', context=data)
