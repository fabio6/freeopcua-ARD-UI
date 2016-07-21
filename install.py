#!/usr/bin/env python
# coding: UTF-8
import os
import sys
from netifaces import interfaces, ifaddresses, AF_INET

def menuIP(list_ip):
    print ("\nSelecciona opción IP de la interfaz para el SERVIDOR OPC-UA" )
    for indice in list_ip:
        print 'Opcion [%s] --> Interface: %s  IP: %s\t ' % (indice,list_ip[indice][0],list_ip[indice][1])

def get_ip_puerto():
    list_ip = {}

    for k,ifaceName in enumerate(interfaces()):
        addresses = [i['addr'] for i in ifaddresses(ifaceName).setdefault(AF_INET, [{'addr':'No IP addr'}] )]
        list_ip[k] = [ifaceName,addresses[0]]
    
    menuIP(list_ip)
    opcion = int(input())
    while (True):
        if (opcion < len(list_ip) ):
            ip = str(list_ip[opcion][1])
            break
        else:
            print "Introduce una opcion valida"
            menuIP(list_ip)
            opcion = int(input())
    puerto =raw_input("Introduce el Puerto del servidor OPC-UA: ")
    return ip+":"+puerto


def get_daemon_opts(out):
	p = os.getcwd()
	out.write("DAEMON_OPTS="+"'"+get_ip_puerto()+" "+p+"'"+"\n")

def get_source (out):
	if not ENV==None :
		out.write( "		source "+ENV+"\n")

def set_ENV (l, out):
	t= raw_input ("¿Usa entorno virtual? pulse [S] Si o [N] No: \n")
	if t[0] == 's' or t[0] == 'S':
		e = raw_input( "Escribe la ruta absoluta al script de activación del entorno:")
		if e[0] != "/":  e="/"+e
		out.write("ENV="+e+"\n")
		global ENV
		ENV = e

def get_daemon(out):
	p = os.getcwd()
	out.write("DAEMON="+p+"/opcua_server.py""\n")

ENV=None

def get_projectloc(out):
	p = os.getcwd()
	out.write("PROJECTLOC="+p+"\n")

def get_source2 (out):
	if not ENV==None:
		out.write("	source "+ENV+"\n")

def get_path(out):
	p = os.getcwd()
	out.write("PATH="+p+"\n")

def processline(line, out):
	if "__PATH__" in line:
		get_path(out)

	elif "__DAEMON__" in line:
		get_daemon(out)

	elif "__ENV__" in line:
		set_ENV(line, out)

	elif "__SOURCE__" in line:
		get_source(out)

	elif "__DAEMON_OPTS__" in line:
		get_daemon_opts(out)

	elif "__PROJECTLOC__" in line:
		get_projectloc(out)

	elif "__SOURCE2__" in line:
		get_source2(out)

	else:
		out.write(line)


if __name__ == "__main__":

	if os.geteuid() != 0:
		print "Debes tener privilegios root para ejecutar esta instalación"
		sys.exit(1)
	else:
		print "Bienvenidos a la instalación del Servidor OPC UA y su Interfaz WEB"

	# Generando script del servidor opc-ua a partir de conf.tpl
	out = open ("script_opcua", "wb")
	with open('conf.tpl') as fp:
	    for line in fp:
	        processline(line,out)
	out.close()

	# Generando script del servidor web  a partir de conf-web.tpl
	out = open ("script_web", "wb")
	with open ('conf-web.tpl') as f:
		for line in f:
			processline(line, out)
	out.close()

	#Ejecuciones
	os.system("rm /var/log/webinterface*")
	os.system("rm /var/log/opcua_server*")
	os.system("chmod 777 script_opcua")
	os.system("chmod 777 script_web")
	os.system("cp script_opcua /etc/init.d/")
	os.system("cp script_web /etc/init.d/")
	os.system("cd /etc/init.d/")
	os.system("update-rc.d script_opcua defaults")
	os.system("update-rc.d script_web defaults")
	os.system("systemctl daemon-reload")
	q= raw_input ("¿Quiere ejecutar estos dos servicios? pulse [S] Si o [N] No: ")
	if q[0] == 's' or q[0] == 'S':
		os.system("service script_opcua start")
		os.system("service script_web start")
		print "¡¡¡Servicios iniciados!!!"
		print "Loggins: /var/log/webinterface.log y /var/log/opcua_server.log"
		"Instalación finalizada"
	else:
		print "Para inicializar los servicios utilice: service <servicio> star"
		print "Servicios: <script_web> y <script_opcua> respectivamente"
		print "Instalación finalizada"	
