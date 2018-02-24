# -*- coding: utf-8 -*-
from django import forms
from django.forms import (
    TextInput, CharField, Select, RadioSelect, Textarea, CheckboxInput
)
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


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
