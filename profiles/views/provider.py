from django.http import HttpResponse


def view(request):
    return HttpResponse('Ver proveedores')


def list_provider(request):
    return HttpResponse('Ver lista de proveedores')


def registration(request):
    return HttpResponse('Registrar un nuevo proveedor')
