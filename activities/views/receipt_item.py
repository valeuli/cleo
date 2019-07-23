from django.http import HttpResponse


def view(request):
    return HttpResponse('Ver recibo')


def list_receipt_item(request):
    return HttpResponse('Ver lista de recibos')


def registration(request):
    return HttpResponse('Registrar un nuevo recibo')
