Instalación y ejeccución FreeOPCUA para dispositivos Arduino con interfaz web. Solo para equipos DEBIAN.
15/07/2016


Para una correcta instalación ejecute paso a paso.

1.-REQUERIMIENTOS PREVIOS
--------------------------

El equipo debe tener instalado algunas librerias y paquetes:
	
	apt-get update && sudo apt-get upgrade
	apt-get install build-essential
	apt-get install python-dev
	apt-get install libssl-dev
	easy_install pip



2.-MIGRAR BASES DE DATOS
--------------------------

Esto hará la sincronización de los modelos con el esquema en la base de datos.

	./manage.py migrate




3.-INSTALACIÓN DE REQUERIMIENTOS
---------------------------------
Esto instalará todos los paquetes necesarios de python.
		
	pip install -r requirements.txt
	pip freeze --local | grep -v '^\-e' | cut -d = -f 1  | xargs pip install -U


4.-INSTALACIÓN SERVIDOR OPC UA e INTERFAZ COMO SERVICIO DEL SISTEMA 
--------------------------------------------------------------------
Ejecución siguiento los pasos:

	./install.py



5.-CREACIÓN DE USUARIO PARA LA INTERFAZ
----------------------------------------

	./manage.py createsuperuser





LOGs
-----
Visualización de las últimas 50 líneas de nuestros logs

Log de la interfaz web
	tail -50 /var/log/webinterface.log

Log del servidor opc ua
	tail -50 /var/log/opcua_server.log 

