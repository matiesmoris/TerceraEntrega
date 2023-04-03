"""Proyecto3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from Entrega3.views import (mostrar_mis_tareas, mostrar_personas, crear_persona, BuscarPersonas, ProductoList, ProductoDetail, ProductoUpdate, ProductoCreate, ProductoDelete, mostrar_productos, BuscarProductos)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ProductoList.as_view(), name='producto-list'),
    path('mis-tareas/<criterio>', mostrar_mis_tareas, name="mis-tareas"),
    path('personas', mostrar_personas, name="personas"),
    path('personas/create', crear_persona, name="personas-create"),
    path('personas/list', BuscarPersonas.as_view(), name="personas-list"),
    path('producto', mostrar_productos, name="productos"),  
    path('producto/list', BuscarProductos.as_view(), name="producto-list"),
    path('producto/<pk>/detail', ProductoDetail.as_view(), name="producto-detail"),
    path('producto/create', ProductoCreate.as_view(), name="producto-create"),
    path('producto/<pk>/update', ProductoUpdate.as_view(), name="producto-update"),
    path('producto/<pk>/delete', ProductoDelete.as_view(), name="producto-delete"),
]
