# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 14:59:28 2023

@author: nicoc
"""

import numpy as np

N_1 = 1000000
a = 0
b = np.pi
x_1 = np.random.uniform(a,b,N_1) #N es el número de muestras aleatorias que tomará
def func_integrate(x):
    return np.exp(-x)*np.sin(x)
fi = func_integrate(x_1)
I = (b-a)*sum(fi)/N_1
Iteo = 0.5*(1+np.exp(-np.pi))
print(f'El valor teórico es: {Iteo:.6f} y valor utilizando Monte Carlo es {I:.6f}, con un error porcentual de: {np.abs(1-I/Iteo): .6%}')


#opcion mas precisa basada en CHAT GPT 4.3

def MONTECARLO(num_samples):
    total = 0
    for _ in range(num_samples):
        x, y, z = np.random.uniform(-1, 1, 3)
        r_squared = x**2 + y**2 + z**2
        if r_squared <= 1:
            function_value = np.sin(r_squared) * np.exp(np.sin(r_squared))
            total += function_value

    volumen_esfera_radio1= (4/3) * np.pi
    integral_estimate = total*volumen_esfera_radio1 / num_samples 
    
    return integral_estimate

# Número de muestras para el método de Monte Carlo
num_samples = 100000

# Calcular la estimación de la integral
integral_estimate = MONTECARLO(num_samples)
print("Estimación de la integral:", integral_estimate)

#NUESTRA OPCION 

R = 1
N = 100000
x = np.random.uniform(-R,R,N)
y = np.random.uniform(-R,R,N)
z =np.random.uniform(-R,R,N)

suma = 0
N_IN=0
for i in range(N):
    if x[i]**2+y[i]**2+z[i]**2<=R**2:
        N_IN+=1
        suma += np.sin((x[i]**2)+(y[i]**2)+(z[i]**2))*np.e**((x[i]**2)+(y[i]**2)+(z[i]**2)) #Se suma la imagen pcón es 1

I = (suma/N)*(N_IN/N)*(R*2)**3
print(I)


