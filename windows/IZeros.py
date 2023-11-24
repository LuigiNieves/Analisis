import tkinter as tk
from functions.Zeros import *
from sympy import symbols,exp,log,sin,cos,tan,cot,sec,csc,pi
from tkinter import ttk
from tkinter import messagebox

    
class AZeros(tk.Frame):
  def __init__(self, parent, controller,squares=0):
    super().__init__(parent)
    self.configure(background = "alice blue")
    self.controller =controller  
    self.squares =  squares
    self.entries =[]
    self.widget()
  

  def create_instructions(self,text):
    tk.Label(self,text=f'{text}, puede utilizar las siguientes nomenclaturas (exp,log,sin,cos,tan,cot,sec,csc,pi), utilice solo x (mínuscula) como variable, recuerde las reglas de los métodos', wraplength=700,justify='left').grid(row=0, column=0, padx=1, pady=1, sticky='ew',columnspan=4)
    

  def widget(self):
    for idx, label_text in enumerate(self.squares):
      label = tk.Label(self, text=label_text, width=3,)
      label.grid(row=idx+1, column=0, padx=1, pady=1, sticky='ew')
      entry = tk.Entry(self, width=45)
      entry.grid(row=idx+1, column=1, padx=1, pady=1, sticky='w')
      self.entries.append(entry)
    
  def show_result(self,data):    
    top = tk.Toplevel(self)
    top.title("Tabla de datos")

    tree = ttk.Treeview(top, columns=("Columna 1", "Columna 2"),show="headings")
    tree.heading("Columna 1", text="Raiz")
    tree.heading("Columna 2", text="Error")

    
    for dato, descripcion in data:
      tree.insert("", "end", values=(dato, descripcion))
    
    tree.tag_configure('oddrow', background='#F0F0F0') 
    tree.tag_configure('evenrow', background='white')  
    for i, item in enumerate(tree.get_children()):
      if i % 2 == 0:
          tree.item(item, tags=('evenrow',))
      else:
          tree.item(item, tags=('oddrow',))  

    tree.pack()   

class CNewton(AZeros):
  def __init__(self, parent, controller):
    squares = ["f","a","t"]
    super().__init__(parent, controller,squares)
    
    execute = tk.Button(self,text="Ejecutar",command=lambda:self.solve_newton())  
    execute.grid(row=5, column=0, padx=10, pady=5) 
    self.create_instructions('Newton')


    
  def solve_newton(self): 
    try:
      x=symbols('x')
      a = newton(eval(self.entries[0].get()), float(self.entries[1].get()), float(self.entries[2].get()))
      print(a)
      self.show_result(a)  
    except Exception as e:
      print(e) 

class CSecante(AZeros):
  def __init__(self, parent, controller):
    squares = ["f","a","b","t"]
    super().__init__(parent, controller,squares)  

    execute = tk.Button(self,text="Ejecutar",command=lambda:self.solve_secante())  
    execute.grid(row=5, column=0, padx=10, pady=5) 
    self.create_instructions('Secante')

    
  def solve_secante(self): 
    try:
      x=symbols('x')
      a = secante(eval(self.entries[0].get()), float(self.entries[1].get()), float(self.entries[2].get()) , float(self.entries[3].get()))
      print(a)
      self.show_result(a)
    except Exception as e:
      messagebox.showinfo("Error",e)  
    
class CBiseccion(AZeros):
  def __init__(self, parent, controller):
    squares = ["f","a","b","t"]
    super().__init__(parent, controller,squares) 
    self.create_instructions('Bisección')


    execute = tk.Button(self,text="Ejecutar",command=lambda:self.solve_biseccion())  
    execute.grid(row=5, column=0, padx=10, pady=5)  
    
  def solve_biseccion(self): 
    try:
      x=symbols('x')
      a = biseccion(eval(self.entries[0].get()), float(self.entries[1].get()), float(self.entries[2].get()) , float(self.entries[3].get()))
      print(a)
      self.show_result(a)
    except Exception as e:
      messagebox.showinfo("Error",e)      
     
class CFalsaPosicion(AZeros):
  def __init__(self, parent, controller):
    squares = ["f","a","b","t"]
    super().__init__(parent, controller,squares)  

    self.create_instructions('Falsa Posición')


    execute = tk.Button(self,text="Ejecutar",command=lambda:self.solve_falsaPosicion())  
    execute.grid(row=5, column=0, padx=10, pady=5)     
  
  def solve_falsaPosicion(self): 
    try:
      x=symbols('x')
      a = falsa_posicion(eval(self.entries[0].get()), float(self.entries[1].get()), float(self.entries[2].get()) , float(self.entries[3].get()))
      print(a)
      self.show_result(a)
    except Exception as e:
      messagebox.showinfo("Error",e)   
          