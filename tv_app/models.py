from __future__ import unicode_literals
from django.db import models

# Create your models here.

class TvManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['titulo']) < 1:
            errors["titulo"] = "Debes ingresar el Título"
        if len(postData['canal']) < 1:
            errors["canal"] = "Debes ingresar el Canal"
        if len(postData['fecha']) < 1:
            errors["fecha"] = "Debes ingresar una Fecha"
        if len(postData['desc']) < 1:
            errors["desc"] = "Debes ingresar una Descripción"
        return errors

class Programa(models.Model):
    titulo = models.CharField(max_length=255)
    canal = models.CharField(max_length=255)
    fecha = models.DateField(max_length=10)
    desc = models.TextField(max_length=600)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = TvManager()