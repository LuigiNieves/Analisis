import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

X=sp.symbols('X')

def minimos_cuadrados(dx,dy):
  x = sp.symbols('x')
  m = len(dx)
  Sy = sum(dy)
  Sx = sum(dx)
  Sx_2 = sum([k**2 for k in dx])
  Sxy = sum([a*b for a,b in zip(dx,dy)])
  denominador = (m*Sx_2 - Sx**2)
  a0 = (Sy*Sx_2-Sx*Sxy)/denominador
  a1 = (m*Sxy-Sx*Sy)/denominador
  m = a0 + a1*x
  return a0,a1

def p_simple(xdata,ydata):
  N=len(xdata)
  M=np.zeros([N,N])
  P=0
  for i in range(N):
    M[i,0]=1
    for j in range(1,N):
      M[i,j]= M[i,j-1]*xdata[i]

  ai = np.linalg.solve(M,ydata)
  for i in range(N):
    P = P+ai[i]*X**i
  return sp.lambdify(X,P),P


def lagrange(xdata,ydata):
  N = len(xdata)
  P = 0
  for i in range(N):
    T=1
    for j in range(N):
      if j!=i:
        T = T*(X-xdata[j])/(xdata[i]-xdata[j])
    P = P + T*ydata[i]
  print('El polinomio interpolante es : P(X)=' ,P)
  return sp.lambdify(X,P)