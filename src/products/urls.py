from django.contrib import admin
from django.urls import path, include
from . import views
from .views import listProductPDF, listProduct, updateProduct, addProduct, deleteProduct

urlpatterns = [
    path('',listProduct,name='listProduct'),
    path('addProduct',addProduct, name='addProduct'),
    path('updateProduct/<id>/',updateProduct, name='updateProduct'),
    path('deleteProduct/<id>/',deleteProduct, name='deleteProduct'),
    path('pdf/', listProductPDF.as_view(), name='tablaPDF'),

]
