from gnewsclient import gnewsclient

from PIL import Image

import requests
from io import BytesIO
#


import tkinter as tk
# Sincronização das notícias Gloogle News Feed por uma Api
# https://pypi.org/project/gnewsclient/

class News:
    
    def __init__(self, telinha):
        self.telinha = telinha
        self.janela = self.telinha.janelinha
        self.client = gnewsclient()
        self.news = None
        self.lista_imagens = []
        self.lista_titulos = []
        self.titulo = tk.Label(self.janela, font=("times", 5, "bold"),fg = "white", bg = "black")
        #self.imagem = ...

    def parametros(self):
        
        self.client.edition = 'Brazil'
        self.client.topic = 'sports'
        self.client.location = 'Brazil'
        self.client.language = 'portuguese'
#        self.titulo.after(200, self.noticias)
#        self.imagem.after(200, self.noticias)



    def inicia_noticias(self):
        self.parametros()
        self.news = self.client.get_news()
        self.titulo_imagem()
        self.titulo.grid(row = 1, column = 0)
        
        
        
    def titulo_imagem(self):

        
        for noticia in self.news:
            self.lista_titulos.append(noticia["title"])        
        
        self.titulo.config(text = self.news[0]["title"])
            







#imagem = news[0]["img"]
#
#response = requests.get(imagem)
#img = Image.open(BytesIO(response.content))
#
#imgplot = plt.imshow(img)
#print(news[0]['title'])
#plt.show()
#
#
#print(img)
