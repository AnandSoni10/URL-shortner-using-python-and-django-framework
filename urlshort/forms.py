from django import forms
from .models import ShortURl

class CreateNewShortURL(forms.ModelForm):
    class Meta:
        model=ShortURl
        fields = {'original_URL'}

        widgets = {
            'original_URL': forms.TextInput(attrs={'class': 'form-control'})
        }