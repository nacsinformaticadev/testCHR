from django.db import models

class Jurisprudencia(models.Model):
    titulo = models.CharField(max_length=255)
    fecha = models.DateField()
    fuente = models.CharField(max_length=255)
    contenido = models.TextField()

    def __str__(self):
        return self.titulo