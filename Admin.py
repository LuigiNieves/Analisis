
import tkinter as tk
import tkinter
from typing import Container
from interfaz import Home,cajas,CNewton,Otros
from tkinter import Menu,Label,StringVar,ttk

class Admin(tk.Tk):

  def __init__(self, *args, **kwargs):
    super().__init__(*args,**kwargs)
    self.title("cuatro en Linea")
    container=tk.Frame(self)
    self.crear_menu=self.crear_barra_menu()
    container.pack(
        side = tk.TOP,
        fill = tk.BOTH,
        expand = True
    )
    
    # container.configure(background = style.BACKGROUND)
    container.grid_columnconfigure(0,weight=1)
    container.grid_rowconfigure(0,weight=1)

    self.frames={}
    for F in (Home,cajas,CNewton,Otros):
        frame=F(container,self)
        self.frames[F]=frame
        frame.grid(row=0, column=0, sticky =tk.NSEW)
    self.show_home(Home)   

  def show_home(self,container):
      frame = self.frames[container]
      frame.tkraise()   #las pone adelante  
  
  def show_frame(self,container): 
    frame = self.frames[container]
    frame.tkraise()   #las pone adelante    

  def salir_ventana(self):
      self.destroy()    

  def crear_barra_menu(self):
    self.barra_menu = Menu()

    self.menu_juego = Menu( tearoff=0 )
  
    self.menu_juego.add_command(label="Integracion",font=("Arial","10"),command=lambda:self.show_frame(cajas))
    # self.menu_juego.add_command(label="6X6",font=("Arial","10"))
    # self.menu_juego.add_command(label="Otra partida",font=("Arial","10"),command=lambda:self.enable())

    subMenuCeros = tk.Menu(self.menu_juego,tearoff=0)
    subMenuCeros.add_command(label="Biseccion",font=("Arial","10"),command=lambda:self.show_frame(Otros))
    subMenuCeros.add_command(label="Falsa Posición",font=("Arial","10"),command=lambda:self.show_frame(Otros))
    subMenuCeros.add_command(label="Newton",font=("Arial","10"),command=lambda:self.show_frame(CNewton))
    subMenuCeros.add_command(label="Secante",font=("Arial","10"),command=lambda:self.show_frame(Otros))

    subMenuCurvas = tk.Menu(self.menu_juego,tearoff=0)
    subMenuCurvas.add_command(label="Euler",font=("Arial","10"))
    subMenuCurvas.add_command(label="Runge Kutta",font=("Arial","10"))

    subMenuInterpolacion = tk.Menu(self.menu_juego,tearoff=0)
    subMenuInterpolacion.add_command(label="Polinomial Simple",font=("Arial","10"))
    subMenuInterpolacion.add_command(label="Lagrange",font=("Arial","10"))
    subMenuInterpolacion.add_command(label="Minimos Cuadrados",font=("Arial","10"))
    

    
    self.menu_juego.add_cascade(label="Ceros", menu = subMenuCeros )  
    self.menu_juego.add_cascade(label="Curvas", menu = subMenuCurvas )  
    self.menu_juego.add_cascade(label="Interpolacion", menu = subMenuInterpolacion)  

    self.menu_juego.add_command(label="Salir",font=("Arial","10"),command = self.salir_ventana)
    self.barra_menu.add_cascade(label = "Iniciar", menu = self.menu_juego ) 
    self.config(menu = self.barra_menu)
  