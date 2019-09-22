from django.shortcuts import render, redirect
from activities.models.receipt_item import Receipt
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST
from profiles.forms.supply_type_prices import SupplyTypePricesForm
from activities.forms.receipt import ReceiptForm


def view(request, _id):
    receipt = get_object_or_404(Receipt, pk=_id)
    data = {'receipt': receipt}
    return render(request, 'activities/view_ri.html', context=data)


def list_receipt(request):
    receipts = Receipt.objects.all().order_by('id')
    data = {'receipts': receipts}
    return render(request, 'activities/list_receipt.html', context=data)


def registration(request):
    data = {
        'supply_type': SupplyTypePricesForm(),
        'receipt': ReceiptForm()
        }
    return render(request, 'activities/register_receipt.html', context=data)


@require_POST
def register(request):
    receitp_form = ReceiptForm(request.POST)

    if not receipt_form.is_valid():
        messages.error(request, receipt_form.errors)
        data = {
            'receipt_form': receipt_form,
            'provider_form': provider_form,
        }
        return render(request, 'activities/register_receipt.html', context=data)

    receipt = Receipt.objects.create(
        date = receitp_form.cleaned_data['date'],
        observations = receitp_form.cleaned_data['observations'],
        provider = receitp_form.cleaned_data['provider']
    )

    messages.success(request, 'Recibo agregado con éxito')
    return redirect('list_receipt')
