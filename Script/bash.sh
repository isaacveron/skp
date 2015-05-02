#!/bin/bash
menu ()
{	
	echo "\nElija el numero de la accion que desea realizar"
	echo ' 1 Crear BD skp'
	echo ' 2 Cargar BD'
	echo ' 3 Crear un backup de la BD'
	echo ' 4 Eliminar BD'
	echo ' 5 Iniciar Sistema'
	echo ' 6 Salir'
}

alerta ()
{
	echo 'Opcion no valida, porfavor ingrese una opcion valida'
}

usuario_BD='root'
usuario='isaac'
echo "#########Bienvenido al Sistema skp#########"
while [ "$OPT" != 6 ]
do
	menu
	read OPT
	case $OPT in
		1 )	
			sudo -u "$usuario_BD" createdb skp
			if [ $? -ne 0 ]; then  
				echo 'La BD ya existe'
			else
				echo 'La BD skp se ha creado con exito'
			fi
			;;		
		2 )
			pg_restore -i -h localhost -p 5432 -U "$usuario_BD" -d skp -v "/home/"$usuario"/Escritorio/git/skp/Script/backup.sql"
			if [ $? -ne 0 ]; then  
				echo 'Error la BD no existe por favor creelo'
			else
				echo 'La BD fue cargada correctamente'
			fi
			;;
		3 )
			pg_dump -i -h localhost -p 5432 -U "$usuario_BD" -F c -b -v -f "/home/"$usuario"/Escritorio/git/skp/Script/backup.sql" skp
			if [ $? -ne 0 ]; then  
				echo 'Error la BD no existe por favor creelo'
			else
				echo 'Se creo un backup de la BD correctamente'
			fi
			;;
		4 )
			sudo -u "$usuario_BD" dropdb skp
			if [ $? -ne 0 ]; then  
				echo 'Error la BD no existe por favor creelo'
			else
				echo 'La BD se elimino correctamente'
			fi
			;;
		5 )
			cd /var/www
			sudo rm -r -f skp
			sudo wget https://github.com/isaacveron/skp/archive/master.zip
			sudo unzip master.zip
			sudo rm master.zip
			sudo mv skp-master skp
			cd skp/Script
			sudo cp skp.conf /etc/apache2/sites-available/skp.conf
			sudo cp wsgi.load /etc/apache2/mods-available/wsgi.load
			sudo a2ensite skp.conf
			sudo /etc/init.d/apache2 restart
			xdg-open http://skp.com
			clear		
			;;
		6 )
			sudo /etc/init.d/apache2 stop
			exit ;;
		? ) clear && alerta;;
	esac
done



