from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    full_name = forms.CharField(max_length=255)
    cuca = forms.CharField(max_length=255)

    class Meta:
        model = CustomUser
        fields = ('username', 'full_name', 'cuca', 'email', 'password1', 'password2')