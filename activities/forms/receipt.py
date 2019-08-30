from django import forms
from profiles.models.provider import Provider


class ReceiptForm(forms.Form):
    date = forms.DateField(
        widget=forms.TextInput
        (attrs={'class': 'datepicker'}),
        label='Fecha'
    )
    observations = forms.CharField(
        required=False, max_length=100,
        label='Observaciones'
    )
    provider = forms.ModelChoiceField(
        queryset=Provider.objects.all()
    )
