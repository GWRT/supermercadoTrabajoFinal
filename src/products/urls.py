from django.contrib import admin
from django.urls import path, include
from . import views
from .views import listProduct, updateProduct, addProduct, deleteProduct, listProductPDF

urlpatterns = [
    path('',listProduct.as_view(),name='listProduct'),
    path('addProduct',addProduct.as_view(), name='addProduct'),
    path('updateProduct/<int:pk>/',updateProduct.as_view(), name='updateProduct'),
    path('deleteProduct/<int:pk>/',deleteProduct.as_view(), name='deleteProduct'),
    path('pdf/', listProductPDF.as_view(), name='tablaPDF'),
]
