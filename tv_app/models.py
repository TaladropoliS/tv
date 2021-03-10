from django.db import models

# Create your models here.

class Programa(models.Model):
    titulo = models.CharField(max_length=255)
    canal = models.CharField(max_length=255)
    fecha = models.DateField(max_length=10)
    desc = models.TextField(max_length=600)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)