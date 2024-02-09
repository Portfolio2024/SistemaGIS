from django import forms
from .models import *

class Sistema_AisladoForm(forms.ModelForm):
    class Meta:
        model = Sistema_Aislado
        fields = ['titulo', 'creador', 'files']