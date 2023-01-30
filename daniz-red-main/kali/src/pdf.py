

#entrada: 

import os
import string
from time import gmtime, strftime, sleep
#from PyPDF2 import PdfFileMerger
from PyPDF2 import PdfMerger

home="/src"+"/archivos"

carpetas=os.listdir(home)

#recorre la lista de carpetas y selecciona las q no inician con .
carpetas=[x for x in carpetas if not x.startswith(".")]

extensiones= [".xml",".txt",".json"] 


import argparse #detectar instrucciones o argumentos q pase un usuario desde la consola sin la necesidad de crear
#un menu

parser=argparse.ArgumentParser(description="Variable for report") #descripcion del objeto
parser.add_argument("-v", "--variable", help="Name for pdf") #anade argumento

parser=parser.parse_args() #los argumentos est{en disponibles para el usuario
print(parser.variable)

def list_a():

	file_list=open("/src/file_list","w+")#almacena archivos descubiertos
	for carpeta in carpetas:
		ruta=home+"/"+carpeta #crea una ruta completa de las carpetas
		for extension in extensiones:
			#explora los archivos
			#rutabs: ruta absoluta, directorio: cada carpeta, archivo: cada archivo q encuentra
			for rutabs, directorio, archivo in os.walk(ruta):
				for file in archivo:
					if file.endswith(extension): #con q caracteres termina un archivo
						file_list.write(os.path.join(rutabs, file)+"\n") #guardar archivo
	file_list.close() #manda cada archivo a cifrar
	
	#eliminar el elemnto nulo de la lista
	lista=open("/src/file_list","r")
	lista=lista.read().split("\n")
	lista=[l for l in lista if not l== ""] #rellena lista solo con valores diferentes de ""
	
	return(lista)

lista=list_a()



l_x=[]
l_j=[]
l_t=[]

for element in lista:
	#print(element)
	if element[-4:] == ".xml":
		l_x.append(element)


	elif element[-5:] == ".json":
		l_j.append(element)


	elif element[-4:] == ".txt":
		l_t.append(element)


#--------------xml------------------------

#cambiar lx_1 a l_x
#lx_1=["/home/kali/Documents/Tesis/daniz-red/src/archivos/hosts/fase_2/192.168.0.110nmappn.xml","/home/kali/Documents/Tesis/archivos/hosts/fase_2/192.168.56.168vunlnmaptcp.xml","/home/kali/Documents/Tesis/archivos/hosts/fase_2/192.168.56.168vunlnmapudp.xml","/home/kali/Documents/Tesis/daniz-red/src/archivos/hosts/fase_2/upnmap.xml"]

lx_1=l_x

n_t=[]
n_u=[]
n_pn=[]
n_ap=[]
n_f=[]
n_i=[]    



for t in lx_1:
	#print(element) #ESTE FALTA BUSCAR
	if t[-11:] == "nmaptcp.xml" and t[-12:] != "lnmaptcp.xml":   #NO HAY   #tcp
		n_t.append(t)
		#print("entra")


	elif t[-11:] == "nmapudp.xml":    #udp NO HAY IGUAL ARRIBA
		n_u.append(t)


	elif t[-10:] == "nmappn.xml":     
		n_pn.append(t)

	elif t[-9:] == "pnmap.xml":     #upnmap
		n_ap.append(t)

	elif t[-8:] == "serv.xml":     
		n_f.append(t)

	elif t[-12:] == "lnmaptcp.xml":  #ESTE FALTA BUSCAR HICE PRIMERO
		n_i.append(t)


def n_ip(n_t): #saca el nombre del path
	name=[]
	name1=""
	count=0
	for s in range(0,len(n_t)):

		for m in range(len(n_t[s])-1,-1,-1):

			name1=name1+str(n_t[s][m])
		name.append(name1)
		name1=""
	#return(name)

	n_tcp=name


	nombres=[]
	for t in range(0,len(n_tcp)):

		indice = n_tcp[t].find("/")
		val=n_tcp[t]
		nam=val[:indice]
		#print(nam)
		nombres.append(nam)

	nm1=""
	nm=[]

	for s in range(0,len(nombres)):

		for m in range(len(nombres[s])-1,-1,-1):
			#print(m)
			#print(n_t[s][m])
			nm1=nm1+str(nombres[s][m])
		#name1=name1[1:] #quitar /
		nm.append(nm1)
		nm1=""

	return(nm)

nombren_t=n_ip(n_t)
nombren_u=n_ip(n_u)
nombren_pn=n_ip(n_pn)
nombren_ap=n_ip(n_ap)
nombren_f=n_ip(n_f)
nombren_i=n_ip(n_i)


"""
  ----------  NOMBRE TCP --------------
  Obtencion de puertos TCP abiertos
  python3 tcp.py -i 104-sin.xml -s 104-sin.pdf -l Obtencion-de-puertos-TCP-abiertos
"""
tcp="1.2_Obtención-de-puertos-TCP-abiertos"

for s in range(0,len(nombren_t)):
	nt=n_t[s]

	md=nombren_t[s].replace("xml","pdf")
	print("---- tcp 1 -i "+str(n_t[s])+" -s "+str(md)+" -l " + tcp)
	comandt="/usr/bin/python3 /src/tcp.py -i "+str(n_t[s])+" -s "+str(md)+" -l "+tcp
	os.system(comandt)


	ml=nombren_t[s].replace("xml","pdf")

	carpetast="/src"
	#print(carpetas)
	dire=str(carpetast)+"/Reportes"#+str(options.output)
	#print(dir)

	comand5="mv "+str(ml)+" "+str(dire)
	#print(comand5)

	os.system(comand5)

	mr=n_t[s].replace("xml","txt")

	com="rm "+str(mr)
	#print(com)
	os.system(com)


"""
  ----------  NOMBRE UDP ----------
  Obtencion de puertos UDP abiertos
"""
udp="1.2_Obtención-de-puertos-UDP-abiertos"

for s in range(0,len(nombren_u)):
	nt=n_u[s]

	md=nombren_u[s].replace("xml","pdf")

	print("---- tcp 2 -i "+str(n_t[s])+" -s "+str(md)+" -l " + tcp)
	comandt="/usr/bin/python3 /src/tcp.py -i "+str(n_u[s])+" -s "+str(md)+" -l "+udp
	os.system(comandt)

	ml=nombren_u[s].replace("xml","pdf")

	carpetast="/src"
	#print(carpetas)
	dire=str(carpetast)+"/Reportes"#+str(options.output)
	#print(dir)

	comand5="mv "+str(ml)+" "+str(dire)
	#print(comand5)

	os.system(comand5)
	mr=n_u[s].replace("xml","txt")

	com="rm "+str(mr)
	#print(com)
	os.system(com)


"""
  ------------  LNMAPTCP.XML   # 192.168.56.102vunlnmaptcp.xml
  --------         N_PN
"""

for s in range(0,len(nombren_pn)):

	#poner con path la entrada y salida
	nt=n_pn[s]

	md=nombren_pn[s].replace("xml","md")
	

	comand="/usr/bin/python3 /src/nmap2md.py "+str(n_pn[s])+" -o "+str(md)+" -c "+"'Port,State,Service' --hs 3 --rc '[port.number]/[port.protocol],[state],[service.name]'"
	

	os.system(comand)

	mn=nombren_pn[s].replace("xml","pdf")

	command1="/usr/bin/python3 "+"/src/doc-1.py "+"-t "+str(md)+" -s "+str(mn)+" -l 1.2_Escaneo-de-puertos-sin-utilizar-ICMP"

	os.system(command1)


	ml=nombren_pn[s].replace("xml","pdf")

	carpetast="/src"
	dire=str(carpetast)+"/Reportes"

	comand5="mv "+str(ml)+" "+str(dire)

	os.system(comand5)

	comandr="rm "+str(md)
	os.system(comandr)


"""
  -----------PNMAP.XML---------
  otros archivos: host activos 
  diferente: filtra otra manera 
  print("PNMAP.XML")
"""

for s in range(0,len(nombren_ap)):

	#poner con path la entrada y salida
	nt=n_ap[s]

	md=nombren_ap[s] #nombre en xml

	ml=nombren_ap[s].replace("xml","pdf")

	comand="/usr/bin/python3 /src/pxml.py"+" -i "+str(n_ap[s])+" -s "+str(ml) #no
	#print(comand)

	os.system(comand) 

			#                   3 mover pdf

	carpetast="/src"
	#print(carpetas)
	dire=str(carpetast)+"/Reportes/Escaneo"#+str(options.output)
	#print(dir)

	comand5="mv "+str(ml)+" "+str(dire)
	#print(comand5)

	os.system(comand5)  

"""
  --------         SERV.XML
  Escaneo de vulnerabilidades utilizando servicios obtenidos con NMAP
  print("serv")
"""

for s in range(0,len(nombren_f)):

	#poner con path la entrada y salida
	nt=n_f[s]

	md=nombren_f[s].replace("xml","md")
	mi=n_f[s].replace("xml","nmap")

	comand="/usr/bin/python3 /src/nmap2md.py "+str(n_f[s])+" -o "+str(md)+" -c "+"'Port,Service,Script,Salida' --hs 4 --rc '[port.number]/[port.protocol]/[state],[service.name], [script.id], [script.output]'"
	#print(comand)
	os.system(comand)

	mn=nombren_f[s].replace("xml","pdf")

	command1="/usr/bin/python3 "+"/src/doc-1.py "+"-t "+str(mi)+" -s "+str(mn)+" -l 1.3_Escaneo-de-vulnerabilidades-utilizando-servicios-obtenidos-con-NMAP"

	os.system(command1)


	ml=nombren_f[s].replace("xml","pdf")

	carpetast="/src"
	dire=str(carpetast)+"/Reportes"

	comand5="mv "+str(ml)+" "+str(dire)

	os.system(comand5)


	# eliminar otro
	comandr="rm "+str(md)
	os.system(comandr)

"""
  -------------  LNMAPTCP.XML   # 192.168.56.102vunlnmaptcp.xml
  2 pasar a md 
"""

for s in range(0,len(nombren_i)):

	#poner con path la entrada y salida
	nt=n_i[s]

	md=nombren_i[s].replace("xml","md")
	

	comand="/usr/bin/python3 /src/nmap2md.py "+str(n_i[s])+" -o "+str(md)+" -c "+"'Port,Service,Script,Salida' --hs 4 --rc '[port.number]/[port.protocol]/[state],[service.name], [script.id], [script.output]'"
	#print(comand)
	os.system(comand)


	mn=nombren_i[s].replace("xml","pdf")
	mi=n_i[s].replace("xml","nmap")

	command1="/usr/bin/python3 "+"/src/doc-1.py "+"-t "+str(mi)+" -s "+str(mn)+" -l 1.3_Vulnerabilidades-mediante-puertos-TCP"



	os.system(command1)

	ml=nombren_i[s].replace("xml","pdf")

	carpetast="/src"
	dire=str(carpetast)+"/Reportes"

	comand5="mv "+str(ml)+" "+str(dire)

	os.system(comand5)


	#eliminar otro
	comandr="rm "+str(md)
	os.system(comandr)


#--------------------json------------------------

n_n=[]
n_h=[] 


for t in l_j:
	#print(element) #ESTE FALTA BUSCAR
	if t[-11:] == "nuclei.json":   #NO HAY   #tcp
		n_n.append(t)
		#print("entra")


	elif t[-10:] == "harve.json":    #udp NO HAY IGUAL ARRIBA
		n_h.append(t)


nombren_n=n_ip(n_n)
nombren_h=n_ip(n_h)


#print("valores")

#print(nombren_n)
#print(nombren_h)

#print("valores")



# ------------------- NUCLEI 


# python3 arc-j.py -i 192.168.0.110nuclei.json -s 192.168.0.110nuclei.pdf -l Escaneo-de-vulnerabilidades-con-nuclei



nu="1.3_Escaneo-de-vulnerabilidades-con-nuclei"

for s in range(0,len(nombren_n)):
	nt=n_n[s]

	md=nombren_n[s].replace("json","pdf")

	comandt="/usr/bin/python3 /src/arc-j.py -i "+str(n_n[s])+" -s "+str(md)+" -l "+nu
	#print(comandt)
	os.system(comandt)

		#                   3 mover pdf


	carpetast="/src"
	#print(carpetas)
	dire=str(carpetast)+"/Reportes"#+str(options.output)
	#print(dir)

	mr=n_n[s].replace("json","pdf")

	comand5="mv "+str(md)+" "+str(dire)
	#print(comand5)

	os.system(comand5)

	com="rm /src/ad.txt"
	#print(com)
	os.system(com)


# -------------------- HARVESTER

#python3 harve.py -i theharve.json -s theharve.pdf -l Informacion-obtenida-mediante-un-escaneo-pasivo

no="1.1_Información-obtenida-utilizando-the-harvester"

# archivo: theharve.json

for s in range(0,len(nombren_h)):
	nt=n_h[s]

	md=nombren_h[s].replace("json","pdf")

	comandt="/usr/bin/python3 /src/harve.py -i "+str(n_h[s])+" -s "+str(md)+" -l "+no
	#print(comandt)
	os.system(comandt)

		#                   3 mover pdf


	carpetast="/src"
	#print(carpetas)
	dire=str(carpetast)+"/Reportes/Escaneo"#+str(options.output)
	#print(dir)

	mr=n_h[s].replace("json","pdf")

	comand5="mv "+str(md)+" "+str(dire)
	#print(comand5)

	os.system(comand5)

	com="rm /src/th.txt"
	#print(com)
	os.system(com)

#------------------------txt------------------------


n_s=[]
n_a=[] 


#print(l_t)

for t in l_t:
	#print(t)
	#print(element) #ESTE FALTA BUSCAR
	if t[-9:] == "e_red.txt":   #NO HAY   #tcp
		n_s.append(t)
		#print("entra")


	elif t.find("cve") >= 0:
		n_a.append(t)

	elif t.find("CVE") >= 0:
		n_a.append(t)


nombren_s=n_ip(n_s)
nombren_a=n_ip(n_a)




def llamar_txt(ar_py,t_txt,t_pdf,leo,sub_leo):

	com="/usr/bin/python3 "+ar_py+" -i "+t_txt+" -s "+t_pdf+" -l "+leo+" -t "+sub_leo
	#print(com)
	os.system(com)



try:

	ar_py="/src/texto.py"
	t_txt=str(n_s[0])
	t_pdf=nombren_s[0].replace("txt","pdf")
	leo="1.1_Escaneo-de-red-con-python"
	sub_leo="Hosts-activos"

	llamar_txt(ar_py,t_txt,t_pdf,leo,sub_leo)
	carpetast="/src"
	#print(carpetas)
	dire=str(carpetast)+"/Reportes/Escaneo"#+str(options.output)
	#print(dir)

	comand5="mv "+str(t_pdf)+" "+str(dire)
	#print(comand5)

	os.system(comand5)

except:
	pass



# -------------------ATAQUES


# ataques realizados

#CVE ID:

leo="2.1_Ataques-realizados"
ar_py="/src/texto.py"

for s in range(0,len(nombren_a)):

	t_txt=str(n_a[s])
	t_pdf=nombren_a[s].replace("txt","pdf")
	sub_leo=nombren_a[s].replace(".txt","")
	c=int(sub_leo.find("c"))
	valor="CVE_ID:"+sub_leo[-c-1:]
	llamar_txt(ar_py,t_txt,t_pdf,leo,valor)
	carpetast="/src"
	#print(carpetas)
	dire=str(carpetast)+"/Reportes/Ataque"#+str(options.output)
	#print(dir)

	comand5="mv "+str(t_pdf)+" "+str(dire)
	#print(comand5)

	os.system(comand5)

#-----------------------JUNTAR ARCHIVOS


# -----------------

#pdfs = ['file1.pdf', 'file2.pdf', 'file3.pdf', 'file4.pdf']

home="/src"+"/Reportes/"

carpetas=os.listdir(home)

pd=[] 
#print(home)
#print(carpetas)


for m in range(0,len(carpetas)):
	if carpetas[m].endswith(".pdf"):
		pd.append(home+carpetas[m])

#print(pd)


n_1=[]
n_2=[]
n_3=[]
n_4=[]
n_5=[]
n_6=[]




for t in pd:
	#print(element) #ESTE FALTA BUSCAR
	if t[-11:] == "nmaptcp.pdf" and t[-12:] != "lnmaptcp.pdf":   #NO HAY   #tcp
		n_1.append(t)
		#print("entra")


	elif t[-11:] == "nmapudp.pdf":    #udp NO HAY IGUAL ARRIBA
		n_2.append(t)


	elif t[-10:] == "nmappn.pdf":     
		n_3.append(t)

	elif t[-10:] == "nuclei.pdf":     #upnmap
		n_4.append(t)

	elif t[-8:] == "serv.pdf":     
		n_5.append(t)

	elif t[-12:] == "lnmaptcp.pdf":  #ESTE FALTA BUSCAR HICE PRIMERO
		n_6.append(t)
		
	#elif t[-9:] == "pnmap.pdf":     #upnmap
	#	n_7.append(t) 

#print(n_1)
#print(n_2)
#print(n_3)
#print(n_4)
#print(n_5)
#print(n_6)
#input("paraaaaaaaaa")

#merger = PdfFileMerger()
merger = PdfMerger()

for pdf in n_3:
   merger.append(pdf)

for pdf in n_1:
   merger.append(pdf)

for pdf in n_2:
   merger.append(pdf)

merger.write("/src/2.pdf")

comand2="mv /src/2.pdf "+str(home)
	#print(comand5)

os.system(comand2)

#------------------

#merger = PdfFileMerger()
merger = PdfMerger()

for pdf in n_4:
   merger.append(pdf)

for pdf in n_6:
   merger.append(pdf)

for pdf in n_5:
   merger.append(pdf)
   
#for pdf in n_7:
   #merger

merger.write("/src/3.pdf")

comand3="mv /src/3.pdf "+str(home)
	#print(comand5)

os.system(comand3)


#-----------------BORRAR EXTRA

for w in range(0,len(n_1)):
	con="rm "+str(n_1[w])
	os.system(con)

for w in range(0,len(n_2)):
	con="rm "+str(n_2[w])
	os.system(con)

for w in range(0,len(n_3)):
	con="rm "+str(n_3[w])
	os.system(con)

for w in range(0,len(n_4)):
	con="rm "+str(n_4[w])
	os.system(con)

for w in range(0,len(n_5)):
	con="rm "+str(n_5[w])
	os.system(con)

for w in range(0,len(n_6)):
	con="rm "+str(n_6[w])
	os.system(con)

#---------------------------------Escaneo


home="/src"+"/Reportes/Escaneo/"

carpetas=os.listdir(home)

pd=[] 
#print(home)
#print(carpetas)


for m in range(0,len(carpetas)):
	if carpetas[m].endswith(".pdf"):
		pd.append(home+carpetas[m])

#print(pd)


#pd1=[] 
#pd1.append(pd[0])
#pd1.append(pd[2])
#pd1.append(pd[1])

#merger = PdfFileMerger()
merger = PdfMerger()

for pdf in pd:
   merger.append(pdf)


merger.write("/src/1.pdf")

home1="/src"+"/Reportes/"

comand3="mv /src/1.pdf "+str(home1)
	#print(comand5)

os.system(comand3)


for w in range(0,len(pd)):
	con="rm "+str(pd[w])
	os.system(con)

#---------------------------------Ataques


home="/src"+"/Reportes/Ataque/"

carpetas=os.listdir(home)

pd=[] 
#print(home)
#print(carpetas)


for m in range(0,len(carpetas)):
	if carpetas[m].endswith(".pdf"):
		pd.append(home+carpetas[m])

#print(pd)



merger = PdfMerger()

for pdf in pd:
   merger.append(pdf)


merger.write("/src/4.pdf")

home1="/src"+"/Reportes/"

comand3="mv /src/4.pdf "+str(home1)
	#print(comand5)

os.system(comand3)


for w in range(0,len(pd)):
	con="rm "+str(pd[w])
	os.system(con)


#-----------------------UNION FINAL

home="/src"+"/Reportes/"

carpetas=sorted(os.listdir(home))

pd=[] 
#print(home)
#print(carpetas)

#input(str(carpetas))
for m in range(0,len(carpetas)):
	if carpetas[m].endswith(".pdf"):
		pd.append(home+carpetas[m])

#print(pd)

#input(str(pd))
pd1=pd


merger = PdfMerger()

for pdf in pd1:
   merger.append(pdf)


name="/src/"+"reporte-"+parser.variable+".pdf"
merger.write(name)

for w in range(0,len(pd)):
	con="rm "+str(pd[w])
	os.system(con)

home1="/src"+"/Reporte_final/"


#comand3="mv "+str(home1)+"reporte-"+parser.variable+".pdf"

command3="mv /src/reporte-"+parser.variable+".pdf "+str(home1)
#print(command3)

os.system(command3)
