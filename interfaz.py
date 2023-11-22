import tkinter as tk
import tkinter
from tkinter import Label, StringVar, ttk,messagebox
from funciones import Newton,biseccion,falsaPosicion,secante,imprimir
import ast
from sympy import latex,sympify,symbols,parse_expr,lambdify
class Home(tk.Frame):

  def __init__(self,parent,controller):
    super().__init__(parent)
    # self.configure(background = style.BACKGROUND)
    self.controller =controller
    self.gameMode = tk.StringVar(self, value="normal")
    self.crearwidgets()
      
  def imprimir(x,y):
    pass

  def crearwidgets(self):
    """ crear botones b o Cancelar""" 
    pass

class cajas(tk.Frame):
  def __init__(self, parent, controller):
    super().__init__(parent)
    self.configure(background = "blue")
    self.controller =controller 
  
class AbstracCeros(tk.Frame):
  def __init__(self, parent, controller,orden=0,cuadros=0):
    super().__init__(parent)
    self.configure(background = "blue")
    self.controller =controller  
    self.orden = orden
    self.cuadros =  cuadros
    self.entries =[]
    self.widget()
    
  
  def widget(self):
    for idx, label_text in enumerate(self.cuadros):
      label = tk.Label(self, text=label_text)
      label.grid(row=idx, column=0, padx=10, pady=5)
      entry = tk.Entry(self)
      entry.grid(row=idx, column=1, padx=10, pady=5)
      
      # entry.bind("<KeyRelease>", lambda event, idx=idx: self.obtener_contenido(event, idx))
      self.entries.append(entry) 
      
    
     
      
      

class CNewton(AbstracCeros):
  def __init__(self, parent, controller, orden=0):
    cuadros = ["f","a","t"]
    super().__init__(parent, controller, orden,cuadros)
    
    ejecutar = tk.Button(self,text="ejecutar",command=lambda:self.RevNewton())  
    ejecutar.grid(row=4, column=0, padx=10, pady=5) 
    
  def RevNewton(self): 
    x=symbols('x')
    # a=sympify(self.entries[0].get())
    # print(a)
    a,b = Newton(eval(self.entries[0].get()), float(self.entries[2].get()), float(self.entries[2].get()))
    print(a,b)
    
    # ultima_fila = self.grid_size()[1] - 1
    # print(type(parse_expr("x**2-6")),parse_expr(self.entries[0].get()))
    # label = tk.Label(self, text=a)
    # label.grid(row=8, column=0, padx=10, pady=5)
    
  
    
    

class Otros(AbstracCeros):
  def __init__(self, parent, controller, orden=1):
    cuadros = ["f","a","b","t"]
    super().__init__(parent, controller, orden,cuadros)        