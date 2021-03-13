from __future__ import unicode_literals
from django.db import models
from datetime import date

# Create your models here.

class TvManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['titulo']) < 2:
            errors["titulo"] = "Ingresar Título, mínimo 2 caracteres."
        if len(postData['canal']) < 3:
            errors["canal"] = "Ingresar Canal, mínimo 3 caracteres."
        if len(postData['fecha']) < 8:
            errors["fecha"] = "Ingresar Fecha, no superior a la de hoy."
        if len(postData['desc']) < 1:
            return errors
        else:
            if len(postData['desc']) < 10:
                errors["desc"] = "Ingresar Descripción, mínimo 10 caracteres."
            return errors

class Programa(models.Model):
    titulo = models.CharField(max_length=255)
    canal = models.CharField(max_length=255)
    fecha = models.DateField(max_length=10)
    desc = models.TextField(max_length=600)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = TvManager()