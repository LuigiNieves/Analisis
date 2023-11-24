import sympy as sp
import numpy as np

def factorial(x):
  total = 1
  for i in range(1,int(x+1)):
    total*=i
  return total
        

def Taylor(f,x0,n):
  P=0
  x = sp.symbols('x')
  for i in range(int(n+1)):
    df = sp.diff(f,x,i).subs({x:x0})
    T = (df*(x-x0)**i)/factorial(i)
    P += T
  return P


def Cota_t(f,x_,n,x0):
    x = sp.symbols('x')
    df = sp.diff(f,x,int(n+1))
    df = sp.lambdify(x,df)
    U=np.linspace(min(x_,x0),max(x_,x0),1000)
    Max = np.max(np.abs(df(U)))
    cota = (Max*(x_-x0)**(n+1))/factorial(n+1)
    return cota

def diferenciacion(intervalos:list,h: float,x0: float,k):
    valores = [x0]
    inicial,final = intervalos
    puntos = int((final - inicial)/h)
    t = np.linspace(inicial,final,puntos+1)
    for i in range(puntos):
        valores.append(k(valores[i])*h + valores[i])
    return t,valores

