#!/usr/bin/env python3
import sys
import os
import subprocess
import json
import netifaces as ni
from time import gmtime, strftime, sleep

global dircompleta
def probrarch(arch):
	bina=os.stat(arch).st_size==0 
	if bina==True:
		#input("holaaaaaaaaaaaa")
		os.system("rm -r %s" %(arch))
	#f=open(arch,"r").read().split("\n")
	#input(str(str(f)+str(len(f))))
	#if len(f)==1 and f[0]=="":
		#input("holaaaaaaaaaaaa")
		#os.system("rm -r %s" %(arch))
def logo():
	print(color.HEADER+ '''
---------------------------------------------------------------
---------------------------------------------------------------      
--                                                           --                                                                                                         
--                    |                                      --
--                    |              o                       --
--                    |                                      --
--                 /-\|  /-\   |---  |  ---/                 --
--                /   | |   |  |   | |    /                  --
--                \   | |   |  |   | |   /                   --
--                 \_/   \_/ \ |   | |  /___                 --
--                                                           --
--      daniz-red 1.0.2                                      --
--      Coded by Brian Quinde, Lisseth Campoverde            --
--      Universidad de Cuenca                                --
--      daniz.redteam@outlook.es                             --
---------------------------------------------------------------
---------------------------------------------------------------
	'''+color.END)

def nucljson(archivo):
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

		lista =[]
		for j in range(cont-1):
			#print(str(j+1)+".json")
			with open(str(j+1)+".json") as file:
		    		data = json.load(file)
			lista.append(str(data["matched"])+"-->"+str(data["info"]["reference"]))
		for j1 in range(cont):
			subprocess.Popen(["rm","-r", str(j1+1)+".json"])
		return(lista)

def correrprog(objetivo,progra,arch,conte):
	prog=["python3"]
	fase_1=arch		
	for i in range(len(conte)):
		for j in range(len(prog)):
			try:
				os.system("%s %s -o %s -f %s" % (prog[j],progra+ conte[i],objetivo,fase_1+str(conte[i])[:-3]))  #ejecucion de programa cuando tiene -o y -f
				for j28 in [".xml",".json",".txt"]:
					try:
						probrarch(fase_1+str(conte[i])[:-3]+j28)
					except:
						pass
				print("%s %s -o %s -f %s" % (prog[j],progra + conte[i],objetivo,fase_1+str(conte[i])[:-3]))
			except:
				pass
				
#comenzaria aqui la programacion



def clearScr():
	os.system('clear')
def seleccionmul(path,tipo1,info):
	
	opt=""
	manlist=crearmenu(path,tipo1)
	menu=manlist[0]
	
	lista1=manlist[1]
	listob=[]
	#raw_input(manlist[1])
	
	while opt!="a" and opt!="b" and opt!="q":
		clearScr()
		print("Info: ")
		print(color.HEADER+str(info)+ color.END)
		print(str(tipo1)+" selected: "+ str(listob))
		print(color.OKBLUE+menu+color.END)
		opt = "b" #input("Select--> ")
		clearScr()
		if opt=="a":
			sal=[]
			for i in listob:
				if i not in sal:
					sal.append(i)
			return(sal)
		elif opt=="b":
			salida=lista1
			return(salida)
		elif opt=="q":
			clearScr()
			return("Go back")
		try:
			if lista1[int(opt)-1] in lista1:
				listob.append(lista1[int(opt)-1])
		except:
			print("The option "+ str(tipo1)+" do/does not exists")
	#print(listob)
		
		
def crearmenu(path1,tipo):
	if type(path1)==str:
		lista=os.listdir(path1)
	elif type(path1)==list:
		lista=path1
	m=""
	for i in range(len(lista)):
			m=m+"{"+str(i+1)+"}--"+lista[i]+"\n"
	m=m+"{a}--Continue with selected " +str(tipo)+"\n"
	m=m+"{b}--Automatic--(All the "+str(tipo)+")--"+"\n"
	m=m+"{q}--Go back"
	return ([m,lista])

class color:
	HEADER = '\033[95m'
	IMPORTANT = '\33[35m'
	NOTICE = '\033[33m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	RED = '\033[91m'
	END = '\033[0m'
	UNDERLINE = '\033[4m'
	LOGGING = '\33[34m'

import argparse
parser=argparse.ArgumentParser(description="Automatic daniz-red execution")
parser.add_argument("-c", "--config", help="Configuration file")
parser=parser.parse_args() 
conf1=json.load(open(str(parser.config),"r"))
#input(conf1["target"])
#conf=open(str(parser.config),"r").read().split("\n")[:-1]

#if len(conf) >= 2:
correo=conf1["e-mail"]
s=open("/src/correo.txt","w")
s.write(correo)
s.close()
interfaz=conf1["interface"]
try:
	objetivo=conf1["target"]
except:
	objetivo=""
#else:
#	print("the config file is wrong")
#	sys.exit()

try:
	objetivoo=objetivo.split(",")
	#input(str(objetivoo))

except:
	objetivoo=[objetivo]


for objetivooo in objetivoo:
	#input(str(objetivooo))
	clearScr()
	try:
		os.system("mkdir %s/archivos/"%("/src"))
		os.system("mkdir /src/archivos/hosts/")
		os.system("mkdir /src/archivos/hosts/fase_1/")
		os.system("mkdir /src/archivos/hosts/fase_2/")
		os.system("mkdir /src/archivos/hosts/fase_3/")
		os.system("mkdir /src/archivos/hosts/explotacion/")
		os.system("mkdir /src/Reportes/")
		os.system("mkdir /src/Reportes/Ataque/")
		os.system("mkdir /src/Reportes/Escaneo/")
		os.system("mkdir /src/Reporte_final")
	except:
		pass
	clearScr()
	logo()
	print (color.HEADER+"************************* DaNiz Red Team*************************"+ color.END+ '''
		''' + color.OKBLUE + '''
	   {1}--Start analysis
	   {2}--Reports
	   {99}-Quit\n
		'''+color.END)
		
	choice = "1"#input("option: ")
	backdoor=""
	if choice == "1":
		opt2=""
		while opt2!="99" and backdoor!="sal":
			os.system("rm %s/archivos/hosts/fase_1/*" %("/src"))
			os.system("rm %s/archivos/hosts/fase_2/*" %("/src"))
			os.system("rm %s/archivos/hosts/fase_3/*" %("/src"))
			os.system("rm %s/archivos/hosts/explotacion/*" %("/src"))
			clearScr() 
			print (color.HEADER+"*************************** Starting analysis ***************************"+color.END)
			print(color.WARNING+"This framework can perform the following audits:"+color.END)
			print (color.OKBLUE+'''
		   {1}--Hosts
		   {2}--Web pages
		   {3}--Network
		   {99}-Go back\n
			'''+color.END)
			opt2="1"#input("Option: ")
			if opt2=="1":
				
				obj_fase_1=objetivooo#
				inter=str(interfaz)#open("interface.txt","r").read().replace("\n","")
				if obj_fase_1=="":
					try: 
						ni.ifaddresses(str(inter))
						ip = ni.ifaddresses(str(inter))[ni.AF_INET][0]['addr']
						listado=ip.split(".")
						sin=listado[:-1]
						obj_fase_1=str(".".join(sin))+".0/24"
					except:
						print("The interface is not valid")
						break
					#print (ip)
	    			#contenido=os.listdir(str(os.getcwd())+"/modules/hosts/fase_1")
				contenido=""
				while contenido!="Go back" and backdoor!="sal":
					os.system("rm %s/archivos/hosts/fase_1/*"%("/src"))
					contenido=seleccionmul(str("/src")+"/modules/hosts/fase_1","programs","") #accede al programa que permite seleccionar entre los programas existente u objetivos a utilizar 
					#print(contenido)
					if type(contenido) == list and len(contenido)>0:
						program=str("/src")+"/modules/hosts"  # lugar donde se encuentran los programas
						filepath=str("/src")+"/archivos/hosts" #lugar a donde van a ir los archivos encontrados y de donde tiene que salir el informe de esta parte
						programa=program+"/fase_1/"
						fase_1=filepath+"/fase_1/"
						correrprog(obj_fase_1,programa,fase_1,contenido)	
						clearScr()
						input_fase_2=os.listdir(fase_1)
						print (input_fase_2)
						f2_obj=[]
						for i2 in input_fase_2:
							f2_aux = os.popen("cat %s | grep -E -o \"([0-9]{1,3}[\.]){3}[0-9]{1,3}\" " % (fase_1+i2)).read().split("\n")[:-1] #comando para conseguir ips desde un archivo cualquira
							for i3 in f2_aux:
								if i3 not in f2_obj:
									f2_obj.append(i3)
						if len(f2_obj)!=0:
							fase2obj=""
							while fase2obj!="Go back" and backdoor!="sal":
								fase2obj=seleccionmul(f2_obj,"ips","unooo") #accede al programa que permite seleccionar entre los programas existente u objetivos a utilizar
								#input(str(fase2obj))
								#print (fase2obj," estas son las ips")
								if type(fase2obj)==list and len(fase2obj)>0:
									contenidof2=""
									while contenidof2!="Go back" and backdoor!="sal":
										contenidof2=seleccionmul(str("/src")+"/modules/hosts/fase_2","programas","")
										if type(contenidof2)==list and len(contenidof2)>0: 
											
											prograf2=program+"/fase_2/"
											fase_2=filepath+"/fase_2/"
							    				#print("soy una "+ str(type(fase2obj)))
							    				#input("que eres")
						    				
											
											os.system("rm %s/archivos/hosts/fase_2/*"%("/src"))
											#input(str(fase2obj))
											for f2 in fase2obj:
							    					correrprog(f2,prograf2,fase_2+str(f2),contenidof2)
							    				
											fase_2_fils=os.listdir(fase_2)
											fase_2_salida=[]
											for fil1 in fase_2_fils:
												if ".xml" in fil1:
													lista=os.popen("/usr/bin/python3 /src/probandoxml.py -f %s" %(fase_2+fil1)).read().replace("[","").replace("'","").replace("]]","").replace("\n","").split(",")
													#print(lista)
													#input("hasta aqui si llego")
													#input(lista)
													#fin=[]
													#for f2i in lista:
													#	uni=fin.append(f2i.split(","))
													#for f2j in lista:
														#print(len(f2j))
													if len(lista)>=2: 
														fase_2_salida.append(["Ip: ",lista[0]," Mac: ",lista[1]," puertos =",lista[2:]])
														
											#print(fase_2_salida," " ,str(len(fase_2_salida)))
											
											#print(fase_2_salida,len(fase_2_salida))
											#input("hasta aqui si llego")
											obj_f3=[]
											f3_info=""
											for f2int in fase_2_salida:
												finf2=""
												#print("cuantos", len(f2int))
												for f2int2 in f2int:
													finf2=finf2+str(f2int2)
													#print(finf2)
													#print(f2int[1])
													
												if f2int[1] not in obj_f3:
													obj_f3.append(f2int[1])
													f3_info= f3_info + str(finf2) +"\n"
						
												
												#print(str(finf2))
											#print("*********Informacion acerca de los puertos de los objetivos*********")							
											#print(obj_f3)
											print(color.NOTICE+'''
	Using existing ports in the ip adresses the better objectives can be determined. 
				    							'''+color.END+"\n")
											
											prograf3=program+"/fase_3/"
											fase_3=filepath+"/fase_3/"
											######------------>######desde aqui va la fase 3...... una vez se tienen los puertos
											fase3obj=""
											while fase3obj!="Go back" and backdoor!="sal":
												fase3obj=seleccionmul(obj_f3,"ips",f3_info)
												contenidof3=""
												if type(fase3obj)==list and len(fase3obj)>0:
													while contenidof3!= "Go back" and backdoor!="sal":
														contenidof3=seleccionmul(("/src")+"/modules/hosts/fase_3","programas","")

														if type(contenidof3)==list and len(contenidof3)>0:
															os.system("rm %s/archivos/hosts/fase_3/*"  %(str("/src")))
															for f3 in fase3obj:
									    							correrprog(f3,prograf3,fase_3+str(f3),contenidof3)
															print(color.NOTICE+'''
	At this point the information about vulnerabilities in the objectives
	was obtained.
							    								'''+color.END+"\n")
															print(color.NOTICE+"The third part of the audit are finished"+color.END)
															#input("Press ENTER to continue...")
															### En esta parte se hace uso de las respuestas de nuclei para poder recomendar programas
															vulnprog=program+"/ejecutadores/" # se hace uso de fase_3
															listvulprog=os.listdir(vulnprog)
															nulist=os.listdir(fase_3)
															#probrarch(arch)
															vulnrep=filepath+"/explotacion/"
															nucleilis=[]
															for nu in nulist:
																print(nu)
																if "nuclei.json" in nu:
																	
																	#nuclist.append(nu)
																	nucleilis = nucleilis + nucljson(fase_3+nu)
															nucleilist=[]
															
															for nuc in nucleilis:
																if nuc not in nucleilist:
																	nucleilist.append(nuc)
															
															print(nucleilist)
															reco=[]
															for expr in listvulprog:
																for resvul in nucleilist:
																	print(resvul[:-3].lower())
																	if expr[:-3].lower() in resvul.lower():
																		reco.append([expr,resvul])
															
															#input(reco)
															
															clearScr()
															if len(reco)>0:
																clearScr()
																print('''
		Among the programs loaded compared to the finded vulnerabilities the
		following programs can be executed in the objective. \n
																''')
																
																for recoi in reco:
																	print(recoi[0]+"->"+recoi[1])
															
																#input("si llego aqui")
																ip=""
																for recoj in reco:
																	clearScr()
																	ip=""
																	for letra in recoj[1]:
																		if letra==":":
																			break
																		else:
																			ip=ip+letra
																	###el archivo no lleva .txt por que lo tiene en el programa de ejecucion
																	os.system("rm -r /src/archivos/hosts/ejecutadores/*")
																	os.system("/usr/bin/python3 %s -o %s -f %s" % (vulnprog+recoj[0],ip,vulnrep+str(ip)+str(recoj[0][:-3]))) 
																	#os.system("less %s"%(vulnrep+str(ip)+str(recoj[0][:-3])+".txt" ))
																	print("Ataque "+str(recoj[0])+" realizado")
															
															
																	
																	
															## fin de la parte de recomendacion o ataque
															
															###programacion para informe y envio a email
															
															
															
															
															###fin envion reporte
															
															
															#contenidof4=seleccionmul((os.getcwd())+"/modules/hosts//explotacion","programas","")
															#input("Press ENTER to continue...")
															
															#input("reporte enviado")
															backdoor="sal"
															break
														
														else:
															backdoor="sal"
															break
															
													backdoor="sal"		
													break
												else:
													backdoor="sal"
													break
												backdoor="sal"
												break
											backdoor="sal"		
											break				
										else:
											backdoor="sal"
											break
										backdoor="sal"
										break
											
									backdoor="sal"		
									break						
						
								else:
									backdoor="sal"
									break
								
								backdoor="sal"
								break							
						
							backdoor="sal"
							break
						else:
							backdoor="sal"
							break
						backdoor="sal"
						break												#input("Press ENTER to continue...")
					else:
						backdoor="sal"
						break												
					backdoor="sal"
					break
																		
																		
																	
															
											#raw_input("paraaaaa")
											
										
									
						#raw_input("hasta aqui")
						
				
				
				
				
								#print ("%s %s -o %s > %s" % (prog[j],programa + contenido[i],obj_fase_1,filepath+str(contenido[i])[:-3]+".txt"))
								#raw_input("Este codigo no funciono con %s" % (prog[j]))
				
				#raw_input("hasta aqui vamo")
			elif opt2=="2":
				opt2man=""
				while opt2man!="Go back":
					opt2man=seleccionmul((os.getcwd())+"/modules/web","Manual","Manuals to perform web page analysis and attack")
					
					if type(opt2man)==list and len(opt2man)>0:
						print("Manual will be presented one by one, exit a manual with 'q'")
						for iopt2 in opt2man:
							os.system("less %s" %((os.getcwd())+"/modules/web/"+str(iopt2)))
				#print("opcion 2")
			elif opt2=="3":
				opt3man=""
				while opt3man!="Go back":
					opt3man=seleccionmul((os.getcwd())+"/modules/red","Manual","Manuals to perform network analysis and attack")
					
					if type(opt3man)==list and len(opt3man)>0:
						print("Manual will be presented one by one, exit a manual with 'q'")
						for iopt3 in opt3man:
							os.system("less %s" %((os.getcwd())+"/modules/red/"+str(iopt3)))
			backdoor="sal"
			break
		
	elif choice == "2":
		ch2man=""
		while ch2man!="Go back":
			ch2man=seleccionmul((os.getcwd())+"/Reporte_final","Manual","Manuals to perform network analysis and attack")
			
			if type(ch2man)==list and len(ch2man)>0:
				print("Manual will be sended to your email(correo.txt) one by one")
				for chpt3 in ch2man:
					os.system("python3 enviar-pdf.py -n %s" % (chpt3) )
					#os.system("less %s" %((os.getcwd())+"/modules/red/"+str(iopt3)))
	    
	elif choice == "99":
		sys.exit()
	else:
		input("no existe la opcion")
	
	fecha=strftime("%Y-%m-%d_%H:%M:%S", gmtime())
	os.system("/usr/bin/python3 /src/pdf.py -v %s" % (str(obj_fase_1.replace("/",":"))+str(fecha)) )
															#input("reporte creado... ")
	nomreport="reporte-"+str(obj_fase_1.replace("/",":"))+str(fecha)+".pdf"
	os.system("/usr/bin/python3 /src/enviar-pdf.py -n %s" % (nomreport) )


