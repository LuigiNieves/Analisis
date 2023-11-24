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
  return a0,a1,sp.lambdify(x,m)

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
  return P,sp.lambdify(X,P)


def lagrange(xdata,ydata):
  N = len(xdata)
  P = 0
  for i in range(N):
    T=1
    for j in range(N):
      if j!=i:
        T = T*(X-xdata[j])/(xdata[i]-xdata[j])
    P = P + T*ydata[i]
  return P,sp.lambdify(X,P)

def x2(x,y):
  return [i**2 for i in x],y

def x3(x,y):
  return [i**3 for i in x],y

def sqrtx(x,y):
  return [i**(1/2) for i in x],y

def logx(x,y):
  return [np.log(i) for i in x],y

def logy(x,y):
  return x,[np.log(i) for i in y]

def y2(x,y):
  return x,[i**2 for i in y]

def logxlogy(x,y):
  return [np.log(i) for i in x],[np.log(j) for j in y]

def divsqrty(x,y):
  return x,[1/i**(1/2) for i in y]


# functions = [
# x2,
# x3,
# sqrtx,
# logx,
# logy,
# y2,
# logxlogy,
# divsqrty,
# ]


def graficas9(x,y):
  x = np.array(x)
  y = np.array(y)
  plt.subplots_adjust(left=None, bottom=None,right=None,top=None,wspace=None,hspace=0.5)
  fig = plt.figure(figsize=(16,12))

  plt.subplot(331)
  plt.plot(x,y,'bo')
  plt.grid()
  plt.title('Datos observados')

  x_,y_ = x2(x,y)
  plt.subplot(332)
  plt.plot(x_,y_,'m*')
  plt.grid()
  plt.title('x^2')

  x_,y_ = x3(x,y)
  plt.subplot(333)
  plt.plot(x_,y_,'cd')
  plt.grid()
  plt.title('x^3')

  x_,y_ = sqrtx(x,y)
  plt.subplot(334)
  plt.plot(x_,y_,'yp')
  plt.grid()
  plt.title('sqrt(x)')

  x_,y_ = logx(x,y)
  plt.subplot(335)
  plt.plot(x_,y_,'bv')
  plt.grid()
  plt.title('log(x)')

  x_,y_ = logy(x,y)
  plt.subplot(336)
  plt.plot(x_,y_,'g*')
  plt.grid()
  plt.title('log(y)')

  x_,y_ = y2(x,y)
  plt.subplot(337)
  plt.plot(x_,y_,'rp')
  plt.grid()
  plt.title('sqrt(y)')

  x_,y_ = logxlogy(x,y)
  plt.subplot(338)
  plt.plot(x_,y_,'bs')
  plt.grid()
  plt.title('log(x) y log(y)')

  x_,y_ = divsqrty(x,y)
  plt.subplot(339)
  plt.plot(x_,y_,'y*')
  plt.grid()
  plt.title('1/sqrt(y)')
  
  return fig