from django import forms
from .models import *

class MediaTension1Form(forms.ModelForm):
    class Meta:
        model = MediaTension1
        fields = ['titulo', 'creador', 'files']
        

class MediaTension2Form(forms.ModelForm):
    class Meta:
        model = MediaTension2
        fields = ['titulo', 'creador', 'files']


class MediaTension3Form(forms.ModelForm):
    class Meta:
        model = MediaTension3
        fields = ['titulo', 'creador', 'files']

class MediaTension4Form(forms.ModelForm):
    class Meta:
        model = MediaTension4
        fields = ['titulo', 'creador', 'files']