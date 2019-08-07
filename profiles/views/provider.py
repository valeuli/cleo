from django.http import HttpResponse
from django.shortcuts import render
from profiles.models.provider import Provider
from django.shortcuts import get_object_or_404


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
    return HttpResponse('Registrar un nuevo proveedor')
