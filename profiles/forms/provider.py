from django import forms
from phonenumber_field.formfields import PhoneNumberField
from profiles.models.person import DOCUMENT_TYPE_CHOICES
from profiles.models import Person


class ProviderForm(forms.Form):
    document_number = forms.CharField(
        required=True, max_length=15, label="Número de Documento"
    )
    document_type = forms.ChoiceField(
        required=True,
        choices=DOCUMENT_TYPE_CHOICES,
        label="Tipo de documento"
    )
    name = forms.CharField(
        required=True, max_length=59, label="Nombre y apellido"
    )
    mobile_phone = PhoneNumberField(
        required=True, label="Número de teléfono móvil"
    )
    home_phone = PhoneNumberField(
        required=False, label="Número de teléfono fijo"
    )
    email = forms.EmailField(
        required=True, label="Correo electrónico"
    )

    def clean_unique_document(self):
        qs = Person.objects.filter(
            document_number=self.cleaned_data['document_number'],
            document_type=self.cleaned_data['document_type']
        )
        if qs.exists():
            self.add_error(
                'document_number', 'Identity document already exists.'
                           )

    def clean(self):
        super(ProviderForm, self).clean()
        self.clean_unique_document()
