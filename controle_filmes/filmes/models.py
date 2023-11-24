from django.db import models

class Filme(models.Model):
    titulo = models.CharField(max_length=100, unique=True)
    data_assistido = models.DateField(null=True, blank=True)
    gostaria_assistir = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo

