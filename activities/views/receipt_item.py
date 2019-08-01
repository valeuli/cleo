from django.http import HttpResponse
from django.shortcuts import render
from activities.models.receipt_item import ReceiptItem


def view(request):
    return HttpResponse('Ver recibo')


def list_receipt_item(request):
    receipt_item = ReceiptItem.objects.all()
    data = {'receipt_item': receipt_item}
    return render(request, 'activities/list_receipt_item.html', context=data)


def registration(request):
    return HttpResponse('Registrar un nuevo recibo')
