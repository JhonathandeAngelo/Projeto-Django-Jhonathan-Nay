from django.db import models

class Smatphone(models.Model):
    modelo = models.CharField(max_length=150)
    marca = models.CharField(max_length=100)
    ano = models.IntegerField()
    cor = models.CharField(max_length=100,null=True)