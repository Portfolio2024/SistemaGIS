from django import forms
from .models import KMLFile

class KMLFileForm(forms.ModelForm):
    class Meta:
        model = KMLFile
        fields = ['file']
