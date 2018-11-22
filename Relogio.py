# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import sys
import tkinter as tk
import time
from Traducao_relogio import diadasemana, meses



class Clock:
    
    def __init__(self, telinha):
        self.telinha = telinha
        self.janela = self.telinha.janelinha
        self.clock = tk.Label(self.janela, font=("times", 50, "bold"),fg = "white", bg = "black")
    
    def tick(self):
<<<<<<< HEAD
        time_string = time.strftime("%A %B %d \n %Y %H:%M")
        diadasemana_string = time.strftime("%A")
        print(diadasemana_string)
        self.clock.config(text = time_string)
=======
        dia_semana = time.strftime("%A")
        mes = time.strftime("%B")
        traducao_dias = "{0} \n".format(diadasemana[dia_semana])
        traducao_meses = "{0} de".format(meses[mes])
        dia_mes = time.strftime(" %d de ")
        ano = time.strftime(" %Y ")
        horario = time.strftime("%H:%M \n")
        lista_string = horario + traducao_dias + dia_mes + traducao_meses + ano 
        self.clock.config(text = lista_string)
>>>>>>> 915e91ae0dcfc967f210d5b6300ab8ee40cdbe81
        self.clock.after(200, self.tick)
    
       
    def inicia_clock(self):
        
        self.clock.place(anchor = "nw")    
        self.tick()




#relogio = Clock()
#relogio.iniciar()