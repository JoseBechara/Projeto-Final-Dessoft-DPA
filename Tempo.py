#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 14:11:06 2018

@author: joseantonio
"""

import tkinter as tk
import sys
from weather import Weather, Unit

class tempo:
    
    def __init__(self, telinha):
        self.telinha = telinha
        self.janela = self.telinha.janelinha
        self.previsao = tk.Label(self.janela, font=("times", 50, "bold"),fg = "white", bg = "black")
        
        
        
    def clima(self):
        self.weather = Weather(unit=Unit.CELSIUS)
        self.location = self.weather.lookup_by_location('sao paulo')
        self.condition = self.location.condition
        self.previsao.config(text = "{0} ˚C  \n {1}".format(self.condition.temp, self.condition.text))
        self.previsao.after(200, self.clima)     


    def inicia(self):
        self.previsao.grid(row = 0, column = 0)
        self.clima()



#for i in dir(condition):
#    print(i)

