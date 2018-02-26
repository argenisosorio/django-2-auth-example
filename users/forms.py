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
            'style':'width: 100%; display: inline;',
        }), required = True)

    password = forms.CharField(widget=TextInput(attrs={
            'class':'form-control input-md',
            'style':'width: 100%; display: inline;','type':'password',
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
    username = forms.CharField(widget=TextInput(attrs={
            'value':'aosorio',
            'class':'form-control input-md',
            'style':'width: 100%; display: inline;',
        }), required = True)

    first_name = forms.CharField(widget=TextInput(attrs={
            'value':'argenis',
            'class':'form-control input-md',
            'style':'width: 100%; display: inline;',
        }), required = True)

    last_name = forms.CharField(widget=TextInput(attrs={
            'value':'osorio',
            'class':'form-control input-md',
            'style':'width: 100%; display: inline;',
        }), required = True)

    email = forms.CharField(widget=TextInput(attrs={
            'value':'aosorio@mail.com',
            'class':'form-control input-md',
            'style':'width: 100%; display: inline;',
        }), required = True)

    password1 = forms.CharField(widget=TextInput(attrs={
            'value':'arka.1234-d',
            'class':'form-control input-md',
            'style':'width: 100%; display: inline;','type':'password',
        }), required = True)

    password2 = forms.CharField(widget=TextInput(attrs={
            'value':'arka.1234-d',
            'class':'form-control input-md',
            'style':'width: 100%; display: inline;','type':'password',
        }), required = True)

    def save(self, commit = True):
        """
        Method that saves the data from the form.
        Active users is default.
        """
        user = User.objects.create_user(self.cleaned_data['username'],
                                     self.cleaned_data['email'],
                                     self.cleaned_data['password1'])
        #user.is_active = False
        #user.is_active = True
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
