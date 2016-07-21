from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse
from .models import *
import requests
from django.core import serializers
import datetime
import json


from django.utils import timezone


@staff_member_required
def relay_toggle(request):
	id = request.POST["id"]
	r = Relay.objects.get(id=id)
	if r.state:
		r.state = False
		r.save()
		out = "no"
		ardu_off(r.pin, r.dev.ip)
	else:
		r.state = True 
		r.save()
		ardu_on(r.pin, r.dev.ip)
		out = "yes"

	return HttpResponse(out)


@staff_member_required
def update_vars(request):
	fails = update_arduino_vars()
	data = ""
	if len(fails) == 0:
		data = serializers.serialize("json", Variable.objects.all(), fields=("value", "timestamp"))
	else:
		for f in fails:
			data += "Error: No se ha podido conectar con dispositivo: " + f.name +". "
	return HttpResponse(data)


def ardu_on(pin, ip):
	host = "http://"+ip+"/"
	requests.get('%smode/%s/o' % (host,pin), timeout=4 )
	requests.get('%sdigital/%s/1' % (host,pin), timeout=4 )

def ardu_off(pin, ip):
	host = "http://"+ip+"/"
	requests.get('%smode/%s/o' % (host,pin), timeout=4 ) 
	requests.get('%sdigital/%s/0' % (host,pin), timeout=4 )


def update_arduino_vars():
	#HOST = "http://192.168.2.3/"
	fails = []
	for d in Device.objects.all():
		if not d.update():
			fails.append(d)

	return fails

	