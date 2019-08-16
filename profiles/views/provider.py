from django.http import HttpResponse
from django.shortcuts import render
from profiles.models.provider import Provider
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST
from profiles.models.bank_account import ACCOUNT_TYPE
from profiles.models.person import DOCUMENT_TYPE_CHOICES


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
    return render(request, 'profiles/register_provider.html')


@require_POST
def register(request):
    data = {
        'document_type': DOCUMENT_TYPE_CHOICES,
        'account_type': ACCOUNT_TYPE
    }
    return render(request, 'profiles/register_provider.html', contex=data)
