from django.contrib import admin
from django.urls import path, include
from . import views
<<<<<<< HEAD
from .views import listProductPDF, listProduct, updateProduct, addProduct, deleteProduct
=======
from .views import listProduct, updateProduct, addProduct, deleteProduct, listProductPDF
>>>>>>> 459d354b9c2272a5fc640cded2edff0c46bcfa03

urlpatterns = [
    path('',listProduct.as_view(),name='listProduct'),
    path('addProduct',addProduct.as_view(), name='addProduct'),
    path('updateProduct/<int:pk>/',updateProduct.as_view(), name='updateProduct'),
    path('deleteProduct/<int:pk>/',deleteProduct.as_view(), name='deleteProduct'),
    path('pdf/', listProductPDF.as_view(), name='tablaPDF'),
<<<<<<< HEAD

=======
>>>>>>> 459d354b9c2272a5fc640cded2edff0c46bcfa03
]
