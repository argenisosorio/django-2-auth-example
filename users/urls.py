# -*- coding: utf-8 -*-
from django.urls import path
from users import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', login_required(views.Index.as_view()), name='index'),
    path('login/', views.Login.as_view(), name='login'),
    path('register/', views.Register.as_view(), name='register'),
    path('logout/', views.Logout.as_view(), name='logout'),
]
