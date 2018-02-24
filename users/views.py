# -*- coding: utf-8 -*-
from django.views.generic import View, ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic
from django.shortcuts import render, redirect
from django.contrib.auth import forms, login, logout, authenticate
from users.forms import LoginForm


class Index(TemplateView):
    """
    Class that shows the start template.
    """
    template_name = "users/index.html"


class Login(View):
    """
    Class that manages user authentication.
    """
    form = LoginForm

    def get(self, request):
        """
        Method that manages access by get.
        """
        context = {'form' : self.form()}
        #print ("enter in get......................")
        return render(request, 'users/login.html', context)

    def post(self, request):
        """
        Method that manages access by post.
        """
        form = self.form(None, request.POST)
        context = {'form': form}
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                #print ("authenticated......................")
                return redirect('/')
            else:
                #print ("no login......................")
                return redirect('/')
        else:
            #print ("invalid data......................")
            return redirect('/')


class Logout(View):
    """
    Class that manages user logout.
    """

    def get(self, request):
        """
        Method that redirects after the close of session.
        """
        logout(request)
        return redirect('/')
