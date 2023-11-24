import tkinter as tk
from functions.Interpolation import *
from sympy import exp,log,sin,cos,tan,cot,sec,csc,pi
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import messagebox


def isNumeric(s):
    try:
        float(s)
        return True
    except ValueError:
        return False  


class AInterpolation(tk.Frame):
  def __init__(self, parent, controller,squares=0):
    super().__init__(parent)
    self.configure(background = "alice blue")
    self.controller =controller  
    self.squares = squares
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
    

class CMinimos(AInterpolation):
  def __init__(self, parent, controller, squares=0):
    squares = ["xdata","ydata"]
    super().__init__(parent, controller,  squares)
    last_row = self.grid_size()[1] - 1

    self.create_instructions('Mínimos Cuadrados')
    
    self.result = tk.Label(self, text="" , width=55, wraplength=200)
    self.result.grid(row=last_row+1, column=1, padx=1, pady=1,sticky='nsew' )
    
    execute_graph = tk.Button(self,text="Modelos",command=lambda:self.graph_9())  
    execute_graph.grid(row=last_row+2, column=0, padx=2, pady=5)
    
    execute = tk.Button(self,text="Ejecutar",command=lambda:self.solve_minimos())  
    execute.grid(row=last_row+3, column=0, padx=2, pady=5)
    

  def graph_9(self):
    try:
      xdata = [float(i) for i in self.entries[0].get().split(' ') if isNumeric(i)]
      ydata = [float(i) for i in self.entries[1].get().split(' ') if isNumeric(i)]
      graph = graficas9(xdata,ydata)
      self.show_result(graph)
    except Exception as e:
      messagebox.showinfo("Error",e)    


  def graph(self,x,y,f):
    fig=plt.figure(figsize=(6, 4))
    plt.plot(x, y,'o',label='Puntos Observados')
    plt.plot(x,[f(i) for i in x],label='Mínimos cuadrados')
    plt.title('Gráfica de mínimos cuadrados')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid()
    plt.legend()
    plt.close()
    return fig

  def solve_minimos(self): 
    try:
      xdata = [float(i) for i in self.entries[0].get().split(' ') if isNumeric(i)]
      ydata = [float(i) for i in self.entries[1].get().split(' ') if isNumeric(i)]
      a0,a1,f = minimos_cuadrados(xdata,ydata) 
      
      self.result.config(text=f'{a0} + ({a1})*x') 
      graph = self.graph(xdata,ydata,f)
      self.show_result(graph)
    except Exception as e:
      messagebox.showinfo("Error",e)   

    
class CPsimple(AInterpolation):
  def __init__(self, parent, controller,  squares=0):
    squares = ["xdata","ydata"]
    super().__init__(parent, controller,  squares)
    last_row = self.grid_size()[1] - 1

    self.create_instructions('Polinomial Simple')

    
    self.result = tk.Label(self, text="" , width=65, wraplength=200)
    self.result.grid(row=last_row+1, column=1, padx=1, pady=1,sticky='nsew' )
    
    execute = tk.Button(self,text="Ejecutar",command=lambda:self.solve_Psimple())  
    execute.grid(row=last_row+2, column=0, padx=2, pady=5) 
    
  def solve_Psimple(self): 
    try:
      xdata = [float(i) for i in self.entries[0].get().split(' ') if isNumeric(i)]
      ydata = [float(i) for i in self.entries[1].get().split(' ') if isNumeric(i)]
      P,f = p_simple(xdata,ydata)  
      self.result.config(text=P)
    except Exception as e:
      messagebox.showinfo("Error",e)  


class CLagrange(AInterpolation):
  def __init__(self, parent, controller,  squares=0):
    squares = ["xdata","ydata"]
    super().__init__(parent, controller, squares)
    last_row = self.grid_size()[1] - 1

    self.create_instructions('Lagrange')

    self.result = tk.Label(self, text="" , width=65, wraplength=200)
    self.result.grid(row=last_row+1, column=1, padx=1, pady=1,sticky='nsew' )
    
    execute = tk.Button(self,text="Ejecutar",command=lambda:self.solve_lagrange())  
    execute.grid(row=last_row+2, column=0, padx=2, pady=5) 
      
  def solve_lagrange(self): 
    try:
      xdata = [float(i) for i in self.entries[0].get().split(' ') if isNumeric(i)]
      ydata = [float(i) for i in self.entries[1].get().split(' ') if isNumeric(i)]
      P,f = lagrange(xdata,ydata)  
      self.result.config(text=P)
    except Exception as e:
      messagebox.showinfo("Error",e)   