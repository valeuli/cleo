from django.shortcuts import render, redirect
from profiles.models.provider import Provider
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST
from profiles.forms.bank_account import BankAccountForm
from profiles.forms.provider import ProviderForm
from locations.forms.address import AddressForm
from django.contrib import messages
from profiles.models.person import Person
from profiles.models.bank_account import BankAccount
from locations.models.address import Address


def view(request, _id):
    provider = get_object_or_404(Provider, pk=_id)
    data = {'provider': provider}
    last_three_receipts = provider.receipts.order_by('-date')[:3]

    if last_three_receipts.exists():
        data.update({'receipts': last_three_receipts})

    return render(request, 'profiles/view_po.html', context=data)


def list_provider(request):
    providers = Provider.objects.all()
    data = {'providers': providers}
    return render(request, 'profiles/list_provider.html', context=data)


def registration(request):
    data = {
        'personal_form': ProviderForm(),
        'address_form': AddressForm(),
        'bank_form': BankAccountForm()
    }
    return render(request, 'profiles/register_provider.html', context=data)


@require_POST
def register(request):
    provider_form = ProviderForm(request.POST)
    address_form = AddressForm(request.POST)
    bank_form = BankAccountForm(request.POST)
    if not provider_form.is_valid():
        messages.error(request, provider_form.errors)
        data = {
            'personal_form': provider_form,
            'address_form': address_form,
            'bank_form': bank_form
        }
        return render(request, 'profiles/register_provider.html', context=data)

    if not address_form.is_valid():
        messages.error(request, address_form.errors)
        data = {
            'personal_form': provider_form,
            'address_form': address_form,
            'bank_form': bank_form
        }
        return render(request, 'profiles/register_provider.html', context=data)

    if not bank_form.is_valid():
        messages.error(request, bank_form.errors)
        data = {
            'personal_form': provider_form,
            'address_form': address_form,
            'bank_form': bank_form
        }
        return render(request, 'profiles/register_provider.html', context=data)

    person = Person.objects.create(
        document_code=provider_form.cleaned_data['document_number'],
        document_type=provider_form.cleaned_data['document_type'],
        name=provider_form.cleaned_data['name'],
        mobile_phone=provider_form.cleaned_data['mobile_phone'],
        home_phone=provider_form.cleaned_data['home_phone']
    )

    provider = Provider.objects.create(
        personal_data=person,
        email=provider_form.cleaned_data['email']
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

    BankAccount.objects.create(
        bank=bank_form.cleaned_data['bank_name'],
        account_type=bank_form.cleaned_data['account_type'],
        account_number=bank_form.cleaned_data['account_number'],
        name=bank_form.cleaned_data['name'],
        document_code=bank_form.cleaned_data['document_code'],
        document_type=bank_form.cleaned_data['document_type'],
        provider=provider
    )

    messages.success(request, 'Proveedor agregado con éxito')
    return redirect('list_provider')
