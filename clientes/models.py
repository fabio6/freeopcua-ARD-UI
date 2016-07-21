# coding: UTF-8
from __future__ import unicode_literals

from django.db import models

class Cliente(models.Model):
	nombre = models.CharField(max_length=127, verbose_name='Nombre completo del cliente')
	dni = models.CharField(max_length=9, verbose_name='DNI')
	direccion = models.CharField(max_length=127, verbose_name='Dirección postal')
	comentario = models.TextField(blank=True)


	def __unicode__(self):
		return self.nombre + ": " + self.comentario