"""
URL configuration for ProyectoFinal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from noticias import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    #General
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    #Noticias
    path('noticias/', views.noticias, name='noticias'),
    path('noticias/detalle/<int:pk>', views.noticia_detalles, name='noticia_detalles'),
    path('noticias/crear', views.crear_noticia, name='crear_noticia'),
    path('noticias/editar/<int:pk>', views.noticia_editar, name='noticia_editar'),
    path('noticias/borrar/<int:pk>', views.borrar_noticia, name='borrar_noticia'),
    #Usuarios
    path('singup/', views.singup, name='singup'),
    path('logout/', views.cerrar_sesion, name='logout'),
    path('singin/', views.abrir_sesion, name='singin'),
    #Comentarios
    path('Comentarios/', include('comentarios.urls')),
] 
urlpatterns += staticfiles_urlpatterns()