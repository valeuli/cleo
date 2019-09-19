from django import forms


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
