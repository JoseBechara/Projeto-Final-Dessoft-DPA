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

import os





class interface:
    def __init__(self):
        self.janelinha = tk.Tk()
        self.janelinha.title("SmartMirror")
        pad = 1
        self.janelinha.geometry("{0}x{1}+0+0".format(self.janelinha.winfo_screenwidth() - pad, self.janelinha.winfo_screenheight() - 10*pad))
        self.janelinha.resizable(0, 0)

        
        self.janelinha.configure(background = "black")
        self.cl = Clock(self)
        self.tempo = tempo(self)
        self.news = News(self)
#        self.camera = camera(self)
        
    def iniciar(self):
       
        self.cl.inicia_clock()
        self.tempo.inicia_tempo()
        self.news.inicia_noticias()
        while True:
            
            self.janelinha.update()
#        self.Camera.webcam()
        
main = interface()
main.iniciar()