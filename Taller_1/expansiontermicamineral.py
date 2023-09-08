# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 15:29:32 2023

@author: simon


"""

from Lista_minerales import lista_creaciónObjeto
ruta_archivo= "/Users/simon/OneDrive/Documentos/3er semestre/MCI/Talleres/minerales.txt"
with open(ruta_archivo, encoding='utf-8') as f:
          lineas=f.readlines() 


Minerales= lista_creaciónObjeto(lineas)
Olivino= Minerales[14]
import matplotlib.pyplot as plt

class Mineral:

    def __init__(self, nombre, dureza, lustre, rompimiento_por_fractura, color, composicion, sistema_cristalino, specifix_gravity):
        self.nombre = nombre
        self.dureza = float(dureza)
        self.lustre = lustre
        self.rompimiento_por_fractura = rompimiento_por_fractura
        self.color = color
        self.composicion = composicion
        self.sistema_cristalino = sistema_cristalino
        self.specifix_gravity = specifix_gravity
    
    def silicato(self):
        if "Si" in self.composicion and "O" in self.composicion:
            salida= "True"
        else:
            salida= "False"
        return salida
   
    def Densidad(self):
        k=self.specifix_gravity*1000
        return k
    
    def Mostrar_color(self):
        fig, ax = plt.subplots()
        color = self.color
        rect = plt.Rectangle((0.5, 0.5), 0.5, 0.5, color=color)
        ax.add_patch(rect)
        ax.set_title('Color mineral')
        plt.show()
        
    def Imprimir_info(self):
        if self.rompimiento_por_fractura == "TRUE":
            tipo= "El mineral se rompe por fractura"
        else:
            tipo= "El mineral se rompe por escisión"
        print(str(self.dureza) + " "+tipo + " " + str(self.sistema_cristalino))



class ExpansionTermicaMineral(Mineral):
    def __init__(self,archivo,*args,**kwargs):
        self.Temperatura = []
        self.Volumen = []
        self.archivo = archivo
        super(ExpansionTermicaMineral,self).__init__(*args,**kwargs)
       
    def Coef_expansion(self):   
      with open(self.archivo, encoding='utf-8') as f:
          lineas=f.readlines()
      for c in lineas[1:]:
          Info=c.split(",")
          a=Info[1].replace("\n","")
          self.Temperatura.append(Info[0])
          self.Volumen.append(a)
      
          
    def DerivadaCentral(self,f:list,x:list):
         Datos_Derivada=[]
         h = x[1]-x[0]
         for k in range (1,len(f)-1):
         
             d=(f[k+1]-f[k-1])/(2*h)   
             Datos_Derivada.append(d)
             
         return Datos_Derivada
     

    def CoeficienteExpansion(self,Volumen,Temperatura,Derivada):
         
         alphas=[]
         for k in range(1,9):
           
           
           salida=(1/Volumen[k])*Derivada[k-1]
           alphas.append(salida)
           
         plt.subplot(1,2,1)
         plt.scatter(Temperatura, Volumen)
         plt.title('Gráfica1')

         plt.subplot(1,2,2)
         plt.scatter(Temperatura[1:9], alphas)
         return alphas

    
olivina = ExpansionTermicaMineral.__init__(Olivino,"olivine_angel_2017.csv")
print(olivina)