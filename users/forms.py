# -*- coding: utf-8 -*-
from django import forms
from django.forms import (
    TextInput, CharField, Select, RadioSelect, Textarea, CheckboxInput
)
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm


class LoginForm(AuthenticationForm):
    """
    Form that manages the User model fields.
    """
    username = forms.CharField(widget=TextInput(attrs={
            'class':'form-control input-md',
            'style': 'width: 100%; display: inline;',
        }), required = True)

    password = forms.CharField(widget=TextInput(attrs={
            'class':'form-control input-md',
            'style': 'width: 100%; display: inline;','type':'password',
        }), required = True)

    class Meta:

        model = User

        fields = [
            'username',
            'password',
        ]


class RegisterForm(UserCreationForm):
    """
    Form that manages the User creation.
    """
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')
    email = forms.EmailField(label='Email Address')


    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

