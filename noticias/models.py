from django.db import models
from django.contrib.auth.models import User


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__ (self):
        return self.nombre


class Noticia(models.Model):

    creado = models.DateTimeField(
        'creado',
        auto_now_add = True
    )

    editado = models.DateField(
        'editado',
        auto_now = True
    )

    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
    #imagen = models.ImageField(upload_to = 'noticias')
    #categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__ (self):
        return self.titulo + '-hecho por: ' + self.user.username
