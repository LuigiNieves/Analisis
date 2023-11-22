import tkinter as tk
from windows.IZeros import Home, CNewton, CBiseccion, CFalsaPosicion, CSecante
from tkinter import Menu

class Admin(tk.Tk):
  def __init__(self, *args, **kwargs):
    super().__init__(*args,**kwargs)
    self.title("Analisis Númerico Proyecto Final")
    container=tk.Frame(self)
    self.crear_menu=self.crear_barra_menu()
    container.pack(
        side = tk.TOP,
        fill = tk.BOTH,
        expand = True
    )
    container.grid_columnconfigure(0,weight=1)
    container.grid_rowconfigure(0,weight=1)

    self.frames={}
    for F in (Home,CNewton,CBiseccion, CFalsaPosicion, CSecante):
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
    self.menu_juego.add_command(label="Integracion",font=("Arial","10"),command=lambda:self.show_frame(CBiseccion))
    sub_menu_ceros = tk.Menu(self.menu_juego,tearoff=0)
    sub_menu_ceros.add_command(label="Biseccion",font=("Arial","10"),command=lambda:self.show_frame(CBiseccion))
    sub_menu_ceros.add_command(label="Falsa Posición",font=("Arial","10"),command=lambda:self.show_frame(CFalsaPosicion))
    sub_menu_ceros.add_command(label="Newton",font=("Arial","10"),command=lambda:self.show_frame(CNewton))
    sub_menu_ceros.add_command(label="Secante",font=("Arial","10"),command=lambda:self.show_frame(CSecante))

    sub_menu_curvas = tk.Menu(self.menu_juego,tearoff=0)
    sub_menu_curvas.add_command(label="Euler",font=("Arial","10"))
    sub_menu_curvas.add_command(label="Runge Kutta",font=("Arial","10"))

    sub_menu_interpolacion = tk.Menu(self.menu_juego,tearoff=0)
    sub_menu_interpolacion.add_command(label="Polinomial Simple",font=("Arial","10"))
    sub_menu_interpolacion.add_command(label="Lagrange",font=("Arial","10"))
    sub_menu_interpolacion.add_command(label="Minimos Cuadrados",font=("Arial","10"))
    
    self.menu_juego.add_cascade(label="Ceros", menu = sub_menu_ceros )  
    self.menu_juego.add_cascade(label="Curvas", menu = sub_menu_curvas )  
    self.menu_juego.add_cascade(label="Interpolacion", menu = sub_menu_interpolacion)  

    self.menu_juego.add_command(label="Salir",font=("Arial","10"),command = self.salir_ventana)
    self.barra_menu.add_cascade(label = "Iniciar", menu = self.menu_juego ) 
    self.config(menu = self.barra_menu)
  