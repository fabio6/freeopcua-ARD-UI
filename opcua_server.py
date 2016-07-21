#!/usr/bin/env python
# coding: UTF-8
import sys
import time
import logging
import logging.handlers
import logging.config
import argparse
import os
import requests
from opcua import ua, Server
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "arduino_ua_monitor.settings")
import django
django.setup()
import json
import datetime
from opcuavars.models import Relay, Variable, Device
from django.utils import timezone


def update_arduino_vars():
    fails = []
    for d in Device.objects.all():
        #Actualizamos cada dispositivo, llamando al método.
        if not d.update():
            fails.append(d)
        else:
            timedate = datetime.datetime.now()
            print "%s: Adquiridos datos de  %s" % (timedate, d.name)

    return fails


def update_objects(r_list, v_list, reles, variables):
    #LLamamos a la función de actualizacion de TODOS los dispositivos
    fails = update_arduino_vars()  
    if len(fails) != 0:
        for f in fails:
           print "Error: No se ha podido conectar con dispositivo: " + f.name
        return
    #Leemos la lista de objetos "relés"
    for r in Relay.objects.all():
        #Si el rele no existe en el servidor, se crea con el valor actual
        if not r.name in r_list:
            r_list[r.name] = reles.add_variable(idx, r.name, "Encendido" if r.state else "Apagado")

        #Si ya existe, actualiza valor
        else:
            r_list[r.name].set_value("Encendido" if r.state else "Apagado")

    #Leemos la lista de objetos "variable"
    for v in Variable.objects.all():
        #Si la variable no existe en el servidor, se crea con el valor actual
        if not v.name in v_list:
            v_list[v.name] = variables.add_variable(idx, v.name, v.value)
        #Si ya existe, actualiza valor
        else:
            v_list[v.name].set_value(v.value)




class MyLogger(object):
        def __init__(self, logger, level):
                self.logger = logger
                self.level = level

        def write(self, message):
                # Only log if there is a message (not just a new line)
                if message.rstrip() != "":
                        self.logger.log(self.level, message.rstrip())


#Para crear nuestro log:
LOG_FILENAME = "/var/log/opcua_server.log"
LOG_LEVEL = logging.INFO
logger = logging.getLogger(__name__)
logger.setLevel(LOG_LEVEL)
handler = logging.handlers.TimedRotatingFileHandler(LOG_FILENAME, when="W6", backupCount=2)
formatter = logging.Formatter('%(asctime)sUTC   %(levelname)-8s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
sys.stdout = MyLogger(logger, logging.INFO)




if __name__ == "__main__":
    #Creamos una instancia del servidor OPC UA
    server = Server()
    # Establecemos la comunicación de nuestro servidor opc ua 
    # load server certificate and private key. This enables endpoints
    #Cargamos el certificado del servidor y la clave privada
    #esto activa la comunicación con firma y cifrado.
    if len(sys.argv) == 2:
        server.set_endpoint("opc.tcp://%s" % sys.argv[1] )
        server.load_certificate("certificate-example.der")
        server.load_private_key("private-key-example.pem")
    elif len(sys.argv) == 3:
        server.set_endpoint("opc.tcp://%s" % sys.argv[1] )
        server.load_certificate("%s/certificate-example.der" % sys.argv[2])
        server.load_private_key("%s/private-key-example.pem" % sys.argv[2])
    else:
        a = len(sys.argv)
        print ("Numero de argumentos inexperado: %s" %a)
        print "opcua_server.py ip:puerto (rutacertificado)"
        sys.exit(1)

    # Declaración del espacio de nombres (no necesario)
    uri = "SERVIDOR OPC-UA - ARDUINO:FreeOpcUa:python-opcua"
    idx = server.register_namespace(uri)
    # Cargamos los objetos 
    objects = server.get_objects_node()
    # Cargamos nuestro espacio de direcciones.
    reles = objects.add_object(idx, "Reles")
    variables = objects.add_object(idx, "Variables")
    #Carga de reles y de Variables
    relay_list = {}
    for r in Relay.objects.all():
        relay_list[r.name] = reles.add_variable(idx, r.name, "Encendido" if r.state else "Apagado")
    variable_list = {}
    for v in Variable.objects.all():
        variable_list[v.name] = variables.add_variable(idx, v.name, v.value)

    time.sleep(30)
    os.system("cat /dev/null > /var/log/opcua_server.log")
    # Iniciando servidor
    print "Iniciando servidor OPC-Ua..."
    server.start()
    print "¡¡¡¡¡Servidor Iniciado!!!!!"
    try:
        while True:
            time.sleep(1)
            update_objects(relay_list, variable_list, reles, variables)
    except Exception as e:
        print e
    finally:
        #Cerramos conexión, eliminamos subscripciones, etc. 
        print "......Cerrando servidor....   "
        server.stop()
        sys.exit(1)





