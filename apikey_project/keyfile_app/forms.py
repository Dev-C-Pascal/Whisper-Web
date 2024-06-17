from django import forms
from .models import ApiKey

class ApiKeyForm(forms.ModelForm):
    class Meta:
        model = ApiKey
        fields = ['key', 'file']
