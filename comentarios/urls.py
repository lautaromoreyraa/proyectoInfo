from django.urls import path
from . import views

app_name = 'comentarios'

urlpatterns = [
    path('agregar/<int:pk>', views.agregar_comentario, name='agregar'),
    path('Borrar/<int:comentario_id>', views.borrar_comentario, name='borrar_comentario'),
    path('Modificar/<int:comentario_id>', views.modificar_comentario, name='modificar_comentario'),
]