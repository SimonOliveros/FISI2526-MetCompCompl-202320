# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 15:29:30 2023

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