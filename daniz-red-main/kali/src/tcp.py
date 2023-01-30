


import xmltodict
import json

from collections import OrderedDict 
from fpdf import FPDF
import os
import argparse #definir objetivo especifico con consola

#permite la seleccion desde consola
parse=argparse.ArgumentParser()
#parse.add_argument("-t","--txt",help="Nombre txt con informacion")
parse.add_argument("-i","--ingreso",help="Nombre del archivo .xml de ingreso ")
parse.add_argument("-s","--salida",help="Nombre del archivo .pdf de salida ")
parse.add_argument("-l","--titulo",help="Titulo en el archivo ")
parse=parse.parse_args()

#archivo='106-con.xml' #llama archivo a sacar info

#archivo='104-sin.xml'

archivo=parse.ingreso

# convertir xml a diccionario 


with open(archivo) as xml_data:
    xml_parsed = xmltodict.parse(xml_data.read()) #devuelve diccionario
 

#quitar dic aninados

od2 = json.loads(json.dumps(xml_parsed))

# filtra
n=od2["nmaprun"]

# valida una de las dos maneras

l="sin"

if "host" in n:
    ipv=n.get("host")

	# busco address:
    if "address" in ipv:
    	ip_info=ipv.get("address")


ipm=[]
ipt=[]

try:
	for l in range(len(ip_info)):
	    ipm.append(ip_info[l]["@addr"])

	for l in range(len(ip_info)):
	    ipt.append(ip_info[l]["@addrtype"])
except:
	for l in ip_info:
		if l=="@addr":
			ipm.append(ip_info["@addr"])
			ipm.append("no se pudo obtener")
	for l in ip_info:
		if l=="@addrtype":
			ipt.append(ip_info["@addrtype"])
			ipt.append("no se pudo obtener")



ipf=[]
ipf.append(ipm)
ipf.append(ipt)


#---------------ipf--------

if "host" in n:
    valor=n.get("host")


if "ports" in valor:
    puerto=valor.get("ports")


#--------------PORTS---------------------


extra_p=puerto["extraports"]# -----------VALEEEE EXTRAPORTS   2


lista_e=[]
l1=[]
l2=[]
l3=[]

if "@state" in extra_p:
    l1=extra_p["@state"]
if "@count" in extra_p:
    l2=extra_p["@count"]
if "extrareasons" in extra_p:
    l3=extra_p["extrareasons"]["@reason"]

lista_e.append([l1])
lista_e.append([l2])
lista_e.append([l3])

#print("extra")

m=""

try:

	s=puerto["port"]
	#print(s)
	m="con puertos"

except:
	print("s")
	m="sin puertos"


# ----------------------------------------------------------------------------------------------

title = parse.titulo


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

    def bol(self,lista_e,ip): # lista, #falta la ip
    	scripts=len(lista_e)
    	document.ln(1)
    	document.ln(1)
    	document.ln(1)
    	document.ln(1)
    	document.ln(1)
    	document.ln(1)
    	document.ln(1)
    	document.ln(1)
    	document.ln(1)
    	document.set_font('arial', 'B', 10.0) #B/I/U 
    	document.cell(0,10,"Direcciones:")
    	document.ln()
    	document.set_font('arial', 'I', 10.0)
    	document.cell(0,10,"IP: {}  -  {}".format(str(ip[0][0]),str(ip[1][0])))
    	document.ln(5)
    	document.cell(0,10,"Fisica: {}  -  {}".format(str(ip[1][1]),str(ip[0][1])))
    	document.set_font('arial', 'B', 10.0) #B/I/U 
    	document.ln()
    	document.cell(0,10,"Puertos:")
    	document.set_font('arial', 'I', 10.0)
    	document.ln()
    	document.cell(0,10,"Los {} puertos escaneados pero no presentados, estan en estado: {}".format(str(lista_e[1][0]),str(lista_e[0][0])))
    	document.ln(5)
    	document.cell(0,10,"Los {} puertos respondieron con: {}".format(str(lista_e[1][0]),str(lista_e[2][0])))
    	document.ln()
    	document.cell(0,10,"---------------------------------------------------------------------------------------------------------------------------------------------------------------") 
    	document.ln(2)
    	document.cell(0,10,"---------------------------------------------------------------------------------------------------------------------------------------------------------------") 

    def bol2(self,mn): # lista, #falta la ip
    	
    	document.ln(1)
    	document.ln(1)
    	document.ln(1)
    	document.ln(1)
    	document.ln(1)
    	document.ln(1)
    	
    	document.set_font('arial', 'I', 10.0)
    	document.chapter_body(mn)
    	document.ln(1)

    	document.cell(0,10,"---------------------------------------------------------------------------------------------------------------------------------------------------------------") 
    	document.ln(2)
    	document.cell(0,10,"---------------------------------------------------------------------------------------------------------------------------------------------------------------") 



document = PDF()
document.alias_nb_pages()
document.add_page()
document.line(45, 45, 180, 45)
document.set_line_width(2)
document.set_font('helvetica', size=12)
document.set_font('arial', 'B', 13.0) #B/I/U 
document.set_xy(10, 40)

document.bol(lista_e,ipf)

if m=="con puertos":

	mn=archivo.replace("xml","txt")
	comand="/usr/bin/python3 /src/nmap2md.py "+archivo+" -o "+str(mn)+" -c "+"'Port,State,Service' --hs 3 --rc '[port.number]/[port.protocol],[state],[service.name]'"
	os.system(comand)
	document.bol2(mn)

else:
	y=0

document.output(parse.salida)



#-------------------------------------------
