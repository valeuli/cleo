from django.shortcuts import render, redirect
from activities.models.interview import Interview
from locations.models.address import Address
from profiles.models.person import Person
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST
from activities.forms.interview import InterviewForm
from locations.forms.address import AddressForm

from django.contrib import messages


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
    interview_form = InterviewForm(request.POST)
    address_form = AddressForm(request.POST)
    if not interview_form.is_valid():
        messages.error(request, interview_form.errors)
        data = {
            'interview_form': interview_form,
            'address_form': address_form,
        }
        return render(request, 'activities/register_interviews.html', context=data)

    if not address_form.is_valid():
        messages.error(request, address_form.errors)
        data = {
            'interview_form': interview_form,
            'address_form': address_form,
        }
        return render(request, 'activities/register_interviews.html', context=data)

    person = Person.objects.create(
        name=interview_form.cleaned_data['name'],
        mobile_phone=interview_form.cleaned_data['mobile_phone'],
        home_phone=interview_form.cleaned_data['home_phone']
    )

    interview = Interview.objects.create(
        date = interview_form.cleaned_data['date'],
        observations = interview_form.cleaned_data['observations'],
    )

    Address.objects.create(
        street=address_form.cleaned_data['street'],
        number=address_form.cleaned_data['number'],
        sector=address_form.cleaned_data['sector'],
        reference=address_form.cleaned_data['reference'],
        details=address_form.cleaned_data['details'],
        person=person,
        city=address_form.cleaned_data['city']
    )
    messages.success(request, 'Abordaje agregado con éxito')
    return redirect('list_interviews')
