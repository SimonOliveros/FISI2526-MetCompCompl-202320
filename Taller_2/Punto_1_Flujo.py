import numpy as np
import matplotlib.pyplot as plt


t=np.linspace(0,(2/7),101)

t_ajustada=t[1:100]
        
def DerivadaCentral(f:list,x:list):
         Datos_Derivada=[]
         h = x[1]-x[0]
         for k in range (1,len(f)-1):
         
             d=(f[k+1]-f[k-1])/(2*h)   
             Datos_Derivada.append(d)
             
         return Datos_Derivada

def flujo_anillo(r,B0,omega, f, t):
    salida= np.pi*(r**2)*B0*np.cos(omega*t)*np.cos(2*np.pi*f*t)
    return salida

flujo=flujo_anillo(0.125,0.05,3.5,7,t)
derivada_flujo=DerivadaCentral(flujo,t)

def corriente_inducida(R, derivada_flujo):
      corrientes=[]
      for i in derivada_flujo:
            k=-(1/R)*i
            corrientes.append(k)
      return corrientes



y=corriente_inducida(1750,derivada_flujo)
dy=DerivadaCentral(y, t_ajustada)

plt.scatter(t_ajustada,y)
#plt.show()

def Flujo(t:float):
     return float(np.pi*(0.125**2)*0.05*np.cos(3.5*t)*np.cos(2*np.pi*7*t))
def Derivative(f,x,h=1e-6):
    return (f(x+h)-f(x-h))/(2*h)
def corriente(t):
     return -(1/1750)*Derivative(Flujo,t)


def GetNewtonMethod(f,df,xn,itmax=100,precision=1e-8):
    
    error = 1.
    it = 0
    
    while error > precision and it < itmax:
        
        try:
            
            xn1 = xn - f(xn)/df(f,xn)
            # Criterio de parada
            error = np.abs(f(xn)/df(f,xn))
            
        except ZeroDivisionError:
            print('Division por cero')
            
        xn = xn1
        it += 1
        
   # print('Raiz',xn,it)
    
    if it == itmax:
        return False
    else:
        return xn
    


def GetAllRoots(x, tolerancia=10):
    
    Roots = np.array([])
    
    for i in x:
        
        root = GetNewtonMethod(corriente,Derivative,i)
        
        if root != False:
            
            croot = np.round(root, tolerancia)
            
            if croot not in Roots and croot>=0:
                Roots = np.append(Roots,croot)
                
    Roots.sort()
    
    return Roots
a=2/7
x = np.linspace(0,a,100)

Roots = GetAllRoots(x)
print(Roots)












