# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import sys
import tkinter as tk
import time 
 



class Clock:
    
    def __init__(self, telinha):
        self.telinha = telinha
        self.janela = self.telinha.janelinha
        self.clock = tk.Label(self.janela, font=("times", 50, "bold"),fg = "white", bg = "red")
    
    def tick(self):
        time_string = time.strftime("(diadasemana[%A])  (meses[%B]) %d \n %Y %H:%M")
        self.clock.config(text = time_string)
        self.clock.after(200, self.tick)
    
       
    def inicia_clock(self):
        
        self.clock.place(anchor = "nw")    
        self.tick()




#relogio = Clock()
#relogio.iniciar()