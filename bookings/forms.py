from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    code = forms.CharField(max_length=20, required=False, help_text='Enter your code if you are an employee.')

    class Meta:
        model= User
        fields = ('username', 'password1', 'password2', 'code')