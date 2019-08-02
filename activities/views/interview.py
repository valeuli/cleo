from django.http import HttpResponse
from django.shortcuts import render
from activities.models.interview import Interview
from django.shortcuts import get_object_or_404


def view(request, _id):
    interview = get_object_or_404(Interview, pk=_id)
    data = {'interview': interview}
    return render(request, 'activities/view_i.html', context=data)


def list_interviews(request):
    interviews = Interview.objects.all()
    data = {'interviews': interviews}
    return render(request, 'activities/list_interviews.html', context=data)


def registration(request):
    return HttpResponse('Registrar un nuevo abordaje')
