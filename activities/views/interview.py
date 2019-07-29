from django.http import HttpResponse


def view(request):
    return HttpResponse('Ver abordaje')


def list_interviews(request):
    return HttpResponse('Ver lista de abordaje')


def registration(request):
    return HttpResponse('Registrar un nuevo abordaje')
