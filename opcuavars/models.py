# coding: UTF-8
from __future__ import unicode_literals

from django.db import models
import requests
import json
import datetime
from django.utils import timezone



INIT_PIN = 0
END_PIN = 13

PINS = []
for i in range(INIT_PIN, END_PIN+1):
	PINS.append( ( ("%i") % i, "Patilla %i" % i ) )


DEV_TYPES = (
		("a", "Arduino"),
		("r", "Raspberry")
	)



class Device(models.Model):
	name = models.CharField(max_length=127, verbose_name='Nombre')
	dev_type = models.CharField(max_length=1, verbose_name='Tipo', choices=DEV_TYPES)
	ip = models.GenericIPAddressField()

	def __unicode__(self):
		return self.name+ " ["+self.ip+"]"

	class Meta:
		verbose_name = 'Dispositivo'
		verbose_name_plural = "Dispositivos"

	def update(self):
		try:
			#Petición http al dispositivo
			r = requests.get("http://"+self.ip+"/", timeout = 4.0)
		except requests.exceptions.Timeout:
			return False
			#si ha excedido el nº max de intentos erroneos
		except requests.exceptions.ConnectionError:
			print "máximo de conexiones excedido en "+self.name
			return False
		#Filtramos solo la devolución de variables
		variables = json.loads(r.text)["variables"]
		for k in variables:
			#Filtramos solo los métodos registrados
			query = Variable.objects.filter(method=k, dev=self)
			if query.exists():
				var = query[0]
				var.value = variables[k]
				var.timestamp = datetime.datetime.now()
				var.timestamp = timezone.now()
				var.save()
		return True



class Relay(models.Model):
	name = models.CharField(max_length=31, verbose_name="Nombre del relé")
	pin = models.CharField(choices=PINS, max_length=2)
	state = models.BooleanField(verbose_name='Encendido', default=False)
	dev = models.ForeignKey(Device, verbose_name='Dispositivo')

	class Meta:
		verbose_name = 'Relé'
		verbose_name_plural = "Relés"

	def __unicode__(self):
		return self.name


	def state_toggle(self):
		return  '<a href="#" class="relay-toggle" data-id="%s"><img src="/static/admin/img/icon-%s.svg" alt="False"></a>' % ( self.id , ("yes" if self.state else "no"))

	state_toggle.short_description = "Encendido/Apagado"
	state_toggle.allow_tags = True


class Variable(models.Model):
	name = models.CharField(max_length=31, verbose_name="Nombre de la variable")
	method = models.CharField(max_length=31, verbose_name="Nombre de la variable en la API")
	value = models.CharField(max_length=31, verbose_name='Ultimo valor', editable=False)
	timestamp = models.DateTimeField(editable=False, null=True, verbose_name='Última lectura realizada')
	dev = models.ForeignKey(Device, verbose_name='Dispositivo')


	class Meta:
		verbose_name = 'Variable'
		verbose_name_plural = "Variables"

	def __unicode__(self):
		return self.name

	#esto es mio 
	def get_value(self):
		return  "<span id='variable%s-value' >%s</span>" % (self.id , self.value)
	get_value.short_description = "Último valor"
	get_value.allow_tags = True

	def get_timestamp(self):
		return "<span id='variable%s-timestamp' >%s</span>" % (self.id , self.timestamp)
	get_timestamp.short_description = "Última lectura"
	get_timestamp.allow_tags = True

