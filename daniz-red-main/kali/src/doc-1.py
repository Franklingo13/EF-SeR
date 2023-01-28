#!/usr/bin/env python
#_'_ coding: utf8 _'_


from fpdf import FPDF
import os
import argparse #definir objetivo especifico con consola



#permite la seleccion desde consola
parse=argparse.ArgumentParser()
parse.add_argument("-t","--txt",help="Nombre txt con informacion")
parse.add_argument("-s","--salida",help="Nombre del archivo .pdf de salida ")
parse.add_argument("-l","--titulo",help="Titulo en el archivo ")
parse=parse.parse_args()


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

document.set_font('arial', 'I', 10.0)
document.ln(1)
document.ln(1)
document.ln(1)
document.ln(1)
document.ln(1)
document.ln(1)
document.ln(1)
document.ln(1)
#document.ln()
#document.ln()
document.set_font('arial', 'B', 13.0) #B/I/U 
document.cell(0,10,"Dirección IP:")
document.ln(1)
document.ln(1)
document.ln(1)
document.ln(1)
document.ln(1)
document.ln(1)
document.ln(1)
document.ln(1)
document.chapter_body(parse.txt)
document.ln()
document.cell(0,6,txt="-----------------------------------------------------------------------------------------------------------------------------------------------------------")



document.output(parse.salida)
