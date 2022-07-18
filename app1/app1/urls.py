"""app1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from appweb1.views import paginaprincipal
from paciente.views import detalle_paciente, nuevo_paciente, modificar_paciente, eliminar_paciente, reporte_paciente

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', paginaprincipal, name='inicio'),
    path('detalle_paciente/<int:id>', detalle_paciente, name='detalle_paciente'),
    path('nuevo_paciente/', nuevo_paciente, name='nuevo_paciente'),
    path('modificar_paciente/<int:id>', modificar_paciente, name='modificar_paciente'),
    path('eliminar_paciente/<int:id>', eliminar_paciente, name='eliminar_paciente'),
    path('reporte_paciente/', reporte_paciente, name='reporte_paciente'),
]
