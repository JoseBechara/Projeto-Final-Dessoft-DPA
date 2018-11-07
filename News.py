from gnewsclient import gnewsclient

from PIL import Image

import requests
from io import BytesIO
import time 

import tkinter as tk

# Sincronização das notícias Gloogle News Feed por uma Api
# https://pypi.org/project/gnewsclient/

class News:
    
    def __init__(self, telinha):
        self.telinha = telinha
        self.janela = self.telinha.janelinha
        self.news = None
        self.lista_imagens = []
        self.lista_titulos = []
        self.titulo = tk.Label(self.janela, font=("times", 10, "bold"),fg = "white", bg = "black")
        self.imagem = Label(self.janela, image = ImageTk.PhotoImage(Image.open("True1.gif")))
        self.i = 0
        self.temponoticia = 1000
        

    def parametros(self):
        
        self.client.edition = 'Brazil'
        self.client.topic = 'sports'
        self.client.location = 'Brazil'
        self.client.language = 'portuguese'
#        self.titulo.after(200, self.noticias)
#        self.imagem.after(200, self.noticias)

    def inicia_noticias(self):
        self.atualiza_news()
        self.titulo.after(self.temponoticia * len(self.news), self.inicia_noticias)

        
            
    def update_titulo_imagem(self):
        
#        for noticia in self.news:
            
            #self.lista_titulos.append(noticia["title"] + "\n")

        #self.lista_titulos = "\n".join(self.lista_titulos)      
        if self.i < len(self.news):
            self.titulo.config(text = self.news[self.i]["title"])
            self.i += 1
            #self.janela.update()
            self.titulo.after(self.temponoticia, self.update_titulo_imagem)
            self.titulo.grid(row = 1, column = 1)

        else:
            self.i = 0    
           
#            
#            print("passou por aqui")
            
#for i in range(5):
#News.update_titulo_imagem(4)
            
            
    def atualiza_news(self):
        self.client = gnewsclient()
        self.parametros()
        self.news = self.client.get_news()
        self.update_titulo_imagem()
        
        
        
root = Tk()
img = ImageTk.PhotoImage(Image.open("True1.gif"))
panel = Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")
root.mainloop()                  


#imagem = news[0]["img"]

#response = requests.get(imagem)
#img = Image.open(BytesIO(response.content))
#
#imgplot = plt.imshow(img)
#print(news[0]['title'])
#plt.show()
#
#
#print(img)
