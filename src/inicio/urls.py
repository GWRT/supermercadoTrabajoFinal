from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [ 
    path('',views.Inicio,name='Inicio'),
    path('inventario/',views.inventario.as_view(), name='inventario'),
    path('Contactos/',views.Contactos, name='Contactos'),
    path('Administracion/',views.Administracion, name='Administracion'),
    path('update_item/',views.update_item, name='update_item'),
    path('cart/',views.cart, name='cart'),
    path('checkout/',views.checkout, name='checkout'),
]
