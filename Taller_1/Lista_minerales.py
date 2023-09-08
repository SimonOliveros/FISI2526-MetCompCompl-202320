# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 15:29:31 2023

@author: simon
"""
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
        if "Si" and "O" in self.composicion:
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
ruta_archivo= "/Users/simon/OneDrive/Documentos/3er semestre/MCI/Talleres/minerales.txt"
with open(ruta_archivo, encoding='utf-8') as f:
          lineas=f.readlines()    

def lista_creaciónObjeto(lineas):    
    minerales=[]    
    for k in lineas[1:]:
       Minerales_ejemplo = k.split("\t")

       nombre_min= Minerales_ejemplo[0]
       dureza_min= Minerales_ejemplo[1]
       lustre_min= Minerales_ejemplo[5]
       rompimiento_min= Minerales_ejemplo[2]
       color_min= Minerales_ejemplo[3]
       composicion_min= Minerales_ejemplo[4]
       densidad_min= float(Minerales_ejemplo[6])
       sistema_min= Minerales_ejemplo[7]
    
       mineral_i = Mineral(nombre_min,dureza_min,lustre_min,rompimiento_min,color_min,composicion_min,sistema_min,densidad_min)

       minerales.append(mineral_i)
    return minerales

def contar_sili(minerales)->int:
    cont=0
    for mineral in minerales:
      if mineral.silicato() == "True":
        cont+=1
    return cont

def Dens_prom(minerales)->float:
    suma=0
    for mineral in minerales:
        suma+=float(mineral.Densidad())
    resultado=suma/17
    return resultado

print(lista_creaciónObjeto(lineas))


