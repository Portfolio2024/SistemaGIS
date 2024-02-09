from django import forms
from .models import *

class TransmisionForm(forms.ModelForm):
    class Meta:
        model = Transmision
        fields = ['titulo', 'creador', 'files']
        

class Transmision1Form(forms.ModelForm):
    class Meta:
        model = Transmision1
        fields = ['titulo', 'creador', 'files']