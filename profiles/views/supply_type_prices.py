from django.http import HttpResponse


def view(request):
    return HttpResponse('Ver tabla de incentivo')


def modification(request):
    return HttpResponse('Modificar tabla de incentivo')
