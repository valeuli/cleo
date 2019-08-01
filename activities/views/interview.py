from django.http import HttpResponse
from django.shortcuts import render
from activities.models.interview import Interview


def view(request):
    return HttpResponse('Ver abordaje')


def list_interviews(request):
    interviews = Interview.objects.all()
    data = {'interviews': interviews}
    return render(request, 'activities/list_interviews.html', context=data)


def registration(request):
    return HttpResponse('Registrar un nuevo abordaje')
