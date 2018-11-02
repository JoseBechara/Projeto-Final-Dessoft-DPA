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
        self.clock = tk.Label(self.janela, font=("times", 50, "bold"),fg = "white", bg = "black")
    
    def tick(self):
        time_string = time.strftime("%A %d %B  \n %Y %H:%M")
        self.clock.config(text = time_string)
        self.clock.after(200, self.tick)
    
       
    def inicia_clock(self):
        
        self.clock.grid(row = 0, column = 1)    
        self.tick()


#relogio = Clock()
#relogio.iniciar()