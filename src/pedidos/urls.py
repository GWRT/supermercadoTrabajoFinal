from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.pedidos,name='pedidos'),
    path('checkout/<int:pk>/',views.checkout,name='checkout'),
]
