"""odontologia URL Configuration

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
from django.conf.urls import include, url
from apps.odontologia.views import Home
from apps.paciente.views import Paciente
from apps.empleado.views import Empleado
from apps.administrador.views import Administrador
from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.views.generic.base import TemplateView
from django.urls import path, include
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('odontologia/', include(('apps.odontologia.urls','odontologia'))),
    path('administrador/', include(('apps.administrador.urls','administrador'))),
    path('paciente/', include(('apps.paciente.urls','paciente'))),
    path('empleado/', include(('apps.empleado.urls','empleado'))),
    path('', Home, name = 'index'),
    path('paciente/', Paciente, name = 'paciente'),
    path('administrador/', Administrador, name = 'administrador'),
    path('empleado/', Empleado, name = 'empleado')

    
    ##url('web/', include('django.contrib.auth.urls')),
    ##path('accounts/', include('accounts.urls')),
    ##path('', TemplateView.as_view(template_name='home.html'), name='home'),
    ##path('', TemplateView.as_view(template_name='admin.html'), name='admin'),
    ##url('', include('web.urls')),
	
    ]

