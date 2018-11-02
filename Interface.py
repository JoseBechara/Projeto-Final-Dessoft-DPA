#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 16:25:35 2018

@author: joseantonio
"""

import sys
import tkinter as tk
from Relogio import Clock
from Tempo import tempo
from News import News

class interface:
    def __init__(self):
        self.janelinha = tk.Tk()
        self.janelinha.configure(background = "black")
        self.cl = Clock(self)
        self.tempo = tempo(self)
        self.news = News(self)
    
        
    def iniciar(self):
        self.cl.inicia_clock()
        self.tempo.inicia_tempo()
        self.news.inicia_noticias()
        self.janelinha.mainloop()
                
        
main = interface()
main.iniciar()