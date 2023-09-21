import numpy as np
def funcion(x):
    return x**2



def Simpson3(a,b, n, Function):
    
    prueba=np.linspace(a,b,n)
    h=(b-a)/n
    suma=0
    
    prueba=prueba[::2]
    print(prueba)
    for i in range(len(prueba)-3):

        s=Function(prueba[i])+4*(Function(prueba[i+1]))+Function(prueba[i+2])
        suma += s
        print(prueba[i])
    suma*(h/3)
    return suma

print(Simpson3(0,1,101,funcion))

        
        





