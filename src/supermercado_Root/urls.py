"""supermercado_Root URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from provider.views import providers, modificar, eliminar, create
from categoria.views import categories, crearCategoria, modificarCategoria, eliminarCategoria
from indexPagina.views import home
from accounts.views import login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',login, name='login'),
    path('home', home, name='homePage'),
    path('provider/', providers, name='provider'),
    path('crear/', create, name='crearProveedor'),
    path('modificar/<id>/', modificar, name='modificarProveedor'),
    path('eliminar/<id>/', eliminar, name='eliminarProveedor'),
    path('category/', categories, name='category'),
    path('crearCategoria', crearCategoria, name='crearCategoria'),
    path('modificarCategoria/<id>/', modificarCategoria, name='modificarCategoria'),
    path('eliminarCategoria/<id>/', eliminarCategoria, name='eliminarCategoria'),
    path('products/',include('products.urls')),
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
