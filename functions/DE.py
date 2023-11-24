import numpy as np

def Euler(f,a,b,h,co):
  n=int((b-a)/h)
  t=np.linspace(a,b,n+1)
  yeu=[co]
  for i in range(n):
      yeu.append(yeu[i]+h*f(t[i],yeu[i]))
  return t,yeu


def runge4(f,a,b,h,co):
  n= int((b-a)/h)
  t = np.linspace(a,b,n+1)
  yk=[co]
  for i in range(n):
    k1=h*f(t[i],yk[i])
    k2=h*f(t[i]+h/2,yk[i]+1/2*k1)
    k3=h*f(t[i]+h/2, yk[i]+1/2*k2)
    k4=h*f(t[i+1],yk[i]+k3)
    yk.append(yk[i]+1/6*(k1+2*k2+2*k3+k4))
  return t,yk