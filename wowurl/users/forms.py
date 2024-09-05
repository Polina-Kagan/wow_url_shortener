from django import forms
from django.contrib.auth.models import User

class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(label="Name:", required=True, help_text="Required field. No more than 150 characters. Only letters, numbers and symbols @/./+/-/_.", widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="Email:", required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Password:",help_text="Your password must not match your name. Your password must be at least 8 characters long. Your password cannot consist only of numbers.", required=True,  widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
