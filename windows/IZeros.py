import tkinter as tk
from functions.Zeros import *
from sympy import symbols,lambdify,exp,log
from tkinter import ttk


class Home(tk.Frame):
  def __init__(self,parent,controller):
    super().__init__(parent)
    # self.configure(background = style.BACKGROUND)
    self.controller =controller
    self.gameMode = tk.StringVar(self, value="normal")
    self.crearwidgets()
      
  def crearwidgets(self):
    """ crear botones b o Cancelar""" 
    pass

# class Caja(tk.Frame):
#   def __init__(self, parent, controller):
#     super().__init__(parent)
#     self.configure(background = "blue")
#     self.controller =controller 
  
class AZeros(tk.Frame):
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
    
  def show_result(self,data):    
    top = tk.Toplevel(self)
    top.title("Tabla de datos")

    tree = ttk.Treeview(top, columns=("Columna 1", "Columna 2"), show="headings")
    tree.heading("Columna 1", text="Dato")
    tree.heading("Columna 2", text="Descripción")

    for dato, descripcion in data:
      tree.insert("", "end", values=(dato, descripcion))

    tree.pack()   

class CNewton(AZeros):
  def __init__(self, parent, controller, orden=0):
    cuadros = ["f","a","t"]
    super().__init__(parent, controller, orden,cuadros)
    
    execute = tk.Button(self,text="Ejecutar",command=lambda:self.solve_newton())  
    execute.grid(row=4, column=0, padx=10, pady=5) 
    
  def solve_newton(self): 
    try:
      x=symbols('x')
      a = newton(eval(self.entries[0].get()), float(self.entries[1].get()), float(self.entries[2].get()))
      print(a)
      self.show_result(a)  
      # ultima_fila = self.grid_size()[1] - 1
    except Exception as e:
      print(e) 

class CSecante(AZeros):
  def __init__(self, parent, controller, orden=1):
    cuadros = ["f","a","b","t"]
    super().__init__(parent, controller, orden,cuadros)  
    
    execute = tk.Button(self,text="Ejecutar",command=lambda:self.solve_secante())  
    execute.grid(row=4, column=0, padx=10, pady=5) 
    
    
  def solve_secante(self): 
    try:
      x=symbols('x')
      a = secante(eval(self.entries[0].get()), float(self.entries[1].get()), float(self.entries[2].get()) , float(self.entries[3].get()))
      print(a)
      # ultima_fila = self.grid_size()[1] - 1
    except Exception as e:
      print(e)    
    
class CBiseccion(AZeros):
  def __init__(self, parent, controller, orden=1):
    cuadros = ["f","a","b","t"]
    super().__init__(parent, controller, orden,cuadros)  
    
    execute = tk.Button(self,text="Ejecutar",command=lambda:self.solve_biseccion())  
    execute.grid(row=4, column=0, padx=10, pady=5)  
    
  def solve_biseccion(self): 
    try:
      x=symbols('x')
      a,b = biseccion(eval(self.entries[0].get()), float(self.entries[1].get()), float(self.entries[2].get()) , float(self.entries[3].get()))
      print(a,b)
      # ultima_fila = self.grid_size()[1] - 1
    except Exception as e:
      print(e)     
     
class CFalsaPosicion(AZeros):
  def __init__(self, parent, controller, orden=1):
    cuadros = ["f","a","b","t"]
    super().__init__(parent, controller, orden,cuadros)  
    
    execute = tk.Button(self,text="Ejecutar",command=lambda:self.solve_Fal())  
    execute.grid(row=4, column=0, padx=10, pady=5)     
  
  def solve_biseccion(self): 
    try:
      x=symbols('x')
      a,b = biseccion(eval(self.entries[0].get()), float(self.entries[1].get()), float(self.entries[2].get()) , float(self.entries[3].get()))
      print(a,b)
      # ultima_fila = self.grid_size()[1] - 1
    except Exception as e:
      print(e)   
          