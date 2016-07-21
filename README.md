# freeopcua-ARD-UI
Instalación y ejeccución FreeOPCUA para dispositivos Arduino con interfaz web. Solo para equipos DEBIAN.
15/07/2016


1.-REQUERIMIENTOS PREVIOS
----------------------

El equipo debe tener instalado pyhton 2.7 y además el paquete pip:
	
	apt-get install python-pip



2.-MIGRAR BASES DE DATOS
-------------------------

Esto hará la sincronización de los modelos con el esquema en la base de datos.

	./manage.py migrate



3.-INSTALACIÓN DE REQUERIMIENTOS
---------------------------------
Esto instalará todos los paquetes necesarios de python.
	pip installa -r requirements.txt



4.-INSTALACIÓN SERVIDOR OPC UA e INTERFAZ COMO SERVICIO DEL SISTEMA 
--------------------------------------------------------------------
Ejecución siguiento los pasos:

	./install.py




LOGs
-----
Visualización de las últimas 50 líneas de nuestros logs

Log de la interfaz web
	tail -50 /var/log/webinterface.log

Log del servidor opc ua
	tail -50 /var/log/opcua_server.log 
