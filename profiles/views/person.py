from django.http import HttpResponse
from django.shortcuts import render
from profiles.models.person import Person


def view(request):
    return HttpResponse('Ver personas')


def list_people(request):
    people = Person.objects.all()
    data = {'people': people}
    return render(request, 'profiles/list_people.html', context=data)


def registration(request):
    return HttpResponse('Registrar una person')
