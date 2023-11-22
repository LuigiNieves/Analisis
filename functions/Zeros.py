import pandas as pd
import numpy as np
import sympy as sp 

x = sp.symbols('x')

def newton(f,x0,tol):
    f_1 = f.diff(x)
    N = x0 - f/f_1
    N = sp.lambdify(x,N)
    # F = sp.lambdify(x,f)
    # F_1 = sp.lambdify(x,f_1)
    c = N(x0)
    d=[[x0,'-']]

    while np.abs((c-x0)) > tol:
        d.append([c,np.abs((c-x0)) ]) 
        c = N(x0)
        x0 = c         
    return c,d
  
def biseccion(f,a,b,tol):
    f = sp.lambdify(x,f)
    iter = 0 
    L=[[b,'-']]
    if f(a)*f(b) > 0:
        print('La funcion no cumple el teorema',f(a),'y ',f(b))
    else:
        while np.abs(b-a) > tol:
            iter+=1
            c = (a+b)/2
            if f(a)*f(c) < 0:
                ea = np.abs(b-c)
                b=c
            else:
                ea = np.abs(a-c)
                a=c
            L.append([c,ea])    
            # print('La raiz de la funcion es: ',c, 'iter', iter, 'intervalo ',a,b)
    return c,L  

def falsaPosicion(f,a,b,tol):
    f = sp.lambdify(x,f)
    iter = 0 
    ea=1
    L=[[b,'-']]
    if f(a)*f(b) > 0:
        print('La funcion no cumple el teorema',f(a),'y ',f(b))
    else:
        c = b-((f(b)*(a-b))/(f(a)-f(b)))
        while ea > tol:
            iter+=1
            c = a-((f(a)*(a-b))/(f(a)-f(b)))
            if f(a)*f(c) < 0:
                ea = np.abs(b-c)
                b=c
            else:
                ea = np.abs(a-c)
                a=c
            L.append([c,ea])
    return c,L 

def secante(f,x0,x1,tol):
    F = sp.lambdify(x,f)
    c = x1 - (F(x1)*(x1-x0))/(F(x1)-F(x0))
    d=[[x1,np.abs((c-x1))]]
    while np.abs((c-x1)) > tol :
        ea = np.abs((c-x1))
        x1 = x0
        x0 = c
        d.append([c,ea]) 
        c = x1 - (F(x1)*(x1-x0))/(F(x1)-F(x0))        
    return c,d
  