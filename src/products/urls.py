from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.products,name='products'),
    path('addProduct',views.addProduct, name='addProduct'),
    path('updateProduct/<int:theid>/',views.updateProduct, name='updateProduct'),
    path('deleteProduct/<int:theid>/',views.deleteProduct, name='deleteProduct'),
]
