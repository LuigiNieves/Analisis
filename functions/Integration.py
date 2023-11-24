import sympy as sp

x = sp.symbols('x')


def trapecio(f,a,b,n):
  f = sp.lambdify(x,f)
  h = (b-a)/n
  suma = 0
  for i in range(1,int(n)):
    suma+=f(a+i*h)
  I = h/2*(f(a) +2*suma +f(b))
  return I


def trapecio_datos(xi,yi = []):
  h = xi[1] - xi[0]
  extrem1, *rest, extrem2 = xi if len(yi) == 0 else yi
  return h/2*(extrem1 + 2* sum(rest) + extrem2)


def simpson13(f,a,b,n):
  if n%2 != 0:
    raise Exception('Se necesita un numero par')
  h = (b-a)/n
  even = odd = 0
  for i in range(1,int(n)):
    if i%2 == 0: even+=f(a+i*h)
    else: odd+=f(a+i*h)
  I = h/3*(f(a)+2*even+4*odd + f(b))
  return I

def simpson38(f,a,b,n):
  if n%3!= 0:
    raise Exception('Se necesita un numero multiplo de 3')
  h = (b-a)/n
  not_multiply_of_3 = multiply_of_3 = 0

  for i in range(1,int(n)):
    if i%3 == 0: multiply_of_3+=f(a+i*h)
    else: not_multiply_of_3+=f(a+i*h)
  I = 3*h/8*(f(a)+3*not_multiply_of_3+2*multiply_of_3 + f(b))
  return I