from django.http import HttpResponse


def view(request):
    return HttpResponse('Ver personas')


def list_persons(request):
    return HttpResponse('Ver lista de personas')


def registration(request):
    return HttpResponse('Registrar una person')
