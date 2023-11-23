import tkinter as tk
from functions.DE import *
from sympy import symbols,lambdify,exp,log
from tkinter import ttk
from PIL import Image, ImageTk

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
    
  def show_result(self,grafica):    
    top = tk.Toplevel(self)
    top.title("Tabla de datos")
    imagen_tk = ImageTk.PhotoImage(grafica)
    label_imagen = tk.Label(top, image=imagen_tk)
    label_imagen.pack() 


class CEuler(DE):
  def __init__(self, parent, controller, orden=0, cuadros=0):
    cuadros = ["f","a","b","h","co"]
    super().__init__(parent, controller, orden, cuadros)
    last_row = self.grid_size()[1] - 1
    execute = tk.Button(self,text="Ejecutar",command=lambda:self.solve_euler())  
    execute.grid(row=last_row+1, column=0, padx=2, pady=5) 
    
  def graficar(self,t,P):
    # P=np.array(P)
    # plt.subplot(121)
    # plt.plot(t,P[:,0])
    # plt.grid()
    # # plt.xlim(9.4, 9.6)
    # plt.xlabel('tiempo')
    # plt.ylabel('posicion')
    # plt.subplot(122)
    # plt.plot(t,P[:,1])
    # plt.xlabel('tiempo')
    # plt.xlabel('posicion')
    # plt.grid(True)
    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    plt.figure(figsize=(6, 4))
    plt.plot(x, y)
    plt.title('Gráfica de ejemplo')
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    plt.grid(True)
        
    plt.savefig('img')
    plt.close()
    
    imagen = Image.open('imgn')
    imagen_tk = ImageTk.PhotoImage(imagen)

    return imagen
    
  def solve_euler(self): 
    try:
      x=symbols('x')
      tiempo=matriz=0
      # tiempo,matriz = Euler(eval(self.entries[0].get()), float(self.entries[1].get()), float(self.entries[2].get())\
      #   , float(self.entries[3].get()), float(self.entries[4].get()))
      grafica = self.graficar(tiempo,matriz)
      self.show_result(grafica)  
      # last_row = self.grid_size()[1] - 1
    except Exception as e:
      print(e) 
    
  
      
    