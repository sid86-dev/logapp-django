from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.home, name='home'),
    path("login", views.loginuser, name='login'),
    path("logout", views.logoutuser, name='logout'),
    path("signup", views.signupuser, name='signup'),
]