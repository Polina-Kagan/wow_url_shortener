from django import forms
from django.contrib.auth.models import User
from .models import ShortLink

class LinkCreationForm(forms.ModelForm):
    original_url = forms.CharField(label="Long Link:", required=True,  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'NO MORE than 250 characters'}))
    short_code = forms.CharField(label="Short Word:", required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Max 50 characters'}))

    class Meta:
        model= ShortLink
        fields = ['original_url', 'short_code']