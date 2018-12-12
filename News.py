from gnewsclient import gnewsclient
import requests
from io import BytesIO
import tkinter as tk
from PIL import ImageTk, Image
import os
from urllib.request import urlopen





#import matplotlib.pyplot as plt

# Sincronização das notícias do Gloogle News Feed por uma Api
# https://pypi.org/project/gnewsclient/

class News:
    
    def __init__(self, telinha):
        self.telinha = telinha
        self.janela = self.telinha.janelinha
        self.news = None
        self.lista_imagens = []
        self.lista_titulos = []
        tamanho = 50
        self.largura = 4*tamanho
        self.altura = 3*tamanho
        self.titulo = tk.Label(self.janela, font=("times", 20, "bold"),fg = "white", bg = "black")
        self.imagem = tk.Label(self.janela, width = self.largura, height = self.altura)
        self.i = 0        
        self.temponoticia = 10000 #[ms]
        

    def parametros(self):
        
        self.client.edition = 'Brazil'
        self.client.topic = 'sports'
        self.client.location = 'Brazil'
        self.client.language = 'portuguese'

    def inicia_noticias(self):
        self.atualiza_news()
      

        
            
    def update_titulo_imagem(self):
        
        if len(self.news) == 0:
            self.titulo.after(self.temponoticia, self.atualiza_news)
            
        elif self.i < len(self.news):
            response = requests.get(self.news[self.i]["img"])
            img = Image.open(BytesIO(response.content))
            img = img.resize((self.largura, self.altura), Image.ANTIALIAS) 
            foto = ImageTk.PhotoImage(img)

            self.titulo.config(text = self.news[self.i]["title"])
            self.imagem.config(image = foto)
            self.image = foto
            
            self.titulo.place(x = self.largura + 30, y = self.telinha.janelinha.winfo_screenheight() - 55)
            self.imagem.place(x = 20, y = self.telinha.janelinha.winfo_screenheight() - self.altura - 30 )
            
            self.i += 1
            self.titulo.after(self.temponoticia, self.update_titulo_imagem)
            
            
            

        else:
            self.i = 0
            self.atualiza_news()
            

           
            
            
    def atualiza_news(self):
        self.client = gnewsclient()
        self.parametros()
        try:
            self.news = self.client.get_news()
        except IndexError:
            self.news = []
            self.update_titulo_imagem()
        
        
        

