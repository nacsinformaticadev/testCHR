from django.db import models

class Concesion(models.Model):
    numero = models.CharField(max_length=10)
    enlace = models.URLField()
    tipo = models.CharField(max_length=100)
    gobernacion_maritima = models.CharField(max_length=100)
    lugar = models.CharField(max_length=100)
    ds = models.CharField(max_length=100)
    tramite = models.CharField(max_length=100)
    concesionario = models.CharField(max_length=100)
    vigencia = models.CharField(max_length=100)
    #agregar mas campos si es necesario
    def __str__(self):
        return self.numero
    