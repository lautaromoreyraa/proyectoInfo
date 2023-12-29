from django.db import models
from django.contrib.auth.models import User



class Noticia(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)



    def __str__ (self):
        return self.titulo + '-hecho por: ' + self.user.username