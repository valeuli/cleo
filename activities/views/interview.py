from django.shortcuts import render
from activities.models.interview import Interview
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST
from activities.forms.interview import InterviewForm
from locations.forms.address import AddressForm


def view(request, _id):
    interview = get_object_or_404(Interview, pk=_id)
    data = {'interview': interview}
    return render(request, 'activities/view_i.html', context=data)


def list_interviews(request):
    interviews = Interview.objects.all()
    data = {'interviews': interviews}
    return render(request, 'activities/list_interviews.html', context=data)


def registration(request):
    data = {
        'interview_form': InterviewForm(),
        'address_form': AddressForm()
    }
    return render(request, 'activities/register_interviews.html', context=data)


@require_POST
def register(request):
    pass

