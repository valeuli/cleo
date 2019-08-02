from django.http import HttpResponse
from django.shortcuts import render
from profiles.models.person import Person
from django.shortcuts import get_object_or_404


def view(request, _id):
    person = get_object_or_404(Person, pk=_id)
    data = {'person': person}
    return render(request, 'profiles/view_p.html', context=data)


def list_people(request):
    people = Person.objects.all()
    data = {'people': people}
    return render(request, 'profiles/list_people.html', context=data)


def registration(request):
    return HttpResponse('Registrar una person')
