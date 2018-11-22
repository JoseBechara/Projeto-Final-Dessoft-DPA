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
from Traducao_previsao import tempotraduzido
from PIL import ImageTk, Image
import os

caminho = os.path.abspath(__file__)
imagem = os.path.join(os.path.dirname(caminho),"PNGs/Tornado.png")



class tempo:
    
    def __init__(self, telinha):
        self.telinha = telinha
        self.janela = self.telinha.janelinha
        self.previsao = tk.Label(self.janela, font=("times", 50, "bold"),fg = "white", bg = "black")
        self.figura = None  
        tamanho = 40
        self.largura = 4*tamanho
        self.altura = 3*tamanho
        
    def clima(self):
        self.weather = Weather(unit=Unit.CELSIUS)
        self.location = self.weather.lookup_by_location('sao paulo')
        self.condition = self.location.condition
        
        self.previsao.config(text = "{0} ˚C  \n {1}".format(self.condition.temp, tempotraduzido[int(self.condition.code)]))
        
        self.previsao.place(x = self.telinha.janelinha.winfo_screenwidth() - self.previsao.winfo_reqwidth() - 10, y = 0)

        
        img = Image.open(imagem)
        
        img = img.resize((self.largura, self.altura), Image.ANTIALIAS)
        
        foto = ImageTk.PhotoImage(img)

        self.figura = tk.Label(self.janela, width = self.largura, height = self.altura, image = foto)
        
        self.figura.place(x = self.telinha.janelinha.winfo_screenwidth() - self.previsao.winfo_reqwidth() - self.figura.winfo_reqwidth() - 10, y = 0)

        self.previsao.after(60000, self.clima)  
        

        self.janela.update()
        
    def inicia_tempo(self):
        

        self.clima()
        self.previsao.update()
        self.figura.update()
