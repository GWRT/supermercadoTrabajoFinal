from django.contrib import admin
from . import views
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', views.account, name='account'),
    path('cpassword', views.cpassword, name="cpassword")
]

