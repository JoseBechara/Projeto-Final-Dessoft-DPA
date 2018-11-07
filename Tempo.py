#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 14:11:06 2018

@author: joseantonio
"""
# Sincronização da previsão do Yahoo Weather por uma Api
# https://pypi.org/project/weather-api/

import tkinter as tk
from weather import Weather, Unit


class tempo:
    
    def __init__(self, telinha):
        self.telinha = telinha
        self.janela = self.telinha.janelinha
        self.previsao = tk.Label(self.janela, font=("times", 50, "bold"),fg = "white", bg = "blue")
        
        
        
        
    def clima(self):
        self.weather = Weather(unit=Unit.CELSIUS)
        self.location = self.weather.lookup_by_location('sao paulo')
        self.condition = self.location.condition
        self.previsao.config(text = "{0} ˚C  \n {1}".format(self.condition.temp, self.condition.text))
        self.previsao.after(200, self.clima)     


    def inicia_tempo(self):
        self.previsao.place(x = 1260, y = 0)
        print(self.previsao.cget("width"))
        print(self.previsao.winfo_height())
        self.clima()



#for i in dir(condition):
#    print(i)

