#!/usr/bin/env python
#_'_ coding: utf8 _'_


import os
import string

import xmltodict
import json

from collections import OrderedDict 
from fpdf import FPDF
import argparse
import subprocess

parse=argparse.ArgumentParser()
#parse.add_argument("-t","--txt",help="Nombre txt con informacion")
parse.add_argument("-i","--ingreso",help="Nombre del archivo .json de ingreso ")
parse.add_argument("-s","--salida",help="Nombre del archivo .pdf de salida ")
parse.add_argument("-l","--titulo",help="Titulo en el archivo ")
parse=parse.parse_args()


archivo=parse.ingreso

#SACAR info
			# templateID, 
			#info: severity reference name description **solo si hay
										#name, --    , 
			#matched

def nucljson(archivo):
	datos=[]
	lista =[]
	abierto=open(archivo,"r").read().split("\n")
	cont=0
	#print(len(abierto))
	if len(abierto)>0:
		for i in abierto:
			cont=cont+1
			#print(i,"hola")
			
			f=open(str(cont)+".json","w")
			f.write(i)
			f.close
			#subprocess.Popen(["firefox",str(cont)+".json"])

		
		for j in range(cont-1):
			#print(str(j+1)+".json")
			datos=[]
			with open(str(j+1)+".json") as file:
		    		data = json.load(file)
   
			#lista.append(str(data["matched"])+"-->"+str(data["info"]["reference"]))
			datos.append(str(data["template-id"]))

			datos.append(str(data["info"]["severity"]))

			datos.append(str(data["info"]["reference"]))

			datos.append(str(data["info"]["name"]))

			try:
				datos.append(str(data["info"]["description"]))
			except:
				datos.append("")

			datos.append(str(data["matched-at"]))

			lista.append(datos)

# --------BORRAR ARCHIVOS			
		for j1 in range(cont):
			subprocess.Popen(["rm","-r", str(j1+1)+".json"])
		return(lista)

datos=nucljson(archivo)
#print(datos)


title = parse.titulo
#title = "Escaneo-de-vulnerabilidades-con-nuclei"


class PDF(FPDF):
    def header(self):
        # Logo
        self.image('/src/universidad.png', 20, 8, 80) #50 cambia tamano
        # Arial bold 15
        self.set_font('Arial', 'B', 15)
        # Move to the right
        self.cell(80)

        # Grosor del marco (1 mm)
        self.set_line_width(5)

        # Title
        #self.cell(30, 10, 'INFORME NMAP', 1, 0, 'C')
        w = self.get_string_width(title) + 6
        self.set_x((210 - w) / 2)
        #self.set_draw_color(0, 0, 0)
        self.cell(w, 60, txt = title, ln = 1, align = 'C')
        # Line break
        #self.ln(2000)


    def chapter_body(self, name):
        # Leer archivo de texto
        with open(name, 'rb') as fh:
            txt = fh.read().decode('latin-1')
        # Times 12
        #self.set_font('Times', '', 12)
        self.set_font('arial', 'I', 10.0)
        # Emitir texto justificado
        self.multi_cell(0, 5, txt)
        # Salto de línea
        self.ln()
        # Mención en italic -cursiva-
        self.set_font('', 'I')
        self.cell(0, 5, '(end of excerpt)')

    def bol(self,datos): # lista, #falta la ip
    	#scripts=len(lista_e)
    	document.ln(1)
    	document.ln(1)
    	document.ln(1)
    	document.ln(1)
    	document.ln(1)
    	document.ln(1)
    	document.ln(1)
    	document.ln(1)
    	document.ln(1)

    	for i in range (len(datos)):
    		document.set_font('arial', 'I', 10.0)
    		document.cell(0,10,"TemplateID: {}  -  Severidad: {}".format(str(datos[i][0]),str(datos[i][1])))
    		document.ln(5)
    		document.cell(0,10,"Referencia: {}".format(str(datos[i][2])))
    		document.ln(5)
    		document.cell(0,10,"Nombre: {}".format(str(datos[i][3])))
    		document.ln(5)
    		if len(datos[i][4]) > 100:
    			document.cell(0,10,"Descripción: ")
    			document.ln(3)
    			dir_name=datos[i][4]
    			new_dir_name = dir_name.replace('\n      ', ' ')
    			file = open("/src/ad.txt", "w")
    			file.write(new_dir_name)
    			file.close()
    			document.set_font('arial', 'I', 10.0)
    			document.ln(5)
    			document.chapter_body('/src/ad.txt')
    		else:
    			document.cell(0,10,"Descripción: {}".format(str(datos[i][4])))
    			document.ln(2)
    		document.ln(3)
    		document.cell(0,10,"Objetivo emparejado con cve: {}".format(str(datos[i][5])))
    		document.ln(5)
    	
    		#document.ln()
    		document.cell(0,10,"---------------------------------------------------------------------------------------------------------------------------------------------------------------") 
    		document.ln(2)
    		document.cell(0,10,"---------------------------------------------------------------------------------------------------------------------------------------------------------------") 
    		document.ln(2)
    		document.ln(2)


document = PDF()
document.alias_nb_pages()
document.add_page()
document.line(45, 45, 180, 45)
document.set_line_width(2)
document.set_font('helvetica', size=12)
document.set_font('arial', 'B', 13.0) #B/I/U 
document.set_xy(10, 40)

document.bol(datos)

document.output(parse.salida)
