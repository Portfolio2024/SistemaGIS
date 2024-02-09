from django import forms
from .models import *

class catastroForm(forms.ModelForm):
    class Meta:
        model = Catastro
        fields = ['titulo', 'creador', 'files']