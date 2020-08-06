from django.contrib import admin
from . import views
from django.urls import path, include
from .views import *

urlpatterns = [
	path('', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('logout', views.logout, name='logout'),
]

