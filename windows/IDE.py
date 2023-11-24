import tkinter as tk
from functions.DE import *
from sympy import symbols,lambdify,exp,log,lambdify
from tkinter import ttk
from PIL import Image, ImageTk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class DE(tk.Frame):
  def __init__(self, parent, controller,orden=0,cuadros=0):
    super().__init__(parent)
    self.configure(background = "blue")
    self.controller =controller  
    # self.orden = orden
    self.cuadros =  cuadros
    self.entries =[]
    self.widget()
    
  def widget(self):
    for idx, label_text in enumerate(self.cuadros):
      label = tk.Label(self, text=label_text, width=3)
      label.grid(row=idx, column=0, padx=0, pady=0)
      
      entry = tk.Entry(self, width=45)
      entry.grid(row=idx, column=1, padx=0, pady=0)
    
      self.entries.append(entry)

  def graph(self,x,y):
    fig = plt.figure(figsize=(6, 4))
    plt.plot(x, y,'o')
    plt.title('Gráfica de ejemplo')
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    plt.grid(True)
    plt.close()
    return fig
    
  def show_result(self,graph):    
    top = tk.Toplevel(self)
    top.title("Tabla de datos")
    canvas = FigureCanvasTkAgg(graph, master=top)
    canvas.draw()
    canvas.get_tk_widget().pack()


class CEuler(DE):
  def __init__(self, parent, controller, orden=0, cuadros=0):
    cuadros = ["f","a","b","h","co"]
    super().__init__(parent, controller, orden, cuadros)
    last_row = self.grid_size()[1] - 1
    execute = tk.Button(self,text="Ejecutar",command=lambda:self.solve_euler())  
    execute.grid(row=last_row+1, column=0, padx=2, pady=5) 
    
    
  def solve_euler(self): 
    try:
      x,t=symbols('x t')
      f,a,b,h,co = eval(self.entries[0].get()), float(self.entries[1].get()), float(self.entries[2].get()),float(self.entries[3].get()), float(self.entries[4].get())
      f = lambdify([t,x],f)
      t,points = Euler(f,a,b,h,co)
      grafica = self.graph(t,points)
      self.show_result(grafica)  
    except Exception as e:
      print(e) 


class CRunge(DE):
  def __init__(self, parent, controller, orden=0, cuadros=0):
    cuadros = ["f","a","b","h","co"]
    super().__init__(parent, controller, orden, cuadros)
    last_row = self.grid_size()[1] - 1
    execute = tk.Button(self,text="Ejecutar",command=lambda:self.solve_runge())  
    execute.grid(row=last_row+1, column=0, padx=2, pady=5) 
    
  def solve_runge(self): 
    try:
      x,t=symbols('x t')
      f,a,b,h,co = eval(self.entries[0].get()), float(self.entries[1].get()), float(self.entries[2].get()),float(self.entries[3].get()), float(self.entries[4].get())
      f = lambdify([t,x],f)
      t,points = runge4(f,a,b,h,co)
      grafica = self.graph(t,points)
      self.show_result(grafica)  
    except Exception as e:
      print(e) 
    
  
      
    