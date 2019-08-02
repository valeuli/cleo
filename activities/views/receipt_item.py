from django.http import HttpResponse
from django.shortcuts import render
from activities.models.receipt_item import ReceiptItem


def view(request, _id):
    receipt= get_object_or_404(Interview, pk=_id)
    data = {'receipt': receipt}
    return render(request, 'activities/view_ri.html', context=data)


def list_receipt_item(request):
    receipt_item = ReceiptItem.objects.all()
    data = {'receipt_item': receipt_item}
    return render(request, 'activities/list_receipt_item.html', context=data)


def registration(request):
    return HttpResponse('Registrar un nuevo recibo')
