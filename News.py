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
        self.titulo = tk.Label(self.janela, font=("times", 20, "bold"),fg = "white", bg = "green")
        self.imagem = tk.Label(self.janela, width = self.largura, height = self.altura)
        self.i = 0        
        self.temponoticia = 3000 #[ms]
        

    def parametros(self):
        
        self.client.edition = 'Brazil'
        self.client.topic = 'sports'
        self.client.location = 'Brazil'
        self.client.language = 'portuguese'

    def inicia_noticias(self):
        self.atualiza_news()
        #self.titulo.after(self.temponoticia * len(self.news), self.inicia_noticias)

        
            
    def update_titulo_imagem(self):
        
        
        if self.i < len(self.news):
            response = requests.get(self.news[self.i]["img"])
            img = Image.open(BytesIO(response.content))
            foto = ImageTk.PhotoImage(img)
            img = ImageTk.PhotoImage(Image.open("/Users/joseantonio/Documents/GitHub/Projeto-Final-Dessoft-DPA/dory.png"))
#            print(foto)
            self.titulo.config(text = self.news[self.i]["title"])
            self.imagem.config(image = img)
            self.i += 1
            self.titulo.place(x = self.largura + 30, y = self.telinha.janelinha.winfo_screenheight() - 55)
            self.imagem.place(x = 20, y = self.telinha.janelinha.winfo_screenheight() - self.altura - 30 )
            self.titulo.after(self.temponoticia, self.update_titulo_imagem)
            

        else:
            self.i = 0
            self.atualiza_news()
            
#        print(img)
#        print('')
           
            
            
    def atualiza_news(self):
        self.client = gnewsclient()
        self.parametros()
        self.news = self.client.get_news()
        self.update_titulo_imagem()
        
        
        
# root = Tk()
# img = ImageTk.PhotoImage(Image.open("True1.gif"))
# panel = Label(root, image = img)
# panel.pack(side = "bottom", fill = "both", expand = "yes")
# root.mainloop()                  


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
