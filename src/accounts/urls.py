from django.contrib import admin
from . import views
from django.urls import path, include
from .views import *

urlpatterns = [
<<<<<<< HEAD
    path('', views.account, name='account'),
    path('cpassword', views.cpassword, name="cpassword")
=======
    path('signup', views.signup, name='singup'),
    path('signin', views.signin, name='singin'),
    path('logout', views.logout, name='logout'),
>>>>>>> rama4
]

