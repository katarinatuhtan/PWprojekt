from django import forms
from .models import *

class VolonterForm(forms.ModelForm):
    class Meta:
        model = Volonter
        fields = ['ime', 'prezime', 'godine', 'volonter_prije', 'projekt']
