# coding: UTF-8
from django.contrib import admin
from .models import *


class AdminRelay(admin.ModelAdmin):
	list_display = ("name", "pin", "state_toggle", "dev")

	class Media:
		js = ['/static/js/opcuavars.js',]

admin.site.register(Relay, AdminRelay)


class AdminVariable(admin.ModelAdmin):
	list_display = ("name","get_value", "get_timestamp", "dev")

	class Media:
		js = ['/static/js/update_vars.js',]

admin.site.register(Variable, AdminVariable)


class AdminDevice(admin.ModelAdmin):
	list_display = ("name","dev_type", "ip")

admin.site.register(Device, AdminDevice)