import pandas as pd
import numpy as np
import sympy as sp 

x = sp.symbols('x')

import sympy as sp

#Método de bisección
def biseccion(f,a,b,tolerancia=1E-6 ):
  if f(a)*f(b) > 0:
    return 'No cumple el teorema'
  c = (a+b)/2
  puntos = [[c,abs((b-a)/b)]]
  while abs(b - a) >= tolerancia:
    c = (a+b)/2
    if f(a)*f(c) < 0:
      b=c
    else:
      a=c
    puntos.append([c,abs((b-a)/b)])
  return puntos

# Método de falsa posición
def falsa_posicion(f,a,b,tolerancia = 0.01):
  if (f(a)*f(b)) > 0 :
    return 'No hay raices'
  c = a - ((f(a)*(a-b))/(f(a)-f(b)))
  puntos = [[c , f(c)]]
  while abs(f(c)) >= tolerancia:
    c = a - ((f(a)*(a-b))/(f(a)-f(b)))
    if f(a)*f(c) < 0:
      b=c
    else:
      a=c
    puntos.append([c,f(c)])
  return puntos

#Método de Newton
def newton(funcion,semilla,tolerancia=0.01):
  try:
    dx = funcion.diff(x)
  except:
    return 'Algo salio mal'
  if (dx == 0): return 'Derivada igual a 0'
  puntos = [[semilla,'-']]
  f = sp.lambdify(x,funcion)
  f_ = sp.lambdify(x,dx)
  xi = lambda: puntos[-1][0] - f(puntos[-1][0])/f_(puntos[-1][0])
  puntos.append([xi(),abs((xi() - puntos[-1][0])/xi())])
  while (abs(puntos[-1][0] - puntos[-2][0]) > tolerancia):
    puntos.append([xi(),abs((xi() - puntos[-2][0])/xi())])
  return puntos

#Método de secante
def secante(f,x_0,x_1,tolerancia=0.01):
  valores = [x_0,x_1]
  xi = lambda: valores[-1] - f(valores[-1])*(valores[-2] - valores[-1])/(f(valores[-2]) - f(valores[-1]))
  puntos = [[xi(),'-']]
  while (abs(valores[-1] - valores[-2]) >= tolerancia):
    valores.append(xi())
    puntos.append([xi(),abs((xi()-puntos[-1])/xi())])
  return puntos