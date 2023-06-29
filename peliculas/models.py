from django.db import models
from generos.models import Genero
from django.core.exceptions import ValidationError

# Create your models here.

class Pelicula(models.Model):
    titulo = models.CharField(max_length=128)
    anhio = models.IntegerField()
    director = models.CharField(max_length=128)
    generos = models.ManyToManyField(Genero)

    class Meta:
        ordering = ['titulo',  'anhio', 'director']
        
    def __str__(self):
        return self.titulo
