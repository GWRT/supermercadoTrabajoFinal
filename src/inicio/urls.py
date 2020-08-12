from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [ 
    path('',views.Inicio,name='Inicio'),
    path('inventario/',views.inventario.as_view(), name='inventario'),
    path('Contactos/',views.Contactos, name='Contactos'),
    path('Administracion/',views.Administracion, name='Administracion'),
]
