#!/usr/bin/env python3
#_'_ coding: utf8 _'_


import xmltodict
import json
import argparse #definir objetivo especifico con consola
from fpdf import FPDF
import os


#permite la seleccion desde consola
parse=argparse.ArgumentParser()
#parse.add_argument("-t","--txt",help="Nombre txt con informacion")
parse.add_argument("-i","--ingreso",help="Nombre del archivo de ingreso")
parse.add_argument("-s","--salida",help="Nombre del archivo .pdf de salida ")
parse=parse.parse_args()


with open(parse.ingreso) as xml_data:
    xml_parsed = xmltodict.parse(xml_data.read()) #devuelve diccionario

#print(xml_parsed)


od2 = json.loads(json.dumps(xml_parsed)) 

#print(str(od2))

n=od2["nmaprun"]

#print(n)

if "host" in n:
    ipv=n.get("host")

#print(ipv)

#ipm=ipv["status"]

tu=[]
ad=[]
mac=[]

try:
	for l in range(len(ipv)):
	 	o=ipv[l]
	 	if "address" in ipv[l]:
	 		ipm=o["address"]
	 		if type(ipm)==list:
	 			r=ipm[0]['@addr']
	 			t=ipm[1]['@addr']

	 			ad.append(str(r))
	 			mac.append(str(t))
	 		else:
	 			r=ipm['@addr']
	 			ad.append(str(r))
	 			mac.append("")
	 			
except:
	for l in ipv:
	 	#o=ipv[l]
	 	if l == "address":
	 		ipm=ipv["address"]
	 		if type(ipm)==list:
	 			r=ipm[0]['@addr']
	 			t=ipm[1]['@addr']

	 			ad.append(str(r))
	 			mac.append(str(t))
	 		else:
	 			r=ipm['@addr']
	 			ad.append(str(r))
	 			mac.append("")
	

tu.append(ad)
tu.append(mac)

#-------------------------------------------------------------------------------------------------------------------------

title = '1.1_Descubrimiento en NMAP'


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


document = PDF()
document.alias_nb_pages()
document.add_page()
document.line(45, 45, 180, 45)
document.set_line_width(2)
document.set_font('helvetica', size=12)

# escribir texto


#FALTA IMPRIMIR ID


document.set_font('arial', 'B', 13.0) #B/I/U 
document.set_xy(10, 40)
document.set_font('arial', 'B', 12.0) #B/I/U 

document.ln(1)
document.ln(1)
document.ln(1)
document.ln(1)
document.ln(1)
document.ln(1)
document.cell(0,10,txt="Hosts activos")
document.ln()
document.set_font('arial', 'I', 10.0)

for l in range(len(tu[0])):

    document.cell(0,10,"Dirección IP: {}     -      Direccion MAC: {}".format(str(tu[0][l]),str(tu[1][l])))
    document.ln()

document.cell(0,6,txt="-----------------------------------------------------------------------------------------------------------------------------------------------------------")

document.output(parse.salida)







