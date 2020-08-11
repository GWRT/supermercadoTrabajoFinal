from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.inventory, name='inventory'),
    path('update/<int:pk>/',views.update,name='update'),

]
