#!/usr/bin/env python3
#_*_ coding: utf8 _*_

import argparse #definir objetivo especifico con consola
import os

#puede escanear una ip o un rango

#permite la seleccion desde consola
parse=argparse.ArgumentParser()
parse.add_argument("-o","--objetivo",help="direccion a utilizar")
parse.add_argument("-f","--filepath",help="Lugar donde se va a guardar el archivo")
parse=parse.parse_args()

def nmaptcp(ip,log): #detectar dispositivos conectados a la red 
	#variable q contiene la capa arp
	#configura el paquete arp para escanear las direcciones
	#if log[-4:]==".txt":
	#	log=log[-4:]
	try: 
		iplist=ip.split(".")
		for ip1 in iplist:
			ip2=int(ip1)
		pass
	except:
		os.system('''
		cd /theHarvester; \
		python3 theHarvester.py -d %s -l 300 -b google,urlscan,linkedin,trello -s -f %s.json;
		''' % (ip,log))
def main():
	if parse.objetivo and parse.filepath: #verificar si se incluyo alguna opcion
		nmaptcp(parse.objetivo,parse.filepath) #pasamos la opcion q pase el usuario en la linea de comando
	else:
		print("")


if __name__ == '__main__':
	main()
