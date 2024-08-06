"""
URL configuration for desafio2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from desafioadl.views import index, subtarea, listado, eliminar_tarea, eliminar_subtarea, modificar_tarea, modificar_subtarea

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index),
    path("subtarea/", subtarea),
    path("listado/", listado),
    path('eliminar_tarea/<int:id>/', eliminar_tarea, name='eliminar_tarea'),
    path('eliminar_subtarea/<int:id>/', eliminar_subtarea, name='eliminar_subtarea'),
    path('modificar_tarea/<int:id>/', modificar_tarea, name='modificar_tarea'),
    path('modificar_subtarea/<int:id>/', modificar_subtarea, name='modificar_subtarea'),
]
