from django.http import HttpResponse
from django.shortcuts import render
from profiles.models.provider import Provider


def view(request):
    return HttpResponse('Ver proveedor')


def list_provider(request):
    providers = Provider.objects.all()
    data = {'providers': providers}
    return render(request, 'profiles/list_provider.html', context=data)


def registration(request):
    return HttpResponse('Registrar un nuevo proveedor')
