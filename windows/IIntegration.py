import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from functions.Integration import trapecio
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt


class AIntegration(tk.Frame):
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


class CTrapeze(AIntegration):
  def __init__(self, parent, controller, order=0, squares=0):
    squares = ["f","a","b","n"]
    super().__init__(parent, controller, order, squares)
    last_row = self.grid_size()[1] - 1
    
    self.result = tk.Label(self, text="" , width=65, wraplength=200)
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
      print(e)
