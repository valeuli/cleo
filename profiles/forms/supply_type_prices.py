from django import forms
from profiles.models.supply_type_prices import MATERIAL_TYPE_CHOICES


class SupplyTypePricesForm(forms.Form):
    amount = forms.DecimalField(
        required=True, label='Monto',
        decimal_places=2,
        max_digits=10
    )
    quantify = forms.DecimalField(
        required=True, label='Cantidad de material',
        decimal_places=1,
        max_digits=4
    )
    supply_type = forms.ChoiceField(
        required=True,
        choices=MATERIAL_TYPE_CHOICES,
        label="Tipo de material"
    )