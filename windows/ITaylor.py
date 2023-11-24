import tkinter as tk
from functions.Interpolation import *
from sympy import symbols,lambdify,exp,log,sqrt
from tkinter import ttk
from functions.Taylor import Taylor,Cota_t
from sympy import sin,cos,tan
from tkinter import messagebox



class AZeros(tk.Frame):
  def __init__(self, parent, controller,orden=0,squares=0):
    super().__init__(parent)
    self.configure(background = "blue")
    self.controller =controller  
    # self.orden = orden
    self.squares =  squares
    self.entries =[]
    self.widget()
    
  def widget(self):
    for idx, label_text in enumerate(self.squares):
      label = tk.Label(self, text=label_text)
      label.grid(row=idx, column=0, padx=10, pady=5)
      entry = tk.Entry(self)
      entry.grid(row=idx, column=1, padx=10, pady=5)
      
      # entry.bind("<KeyRelease>", lambda event, idx=idx: self.obtener_contenido(event, idx))
      self.entries.append(entry)
    
  def show_result(self,data):    
    top = tk.Toplevel(self)
    top.title("Tabla de datos")

    tree = ttk.Treeview(top, columns=("Columna 1", "Columna 2"),show="headings")
    tree.heading("Columna 1", text="Raiz")
    tree.heading("Columna 2", text="Error")

    
    for dato, descripcion in data:
      tree.insert("", "end", values=(dato, descripcion))
    
    tree.tag_configure('oddrow', background='#F0F0F0')  # Color para filas impares
    tree.tag_configure('evenrow', background='white')  # Color para filas pares
    for i, item in enumerate(tree.get_children()):
      if i % 2 == 0:
          tree.item(item, tags=('evenrow',))
      else:
          tree.item(item, tags=('oddrow',))  

    tree.pack()   

class CTaylor(AZeros):
  def __init__(self, parent, controller, orden=0):
    squares = ["f","x0","n"]
    super().__init__(parent, controller, orden,squares)
    
    last_row = self.grid_size()[1] - 1
    
    self.result = tk.Label(self, text="" , width=65,wraplength=200)
    self.result.grid(row=last_row+1, column=1, padx=1, pady=1,sticky='nsew' )
    
    execute = tk.Button(self,text="Ejecutar",command=lambda:self.solve_taylor())  
    execute.grid(row=last_row+2, column=0, padx=2, pady=5)
    
  def solve_taylor(self): 
    try:
      x=symbols('x')
      f,x0,n = eval(self.entries[0].get()), float(self.entries[1].get()), float(self.entries[2].get())
      p = Taylor(f,x0,n)
      self.result.config(text=f'El polinomio de grado {n} es {p}')
    except Exception as e:
      messagebox.showinfo("Error",e)  

class CCota(AZeros):
  def __init__(self, parent, controller, orden=0):
    squares = ["f","x_","n","x0"]
    super().__init__(parent, controller, orden,squares)
    
    last_row = self.grid_size()[1] - 1
    
    self.result = tk.Label(self, text="" , width=65,wraplength=200)
    self.result.grid(row=last_row+1, column=1, padx=1, pady=1,sticky='nsew' )
    
    execute = tk.Button(self,text="Ejecutar",command=lambda:self.solve_cota())  
    execute.grid(row=last_row+2, column=0, padx=2, pady=5)
    
  def solve_cota(self): 
    try:
      x = symbols('x')
      f,x_,n,x0 = eval(self.entries[0].get()), float(self.entries[1].get()), float(self.entries[2].get()),float(self.entries[3].get())
      p = Cota_t(f,x_,n,x0)
      self.result.config(text=f'La cota es {p}')
    except Exception as e:
      messagebox.showinfo("Error",e)  
  
  