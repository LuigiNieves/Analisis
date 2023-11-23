import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from PIL import Image, ImageTk

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

def graficas9(x,y):
  plt.subplots_adjust(left=None, bottom=None,right=None,top=None,wspace=None,hspace=0.5)
  plt.figure(figsize=(16,12))

  plt.subplot(331)
  plt.plot(x,y,'bo')
  plt.grid()
  plt.legend()
  plt.title('Datos observados')


  plt.subplot(332)
  plt.plot(x**2,y,'m*')
  plt.grid()
  plt.legend()
  plt.title('x^2')


  plt.subplot(333)
  plt.plot(x**3,y,'cd')
  plt.grid()
  plt.legend()
  plt.title('x^3')


  plt.subplot(334)
  plt.plot(x**(1/2),y,'yp')
  plt.grid()
  plt.legend()
  plt.title('sqrt(x)')



  plt.subplot(335)
  plt.plot(np.log(x),y,'bv')
  plt.grid()
  plt.legend()
  plt.title('log(x)')


  plt.subplot(336)
  plt.plot(x,np.log(y),'g*')
  plt.grid()
  plt.legend()
  plt.title('log(y)')


  plt.subplot(337)
  plt.plot(x,y**2,'rp')
  plt.grid()
  plt.legend()
  plt.title('sqrt(y)')


  plt.subplot(338)
  plt.plot(np.log(x),np.log(y),'bs')
  plt.grid()
  plt.legend()
  plt.title('log(x) y log(y)')


  plt.subplot(339)
  plt.plot(x,1/y**(1/2),'y*')
  plt.grid()
  plt.legend()
  plt.title('1/sqrt(y)')