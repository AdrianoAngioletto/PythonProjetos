from tkinter import *
import requests
from bs4 import BeautifulSoup

# Meu Primeiro Programa em Python, fazendo Test's com a biblioteca Tkinter #Cotando o Dolar

class PrimeiroPy:
    
    def __init__(self):
        
        self.janela = Tk()
        
        imagem = PhotoImage(file='dollar.png')
        
        self.janela.iconbitmap('dolar.ico')

        self.label_fundo = Label(self.janela, image=imagem)
        
        self.label_fundo.image = imagem
        
        self.label_fundo.place(relwidth=1, relheight=1)
        
        self.janela.geometry("800x600")
        
        self.janela.title("Cotando Dolar")   
        
        self.botao = Button(self.janela, text='Ver cotação', command=self.Inicio)
        
        self.botao.pack()
        
        self.texto = Label(self.janela, text='')  
        
        self.texto.pack()
                          
    def Inicio(self):
        
       header = {'User-Agent': 'Mozilla/5.0,  (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0'} 
        
       resultado = requests.get('https://www.google.com/search?q=cotacao+dolar&oq=cotacao+dolar', headers=header)
       
       leitura = BeautifulSoup(resultado.text, 'html.parser')
       
       titulo = leitura.find('span', class_='DFlfde SwHCTb')
       
       lista_de_valores = []
       
       valor = titulo.get_text()
       
       lista_de_valores.append(valor)
       
       self.texto.config(text=f'Cotação do dólar: {valor}')
        
       
    def Meio(self):
        pass
    
    
    def TerceiraParte(self):
        pass
    
    def TalvezFim(self):
        
        self.janela.mainloop() 
    
    
    
inst = PrimeiroPy()
inst.TalvezFim()
