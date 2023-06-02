from django.forms import ModelForm
from .models import Auto


class AutoForm(ModelForm):
    class Meta:
        model = Auto
        fields = ['marka', 'rok_produkcji', 'opis', 'premiera', 'oceny', 'w_sprzedazy']