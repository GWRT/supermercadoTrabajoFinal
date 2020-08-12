from django.contrib import admin
from django.urls import path, include
from . import views
from pedidos.views import pedidos, checkout, listVentas

urlpatterns = [ 
    path('',views.Inicio,name='Inicio'),
    path('inventario/',views.inventario.as_view(), name='inventario'),
    path('Contactos/',views.Contactos, name='Contactos'),
    path('Administracion/',views.Administracion, name='Administracion'),
	path('pedidos/<int:pk>/',pedidos,name='pedidos'),
    path('checkout/<int:pk>/',checkout,name='checkout'),
    path('checkout/<int:pk>/',checkout,name='checkout'),
    path('listVentas/',listVentas.as_view(),name='listVentas'),
]
