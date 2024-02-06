from django import forms
from .models import *


class VolonterForm(forms.ModelForm):
    class Meta:
        model = Volonter
        fields = ['ime', 'prezime', 'godine', 'volonter_prije', 'projekt']

class ProjektForm(forms.ModelForm):
    class Meta:
        model = Projekt
        fields = ['naziv', 'datum_projekta', 'mjesto', 'opis']
        widgets = {
            'datum_projekta': forms.DateInput(attrs={'type': 'date'})
        }

class SkupinaForm(forms.ModelForm):
    volonteri = forms.ModelMultipleChoiceField(
        queryset=Volonter.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Volonterska_skupina
        fields = ['naziv', 'volonteri']
