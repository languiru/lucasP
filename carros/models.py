# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Fabricante(models.Model):
    nome = models.CharField(max_length = 300, null=True)
    def __str__(self):
        return self.nome




class Carro(models.Model):
    nome = models.CharField(max_length=300)
    valor = models.DecimalField(max_digits=19,decimal_places=2, null=True)
    ano = models.IntegerField(null=True)
    modelo = models.CharField(max_length=300,null=True)
    fabricante = models.ForeignKey(Fabricante, null=True)
    caracteristicas = models.CharField(max_length=300, null=True)

    def __str__(self):
        return self.nome


