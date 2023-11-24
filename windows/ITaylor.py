import tkinter as tk
from functions.Interpolation import *
from sympy import symbols,lambdify,exp,log,sin,cos,tan,cot,sec,csc,pi
from tkinter import ttk
from functions.Taylor import Taylor,Cota_t,diferenciacion
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

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
    
    tree.tag_configure('oddrow', background='#F0F0F0')  # Color para filas impares
    tree.tag_configure('evenrow', background='white')  # Color para filas pares
    for i, item in enumerate(tree.get_children()):
      if i % 2 == 0:
          tree.item(item, tags=('evenrow',))
      else:
          tree.item(item, tags=('oddrow',))  

    tree.pack()   

class CTaylor(AZeros):
  def __init__(self, parent, controller):
    squares = ["f","x0","n"]
    super().__init__(parent, controller,squares)
    
    last_row = self.grid_size()[1] - 1

    self.create_instructions('Taylor')
    
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
  def __init__(self, parent, controller):
    squares = ["f","x_","n","x0"]
    super().__init__(parent, controller,squares)
    
    last_row = self.grid_size()[1] - 1

    self.create_instructions('Cota')

    
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

class CDifferentiation(AZeros):
  def __init__(self, parent, controller):
    squares = ["a","b","h",'x0','k']
    super().__init__(parent, controller,squares)

    last_row = self.grid_size()[1] - 1

    self.create_instructions('Diferenciación')

    self.result = tk.Label(self, text="" , width=65,wraplength=200)
    self.result.grid(row=last_row+1, column=1, padx=1, pady=1,sticky='nsew' )
    
    execute = tk.Button(self,text="Ejecutar",command=lambda:self.solve_taylor())  
    execute.grid(row=last_row+2, column=0, padx=2, pady=5)

  def graph(self,graph):    
    top = tk.Toplevel(self)
    top.title("Tabla de datos")
    canvas = FigureCanvasTkAgg(graph, master=top)
    canvas.draw()
    canvas.get_tk_widget().pack()
    
  def solve_taylor(self): 
    try:
      x=symbols('x')
      a,b,h,x0,k = float(self.entries[0].get()),float(self.entries[1].get()),float(self.entries[2].get()),float(self.entries[3].get()),eval(self.entries[4].get())
      k = lambdify(x,k)
      t,points = diferenciacion([a,b],h,x0,k )
      self.result.config(text=f'La aproximación final es de {points[-1]}')
      fig=plt.figure(figsize=(6, 4))
      plt.plot(t, points,label='Diferenciacion')
      plt.title('Gráfica de diferenciación')
      plt.xlabel('X')
      plt.ylabel('Y')
      plt.grid()
      plt.legend()
      plt.close()
      self.graph(fig)

    except Exception as e:
      messagebox.showinfo("Error",e)  
  
  