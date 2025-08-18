from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms.widgets import TextInput, PasswordInput
from . import models


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())


class CreateClientForm(forms.ModelForm):
    class Meta:
        model = models.Client
        fields = ['client_first_name', 'client_last_name', 'client_email', 'client_phone_number', 'client_address', 'client_category']


class UpdateClientForm(forms.ModelForm):
    class Meta:
        model = models.Client
        fields = ['client_first_name', 'client_last_name', 'client_email', 'client_phone_number', 'client_address', 'client_category']
