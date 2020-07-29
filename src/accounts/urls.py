from django.contrib import admin
from django.urls import path, include
from . import views
from .views import listProduct, updateProduct, addProduct, deleteProduct

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
]

