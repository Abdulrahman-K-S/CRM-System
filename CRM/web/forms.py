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
    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user is None:
            self.fields['client_category'].queryset = models.Category.objects.none()
        elif user.is_superuser:
            self.fields['client_category'].queryset = models.Category.objects.all()
        else:
            self.fields['client_category'].queryset = models.Category.objects.filter(
                category_owner=user
            )


class UpdateClientForm(forms.ModelForm):
    class Meta:
        model = models.Client
        fields = ['client_first_name', 'client_last_name', 'client_email', 'client_phone_number', 'client_address', 'client_category']


class CreateCategoryForm(forms.ModelForm):
    class Meta:
        model = models.Category
        fields = ['category_name']
