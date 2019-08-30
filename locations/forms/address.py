from django import forms
from locations.models import Address


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = (
            'street',
            'number',
            'sector',
            'reference',
            'details',
            'city'
        )
        labels = {
            'street':'Calle',
            'number':'Número',
            'sector':'Sector',
            'reference':'Referencia',
            'details':'Detalles',
            'city':'Ciudad'
        }
