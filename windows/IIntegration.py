import tkinter as tk
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from functions.Integration import *
import sympy as sp
from sympy import exp,log,sin,cos,tan,cot,sec,csc,pi
import numpy as np
import matplotlib.pyplot as plt



def isNumeric(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

class AIntegration(tk.Frame):
  def __init__(self, parent, controller,squares=0):
    super().__init__(parent)
    self.configure(background = "alice blue")
    self.controller =controller  
    self.squares =  squares
    self.entries =[]
    self.widget()

  
  def create_instructions(self,text):
    tk.Label(self,text=f'{text}, puede utilizar las siguientes nomenclaturas (exp,log,sin,cos,tan,cot,sec,csc,pi), utilice solo x (mínuscula) como variable, recuerde las reglas de los métodos, recuerde que el tamaño de los xdata y ydata deben ser iguales', wraplength=700,justify='left').grid(row=0, column=0, padx=1, pady=1, sticky='ew',columnspan=4)
    
  def widget(self):
    for idx, label_text in enumerate(self.squares):
      label = tk.Label(self, text=label_text, width=3,)
      label.grid(row=idx+1, column=0, padx=1, pady=1, sticky='ew')
      entry = tk.Entry(self, width=45)
      entry.grid(row=idx+1, column=1, padx=1, pady=1, sticky='w')
      self.entries.append(entry)

  
  def show_result(self,graph):    
    top = tk.Toplevel(self)
    top.title("Tabla de datos")
    canvas = FigureCanvasTkAgg(graph, master=top)
    canvas.draw()
    canvas.get_tk_widget().pack()
  
  def graph(self,f,a,b,n):
    y = np.linspace(min(a,b),max(a,b),int(n+1))
    fig=plt.figure(figsize=(6, 4))
    plt.plot(y,[f(x) for x in y])
    plt.grid()
    plt.title(f'Funcion en el tramo {a} - {b}')
    return fig
  
  def graph_trapecio_datos(self,x,y):
    # y = np.linspace(min(a,b),max(a,b),int(n+1))
    fig=plt.figure(figsize=(6, 4))
    plt.plot(x,y,'or')
    plt.grid()
    plt.title(f'Funcion en el tramo {min(x)} - {max(x)}')
    return fig


class CTrapeze(AIntegration):
  def __init__(self, parent, controller, squares=0):
    squares = ["f","a","b","n"]
    super().__init__(parent, controller, squares)
    last_row = self.grid_size()[1] - 1

    self.create_instructions('Trapecio con función')
    
    self.result = tk.Label(self, text="" , width=65)
    self.result.grid(row=last_row+1, column=1, padx=1, pady=1,sticky='nsew' )
    
    execute = tk.Button(self,text="Ejecutar",command=lambda:self.solve_trapecio())  
    execute.grid(row=last_row+2, column=0, padx=2, pady=5)

  def solve_trapecio(self):
    x = sp.symbols('x')
    try:
      f,a,b,n = eval(self.entries[0].get()),float(self.entries[1].get()),float(self.entries[2].get()),float(self.entries[3].get())
      I = trapecio(f,a,b,n)
      self.result.config(text=f'El area bajo la curva es aproximadamente {I} U^2')
      f = sp.lambdify(x,f)
      graph = self.graph(f,a,b,n)
      self.show_result(graph)
    except Exception as e:
      messagebox.showinfo("Error",e)  
      
      
class CTrapezePuntos(AIntegration):
  def __init__(self, parent, controller, squares=0):
    squares = ["xdata","ydata"]
    super().__init__(parent, controller, squares)
    last_row = self.grid_size()[1] - 1

    self.create_instructions('Trapecio con datos, puedes dejar el ydata vacío si quieres para casos especificos que es necesario')

    
    self.result = tk.Label(self, text="" , width=65)
    self.result.grid(row=last_row+1, column=1, padx=1, pady=1,sticky='nsew' )
    
    execute = tk.Button(self,text="Ejecutar",command=lambda:self.solve_trapecio_Puntos())  
    execute.grid(row=last_row+2, column=0, padx=2, pady=5)

  def solve_trapecio_Puntos(self):
    x = sp.symbols('x') 
    try:
      xdata = [float(i) for i in self.entries[0].get().split(' ') if isNumeric(i)]
      ydata = [float(i) for i in self.entries[1].get().split(' ') if isNumeric(i)]
        
      I = trapecio_datos(xdata,ydata) 
      self.result.config(text=f'El area bajo la curva es aproximadamente {I} U^2')
      if ydata:
        graph = self.graph_trapecio_datos(xdata,ydata)
        self.show_result(graph)
    except Exception as e:
      messagebox.showinfo("Error",e)      

class CSimpson13(AIntegration):
  def __init__(self, parent, controller, squares=0):
    squares = ["f","a","b","n"]
    super().__init__(parent, controller, squares)
    last_row = self.grid_size()[1] - 1

    self.create_instructions('Simpson 1/3, recuerda que solo se permite n par, osea múltiplo de 2')

    
    self.result = tk.Label(self, text="" , width=65)
    self.result.grid(row=last_row+1, column=1, padx=1, pady=1,sticky='nsew' )
    
    execute = tk.Button(self,text="Ejecutar",command=lambda:self.solve_simpson13())  
    execute.grid(row=last_row+2, column=0, padx=2, pady=5)

  def solve_simpson13(self):
    x = sp.symbols('x')
    try:
      f,a,b,n = eval(self.entries[0].get()),float(self.entries[1].get()),float(self.entries[2].get()),float(self.entries[3].get())
      f = sp.lambdify(x,f)
      I = simpson13(f,a,b,n)
      self.result.config(text=f'El area bajo la curva es aproximadamente {I} U^2')
      graph = self.graph(f,a,b,n)
      self.show_result(graph)
    except Exception as e:
      messagebox.showinfo("Error",e)
      
      
class CSimpson38(AIntegration):
  def __init__(self, parent, controller, squares=0):
    squares = ["f","a","b","n"]
    super().__init__(parent, controller,  squares)
    last_row = self.grid_size()[1] - 1

    self.create_instructions('Simpson 1/3, recuerda que solo se permite n múltiplo de 3')

    
    self.result = tk.Label(self, text="" , width=65)
    self.result.grid(row=last_row+1, column=1, padx=1, pady=1,sticky='nsew' )
    
    execute = tk.Button(self,text="Ejecutar",command=lambda:self.solve_simpson38())  
    execute.grid(row=last_row+2, column=0, padx=2, pady=5)

  def solve_simpson38(self):
    x = sp.symbols('x')
    try:
      f,a,b,n = eval(self.entries[0].get()),float(self.entries[1].get()),float(self.entries[2].get()),float(self.entries[3].get())
      f = sp.lambdify(x,f)
      I = simpson38(f,a,b,n)
      self.result.config(text=f'El area bajo la curva es aproximadamente {I} U^2')
      graph = self.graph(f,a,b,n)
      self.show_result(graph)
    except Exception as e:
      messagebox.showinfo("Error",e)    
      