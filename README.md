Instalación y ejeccución FreeOPCUA para dispositivos Arduino con interfaz web. Instalación unicamente para linux, testeado en Debian.
15/07/2016


Para una correcta instalación ejecute paso a paso.

1.-REQUERIMIENTOS PREVIOS
--------------------------
El equipo debe tener instalado algunas librerias y paquetes:

	apt-get update && sudo apt-get upgrade
	apt-get install build-essential libssl-dev python-dev python-setuptools
	easy_install pip



2.-INSTALACIÓN DE REQUERIMIENTOS
---------------------------------
Esto instalará todos los paquetes necesarios de python.
		
	pip install -r requirements.txt
	pip freeze --local | grep -v '^\-e' | cut -d = -f 1  | xargs pip install -U



3.-MIGRAR BASES DE DATOS
-------------------------
Esto hará la sincronización de los modelos con el esquema en la base de datos:

	./manage.py migrate



4.-CREACIÓN DE USUARIO PARA LA INTERFAZ
----------------------------------------
Ejecución para la creación del super usuario en la interfaz web:

	./manage.py createsuperuser



5.-INSTALACIÓN SERVIDOR OPC UA e INTERFAZ COMO SERVICIO DEL SISTEMA 
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

