from django import forms
from profiles.models.bank_account import ACCOUNT_TYPE
from profiles.models.person import DOCUMENT_TYPE_CHOICES


class BankAccountForm(forms.Form):

    bank_name = forms.CharField(
        required=True, max_length=59, label="Nombre del Banco"
    )
    account_type = forms.ChoiceField(
        required=False,
        choices=ACCOUNT_TYPE,
        label="Tipo de cuenta"
    )
    account_number = forms.CharField(
        required=True, max_length=20, label="Número de cuenta"
    )
    name = forms.CharField(
        required=True, max_length=100, label="Nombre y apellido"
    )
    document_type = forms.ChoiceField(
        required=True,
        choices=DOCUMENT_TYPE_CHOICES,
        label="Tipo de Documento"
    )

    document_code = forms.IntegerField(
        required=True, label="Número de Document"
    )