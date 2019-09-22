from django import forms
from phonenumber_field.formfields import PhoneNumberField
from profiles.models.provider import DOCUMENT_TYPE_CHOICES


class InterviewForm(forms.Form):
    date = forms.DateField(
        widget=forms.TextInput
        (attrs={'class': 'datepicker'}),
        label='Fecha'
    )
    observations = forms.CharField(
        required=False, max_length=100,
        label='Observaciones'
    )
    name = forms.CharField(
        required=True, max_length=59, label="Nombre y apellido"
    )
    mobile_phone = PhoneNumberField(
        required=True, label = "Número de celular"
    )
    home_phone = PhoneNumberField(
        required=False, label= "Teléfono fijo"
    )
