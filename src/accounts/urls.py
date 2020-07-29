from django.contrib import admin
from . import views
from django.urls import path, include
from .views import signup, logout, signin

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('logout', views.logout, name='logout'),
]

