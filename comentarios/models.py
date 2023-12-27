from django.db import models
from django.contrib.auth.models import User
from noticias.models import Noticia

# Create your models here.

class Comentario(models.Model):
    creado = models.DateTimeField(
        'creado',
        auto_now_add = True
    )

    editado = models.DateTimeField(
        'editado',
        auto_now = True
    )

    comentario = models.TextField(max_length=400)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE)

    def __str__(self):
        return self.textoComentario + 'Escrito por: ' + self.usuario
