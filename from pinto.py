from tkinter import *
import requests
from bs4 import BeautifulSoup

# Meu Primeiro Programa em Python, fazendo Test's com a biblioteca Tkinter

class PrimeiroPy:
    
    def __init__(self):
        # self.janela = Tk()    
        # self.janela.title("Primeiro Programa")   
        # self.texto = Label(self.janela, text='Clique Aqui')
        pass
                          
    def Inicio(self) -> None:
        
       header = {'User-Agent': 'Mozilla/5.0,  (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0'} 
        
       resultado = requests.get('https://www.google.com/search?q=cotacao+dolar&oq=cotacao+dolar', headers=header)
       
       leitura = BeautifulSoup(resultado.text, 'html.parser')
       
       titulo = leitura.find('span', class_='DFlfde SwHCTb')
        
       print(leitura) 
      
    def Meio(self):
        pass
    
    
    def TerceiraParte(self):
        pass
    
    def TalvezFim(self):
        pass
        # self.janela.mainloop() 
    
    
    
inst = PrimeiroPy()
inst.Inicio()
inst.TalvezFim()
