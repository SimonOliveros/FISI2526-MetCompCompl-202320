import numpy as np
import sympy as sym
import math as math
import matplotlib.pyplot as plt

x = sym.Symbol('x',real=True)
y = sym.Symbol('y',real=True)

def GetLaguerreRecursive(n,x):

    if n==0:
        poly = sym.Number(1)
    elif n==1:
        poly = 1-x
    else:
        poly = ((2*(n-1)+1-x)*GetLaguerreRecursive(n-1,x)-(n-1)*GetLaguerreRecursive(n-2,x))/n
   
    return sym.expand(poly, x)




def GetDLaguerre(n,x):
    Pn = GetLaguerreRecursive(n,x)
    return sym.diff(Pn,x,1)

def GetNewton(f,df,xn,itmax=10000,precision=1e-14):
    
    error = 1.
    it = 0
    
    while error >= precision and it < itmax:
        
        try:
            
            xn1 = xn - f(xn)/df(xn)
            
            error = np.abs(f(xn)/df(xn))
            
        except ZeroDivisionError:
            print('Zero Division')
            
        xn = xn1
        it += 1
        
    if it == itmax:
        return False
    else:
        return xn
    

def GetRoots(f,df,x,tolerancia = 10):
    
    Roots = np.array([])
    
    for i in x:
        
        root = GetNewton(f,df,i)

        if  type(root)!=bool:
            croot = np.round( root, tolerancia )
            
            if croot not in Roots:
                Roots = np.append(Roots, croot)
                
    Roots.sort()
    
    return Roots

def GetAllRootsGLag(n):
    N=n+(n-1)*n**(1/2)

    xn = np.linspace(0,N,300)
    
    Laguerre = []
    DLaguerre = []
    
    for i in range(n+1):
        Laguerre.append(GetLaguerreRecursive(i,x))
        DLaguerre.append(GetDLaguerre(i,x))
    
    poly = sym.lambdify([x],Laguerre[n],'numpy')
    Dpoly = sym.lambdify([x],DLaguerre[n],'numpy')
    Roots = GetRoots(poly,Dpoly,xn)

    if len(Roots) != n:
        ValueError('El número de raíces debe ser igual al n del polinomio.')
    
    return Roots



def GetWeightsGLag(n):

    Roots = GetAllRootsGLag(n)
    

    PolyLaguerre= sym.lambdify([x],GetLaguerreRecursive(n+1,x),'numpy')



    Weights = Roots/(((n+1)**2)*(PolyLaguerre(Roots)**2))
    
    return Weights

print(GetWeightsGLag(10))
def GetHermiteRecursive(n,x):

    if n==0:
        poly = sym.Number(1)
    elif n==1:
        poly = 2*x
    else:
        poly = (2*x*GetHermiteRecursive(n-1,x))-(2*(n-1)*GetHermiteRecursive(n-2,x))
   
    return sym.expand(poly,x)

def GetDHermite(n,x):
    Poly=GetHermiteRecursive(n,x)
    return sym.diff(Poly,x,1)


def GetAllRootsGHermite(n):
    N= (4*n+1)**(1/2)

    xn = np.linspace(-N,N,300)
    
    Hermite = []
    DHermite = []
    
    for i in range(n+1):
        Hermite.append(GetHermiteRecursive(i,x))
        DHermite.append(GetDHermite(i,x))
    
    poly = sym.lambdify([x],Hermite[n],'numpy')
    Dpoly = sym.lambdify([x],DHermite[n],'numpy')
    Roots = GetRoots(poly,Dpoly,xn)

    if len(Roots) != n:
        ValueError('El número de raíces debe ser igual al n del polinomio.')
    
    return Roots

def GetWeightsGHer(n):

    Roots = GetAllRootsGHermite(n)
    

    PolyHermite= sym.lambdify([x],GetHermiteRecursive(n-1,x),'numpy')



    Weights = ((2**(n-1))*math.factorial(n)*((np.pi)**(1/2)))/((n**2)*(PolyHermite(Roots))**2)
    
    return Weights
print(GetWeightsGHer(10))






def P(v,T,m,R):
    
    a=(m/(2*np.pi*R*T))**(3/2)
    b=v**2
    e=-((m*v**2)/(2*np.pi*R*T))
    p=4*np.pi
    return p*a*b*np.exp(e)

v=np.linspace(0,600,601)

for t in range(100,1100,100):
    y=P(v,t,1,1)
    x=v

    plt.scatter(x,y)
    plt.xlabel("Velocidad")
    plt.ylabel("Probabilidad")
    plt.title("Distribución de las velocidades de las moléculas de un gas ideal \n  para distintas temperaturas")

#plt.show()
#La velocidad más probable va aumentando a medida de que aumenta la temperatura

def P2(x):
    
    return x*(4*np.pi)*((1/(2*np.pi*8.314*100))**(3/2))*(x**2)*np.exp(-((1*x**2)/(2*np.pi*8.314*100)))


def IntWithLaguerre(n,f):
    Raices=GetAllRootsGLag(n)
    pesos=GetWeightsGLag(n)
    for i in range(n+1):
        R=Raices[i]
        r=pesos[i]*f(R)
        sum+=r
    return sum

print(IntWithLaguerre(8,P2(x)))






        
    

















