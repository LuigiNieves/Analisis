import tkinter as tk
from functions.DE import *
from sympy import symbols,lambdify,exp,log,sin,cos,tan,cot,sec,csc,pi
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import messagebox
import matplotlib.pyplot as plt


class DE(tk.Frame):
  def __init__(self, parent, controller,squares=0):
    super().__init__(parent)
    self.configure(background = "alice blue")
    self.controller =controller  
    self.squares =  squares
    self.entries =[]
    self.widget()

  
  def create_instructions(self,text):
    tk.Label(self,text=f'{text}, puede utilizar las siguientes nomenclaturas (exp,log,sin,cos,tan,cot,sec,csc,pi), utilice solo x (mínuscula) como variable, recuerde las reglas de los métodos, solo utilice de primer grado', wraplength=700,justify='left').grid(row=0, column=0, padx=1, pady=1, sticky='ew',columnspan=4)
    
  def widget(self):
    for idx, label_text in enumerate(self.squares):
      label = tk.Label(self, text=label_text, width=3,)
      label.grid(row=idx+1, column=0, padx=1, pady=1, sticky='ew')
      entry = tk.Entry(self, width=45)
      entry.grid(row=idx+1, column=1, padx=1, pady=1, sticky='w')
      self.entries.append(entry)

  def graph(self,x,y):
    fig = plt.figure(figsize=(6, 4))
    plt.plot(x, y,'o')
    plt.title('Gráfica')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid()
    plt.close()
    return fig
    
  def show_result(self,graph):    
    top = tk.Toplevel(self)
    top.title("Tabla de datos")
    canvas = FigureCanvasTkAgg(graph, master=top)
    canvas.draw()
    canvas.get_tk_widget().pack()


class CEuler(DE):
  def __init__(self, parent, controller, squares=0):
    squares = ["f","a","b","h","co"]
    super().__init__(parent, controller, squares)
    last_row = self.grid_size()[1] - 1
    execute = tk.Button(self,text="Ejecutar",command=lambda:self.solve_euler())  
    execute.grid(row=last_row+1, column=0, padx=2, pady=5) 

    self.create_instructions('Euler')
    
    
  def solve_euler(self): 
    try:
      x,t=symbols('x t')
      f,a,b,h,co = eval(self.entries[0].get()), float(self.entries[1].get()), float(self.entries[2].get()),float(self.entries[3].get()), float(self.entries[4].get())
      f = lambdify([t,x],f)
      t,points = Euler(f,a,b,h,co)
      grafica = self.graph(t,points)
      self.show_result(grafica)  
    except Exception as e:
      messagebox.showinfo("Error",e)  


class CRunge(DE):
  def __init__(self, parent, controller, squares=0):
    squares = ["f","a","b","h","co"]
    super().__init__(parent, controller, squares)
    last_row = self.grid_size()[1] - 1
    execute = tk.Button(self,text="Ejecutar",command=lambda:self.solve_runge())  
    execute.grid(row=last_row+1, column=0, padx=2, pady=5) 

    self.create_instructions('Runge Kutta')

    
  def solve_runge(self): 
    try:
      x,t=symbols('x t')
      f,a,b,h,co = eval(self.entries[0].get()), float(self.entries[1].get()), float(self.entries[2].get()),float(self.entries[3].get()), float(self.entries[4].get())
      f = lambdify([t,x],f)
      t,points = runge4(f,a,b,h,co)
      grafica = self.graph(t,points)
      self.show_result(grafica)  
    except Exception as e:
      messagebox.showinfo("Error",e)  
    
  
      
    