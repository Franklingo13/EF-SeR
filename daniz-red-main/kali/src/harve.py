#!/usr/bin/env python
#_'_ coding: utf8 _'_


import os
#import string

#import xmltodict
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


def nucljson(archivo):
	datos=[]
	lista =[]
	#abierto=open(archivo,"r").read().split("\n")


	with open(archivo) as file:
		   data = json.load(file)

	datos.append(data["asns"])

	datos.append(data["hosts"])

	datos.append(data["interesting_urls"])

	datos.append(data["ips"])
	return(datos)

datos=nucljson(archivo)

#print(valores[0][0])

#print(datos)


title = parse.titulo
#title = "Informacion-obtenida-mediante-un-escaneo-pasivo"

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

    # Page footer


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

    	#for i in range (len(datos)):

    	document.set_font('arial', 'B', 10.0)
    	document.cell(0,10,"ASNS: ")
    	document.ln(1)
    	document.ln(1)
    	for j in range (len(datos[0])):
    		document.ln(1)
    		document.ln(1)
    		document.ln(1)
    		document.ln(1)

    		document.set_font('arial', 'I', 10.0)
    		document.cell(0,10,str(datos[0][j]))
    		document.ln(1)
    		document.ln(1)
    	document.set_font('arial', 'B', 10.0)
    	document.ln(1)
    	document.ln(1)
    	document.ln(1)
    	document.cell(0,10,"Hosts: ")
    	document.ln(1)
    	document.ln(1)
    	document.ln(1)
    	for k in range (len(datos[1])):
    		document.ln(1)
    		document.ln(1)
    		document.ln(1)
    		document.set_font('arial', 'I', 10.0)
    		document.cell(0,10,str(datos[1][k]))
    		document.ln(1)
    		document.ln(1)
    		document.ln(1)

    	document.ln(5)
    	document.set_font('arial', 'B', 10.0)
    	document.cell(0,10,"Urls a considerar: ")
    	document.ln(1)
    	document.ln(1)
    	document.ln(1)
    	document.ln(1)
    	document.ln(1)
    	for m in range (len(datos[2])):

    		if len(datos[2][m]) > 90:
    			dir_name=datos[2][m]
    			new_dir_name = dir_name.replace('\n      ', ' ')
    			file = open("/src/th.txt", "w")
    			file.write(new_dir_name)
    			file.close()
    			document.set_font('arial', 'I', 10.0)
    			document.ln(1)
    			document.ln(1)
    			document.chapter_body('/src/th.txt')
    			document.ln(1)
    				#document.ln(1)
    				#document.ln(1)
    		else:
    			document.set_font('arial', 'I', 10.0)
    			document.cell(0,10,str(datos[2][m]))
    			document.ln(1)
    			document.ln(1)
    			document.ln(1)
    			document.ln(1)
    			document.ln(1)
    	document.set_font('arial', 'B', 10.0)
    	document.ln(1)
    	document.cell(0,10,"IPs: ")
    	document.ln(1)
    	document.ln(1)
    	document.ln(1)
    	document.ln(1)
    	document.ln(1)

    	for l in range (len(datos[3])):
    		document.ln(2)
    		document.set_font('arial', 'I', 10.0)
    		document.cell(0,10,str(datos[3][l]))
    		document.ln(3)
    	
    		#document.ln()
    	document.ln(1)
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
