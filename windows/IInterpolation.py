import tkinter as tk
from functions.Interpolation import *
from sympy import symbols,lambdify,exp,log
from tkinter import ttk
from PIL import Image, ImageTk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def isNumeric(s):
    try:
        float(s)
        return True
    except ValueError:
        return False  


class AInterpolation(tk.Frame):
  def __init__(self, parent, controller,order=0,squares=0):
    super().__init__(parent)
    self.configure(background = "blue")
    self.controller =controller  
    # self.order = order
    self.squares = squares
    self.entries =[]
    self.widget()

  def widget(self):
    for idx, label_text in enumerate(self.squares):
      label = tk.Label(self, text=label_text, width=3)
      label.grid(row=idx, column=0, padx=1, pady=1)
      entry = tk.Entry(self, width=65)
      entry.grid(row=idx, column=1, padx=1, pady=1)
      self.entries.append(entry)
    
  def show_result(self,value):    
    top = tk.Toplevel(self)
    top.title("Tabla de datos")
    # imagen = Image.open('img.png')
    # imagen_tk = ImageTk.PhotoImage(imagen)

    # label_new = tk.Label(top,text=value)
    # label_new.pack()

    # label_imagen = tk.Label(top,image=imagen_tk)
    # label_imagen.pack()
    canvas = FigureCanvasTkAgg(self.fig, master=top)
    canvas.draw()
    canvas.get_tk_widget().pack()
    

class CMinimos(AInterpolation):
  def __init__(self, parent, controller, order=0, squares=0):
    squares = ["xdata","ydata"]
    super().__init__(parent, controller, order, squares)
    last_row = self.grid_size()[1] - 1
    
    self.result = tk.Label(self, text="" , width=65, wraplength=200)
    self.result.grid(row=last_row+1, column=1, padx=1, pady=1,sticky='nsew' )
    
    execute = tk.Button(self,text="Ejecutar",command=lambda:self.solve_minimos())  
    execute.grid(row=last_row+2, column=0, padx=2, pady=5)

    # xdata = [float(i) for i in [1,2,3,4,5] if self.isNumeric(i)]
    # ydata = [float(i) for i in [9,19,82,101,200] if self.isNumeric(i)]
    
    # self.graph(xdata,ydata)
    # self.show_result()
  
   
    
  def graph(self,x,y,f):
    self.fig=plt.figure(figsize=(6, 4))
    plt.plot(x, y,'o',label='Puntos Observados')
    plt.plot(x,[f(i) for i in x],label='Minimos cuadrados')
    plt.title('Gráfica de ejemplo')
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    plt.grid()
    plt.legend()
    plt.close()


  def solve_minimos(self): 
    try:
      xdata = [float(i) for i in self.entries[0].get().split(' ') if isNumeric(i)]
      ydata = [float(i) for i in self.entries[1].get().split(' ') if isNumeric(i)]
      a0,a1,f = minimos_cuadrados(xdata,ydata) 
      self.result.config(text=f'{a0} + ({a1})*x') 
      self.graph(xdata,ydata,f)
      self.show_result(f'{a0} + ({a1})*x')
    except Exception as e:
      print(e) 

    
class CPsimple(AInterpolation):
  def __init__(self, parent, controller, order=0, squares=0):
    squares = ["xdata","ydata"]
    super().__init__(parent, controller, order, squares)
    last_row = self.grid_size()[1] - 1
    
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
      print(e)   


class CLagrange(AInterpolation):
  def __init__(self, parent, controller, order=0, squares=0):
    squares = ["xdata","ydata"]
    super().__init__(parent, controller, order, squares)
    last_row = self.grid_size()[1] - 1
    
    self.result = tk.Label(self, text="" , width=65, wraplength=200)
    self.result.grid(row=last_row+1, column=1, padx=1, pady=1,sticky='nsew' )
    
    execute = tk.Button(self,text="Ejecutar",command=lambda:self.solve_Psimple())  
    execute.grid(row=last_row+2, column=0, padx=2, pady=5) 
      
  def solve_Psimple(self): 
    try:
      xdata = [float(i) for i in self.entries[0].get().split(' ') if self.isNumeric(i)]
      ydata = [float(i) for i in self.entries[1].get().split(' ') if self.isNumeric(i)]
    
      P,f = lagrange(xdata,ydata)  
      self.result.config(text=P)
    except Exception as e:
      print(e) 