import tkinter as tk
from functions.Interpolation import *
from sympy import symbols,lambdify,exp,log
from tkinter import ttk
from PIL import Image, ImageTk


class AInterpolation(tk.Frame):
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
      label.grid(row=idx, column=0, padx=1, pady=1)
      
      entry = tk.Entry(self, width=65)
      entry.grid(row=idx, column=1, padx=1, pady=1)
    
      self.entries.append(entry)
    
  def show_result(self,grafica):    
    top = tk.Toplevel(self)
    top.title("Tabla de datos")

    imagen = Image.open('img.png')
    imagen_tk = ImageTk.PhotoImage(imagen)
    label_imagen = tk.Label(top, image=imagen_tk)
    label_imagen.pack()
    

class CMinimos(AInterpolation):
  def __init__(self, parent, controller, orden=0, cuadros=0):
    cuadros = ["xdata","ydata"]
    super().__init__(parent, controller, orden, cuadros)
    ultima_fila = self.grid_size()[1] - 1
    
    self.result = tk.Label(self, text="" , width=65, wraplength=200)
    self.result.grid(row=ultima_fila+1, column=1, padx=1, pady=1,sticky='nsew' )
    
    execute = tk.Button(self,text="Ejecutar",command=lambda:self.solve_minimos())  
    execute.grid(row=ultima_fila+2, column=0, padx=2, pady=5)
    
    xdata = [float(i) for i in self.entries[0].get().split(' ') if self.isNumeric(i)]
    ydata = [float(i) for i in self.entries[1].get().split(' ') if self.isNumeric(i)]
    
    grafica=self.graficar(xdata,ydata)
    self.show_result(grafica)
  
  def isNumeric(self,s):
    try:
        float(s)
        return True
    except ValueError:
        return False   
    
  def graficar(self,xdata,ydata):
  
    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    plt.figure(figsize=(6, 4))
    plt.plot(x, y)
    plt.title('Gráfica de ejemplo')
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    plt.grid(True)
        
    plt.savefig('img.png')
    plt.close()
   

  def solve_minimo(self): 
    try:
      xdata = [float(i) for i in self.entries[0].get().split(' ') if self.isNumeric(i)]
      ydata = [float(i) for i in self.entries[1].get().split(' ') if self.isNumeric(i)]
    
      a0,a1 = minimos_cuadrados(xdata,ydata)  
    except Exception as e:
      print(e) 

    
class CPsimple(AInterpolation):
  def __init__(self, parent, controller, orden=0, cuadros=0):
    cuadros = ["xdata","ydata"]
    super().__init__(parent, controller, orden, cuadros)
    ultima_fila = self.grid_size()[1] - 1
    
    self.result = tk.Label(self, text="" , width=65, wraplength=200)
    self.result.grid(row=ultima_fila+1, column=1, padx=1, pady=1,sticky='nsew' )
    
    execute = tk.Button(self,text="Ejecutar",command=lambda:self.solve_Psimple())  
    execute.grid(row=ultima_fila+2, column=0, padx=2, pady=5) 
    
    
    

  def isNumeric(self,s):
    try:
        float(s)
        return True
    except ValueError:
        return False  
      
  def solve_Psimple(self): 
    try:
      xdata = [float(i) for i in self.entries[0].get().split(' ') if self.isNumeric(i)]
      ydata = [float(i) for i in self.entries[1].get().split(' ') if self.isNumeric(i)]
    
      polinomioS,P = p_simple(xdata,ydata)  
      self.result.config(text=P)
    except Exception as e:
      print(e)   