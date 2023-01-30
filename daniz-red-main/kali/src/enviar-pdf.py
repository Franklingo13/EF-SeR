

import os
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 

import argparse #detectar instrucciones o argumentos q pase un usuario desde la consola sin la necesidad de crear
#un menu

parser=argparse.ArgumentParser(description="envio de reporte") #descripcion del objeto
parser.add_argument("-n", "--nombre", help="Nombre reporte") #anade argumento
parser=parser.parse_args() #los argumentos est{en disponibles para el usuario


fromaddr = "pruebas1hack@gmail.com"

with open("/src/correo.txt") as f:
    for linea in f:
    	#print(linea)
    	dire=str(linea)

toaddr = dire
   
msg = MIMEMultipart() 
  
msg['From'] = fromaddr 
  
msg['To'] = toaddr 
  
msg['Subject'] = "Reporte Daniz Red Team"
  
body = "Se adjunta el reporte del pentesting"
  
msg.attach(MIMEText(body, 'plain')) 


filename = parser.nombre

carpetast="/src"
	#print(carpetas)
dire=str(carpetast)+"/Reporte_final/"+str(parser.nombre)

print("Nombre de archivo a enviar: " + dire)

attachment = open(dire, "rb") 
  
p = MIMEBase('application', 'octet-stream') 
  
p.set_payload((attachment).read()) 
  
encoders.encode_base64(p) 
   
p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
  
msg.attach(p) 
  
s = smtplib.SMTP('smtp.gmail.com', 587) 
  
s.starttls() 

try:
	s.login(fromaddr, "hack-123") 
except smtplib.SMTPAuthenticationError as serr:
	print("Las credenciales de autentidación son incorrectas")
	exit(0)
  
text = msg.as_string() 
  
s.sendmail(fromaddr, toaddr, text) 
  
s.quit() 
