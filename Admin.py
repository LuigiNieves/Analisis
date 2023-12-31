import tkinter as tk
from tkinter import Menu
from windows.IZeros import CNewton, CBiseccion, CFalsaPosicion, CSecante
from windows.IInterpolation import CPsimple,CMinimos,CLagrange
from windows.IIntegration import CTrapeze,CTrapezePuntos,CSimpson13,CSimpson38
from windows.IDE import CEuler,CRunge
from windows.ITaylor import CCota,CTaylor,CDifferentiation


class Home(tk.Frame):
  def __init__(self,parent,controller):
    super().__init__(parent)
    self.controller =controller
    self.game_mode = tk.StringVar(self, value="normal")

    tk.Label(self, text='En este software usted tendrá la posibilidad de realizar casi cualquier problema que haya encontrado en la materia de análisis númerico, por medio del menu posicionado en la parte superior izquierda usted podra navegar por los diferentes métodos númericos, por favor haga caso omiso a las instrucciones en cada uno de los métodos para su perfecto funcionamiento, use por favor solo la variable x en minúscula para representar los símbolos en las ecuaciones, en algunos casos tendrá que usar la variable t en mínuscula para representar el tiempo. Siga las instrucciones en cada apartado del programa y este funcionará de maravilla, muchas gracias por usar nuestro software !!!', wraplength=400,justify='left').pack(expand=True, fill=tk.BOTH)


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

    for F in (Home,CNewton,CBiseccion, CFalsaPosicion, CSecante,CPsimple,CMinimos,CLagrange,CTrapeze,CTrapezePuntos,CSimpson13,CSimpson38, CEuler,CRunge,CCota,CTaylor,CDifferentiation):
        frame=F(container,self)
        self.frames[F]=frame
        frame.grid(row=0, column=0, sticky =tk.NSEW)
    self.show_home(Home)   

  def show_home(self,container):
      frame = self.frames[container]
      frame.tkraise() 
  
  def show_frame(self,container): 
    frame = self.frames[container]
    frame.tkraise()  

  def salir_ventana(self):
      self.destroy()    

  def crear_barra_menu(self):
    self.barra_menu = Menu()
    self.menu_juego = Menu( tearoff=0 )
    sub_menu_ceros = tk.Menu(self.menu_juego,tearoff=0)
    sub_menu_ceros.add_command(label="Biseccion",font=("Arial","10"),command=lambda:self.show_frame(CBiseccion))
    sub_menu_ceros.add_command(label="Falsa Posición",font=("Arial","10"),command=lambda:self.show_frame(CFalsaPosicion))
    sub_menu_ceros.add_command(label="Newton",font=("Arial","10"),command=lambda:self.show_frame(CNewton))
    sub_menu_ceros.add_command(label="Secante",font=("Arial","10"),command=lambda:self.show_frame(CSecante))

    sub_menu_curvas = tk.Menu(self.menu_juego,tearoff=0)
    sub_menu_curvas.add_command(label="Euler",font=("Arial","10"),command=lambda:self.show_frame(CEuler))
    sub_menu_curvas.add_command(label="Runge Kutta",font=("Arial","10"),command=lambda:self.show_frame(CRunge))

    sub_menu_interpolacion = tk.Menu(self.menu_juego,tearoff=0)
    sub_menu_interpolacion.add_command(label="Polinomial Simple",font=("Arial","10"),command=lambda:self.show_frame(CPsimple))
    sub_menu_interpolacion.add_command(label="Lagrange",font=("Arial","10"),command=lambda:self.show_frame(CLagrange))
    sub_menu_interpolacion.add_command(label="Minimos Cuadrados",font=("Arial","10"),command=lambda:self.show_frame(CMinimos))

    sub_menu_integration = tk.Menu(self.menu_juego,tearoff=0)
    sub_menu_integration.add_command(label="Trapecio función",font=("Arial","10"),command=lambda:self.show_frame(CTrapeze))
    sub_menu_integration.add_command(label="Trapecio datos",font=("Arial","10"),command=lambda:self.show_frame(CTrapezePuntos))
    sub_menu_integration.add_command(label="Simpson 1/3",font=("Arial","10"),command=lambda:self.show_frame(CSimpson13))
    sub_menu_integration.add_command(label="Simpson 3/8",font=("Arial","10"),command=lambda:self.show_frame(CSimpson38))

    sub_menu_taylor = tk.Menu(self.menu_juego,tearoff=0)
    sub_menu_taylor.add_command(label="Serie Taylor",font=("Arial","10"),command=lambda:self.show_frame(CTaylor))
    sub_menu_taylor.add_command(label="Cota",font=("Arial","10"),command=lambda:self.show_frame(CCota))
    sub_menu_taylor.add_command(label="Diferenciación",font=("Arial","10"),command=lambda:self.show_frame(CDifferentiation))
    
    self.menu_juego.add_cascade(label="Ceros", menu = sub_menu_ceros )  
    self.menu_juego.add_cascade(label="EDO", menu = sub_menu_curvas )  
    self.menu_juego.add_cascade(label="Interpolacion", menu = sub_menu_interpolacion)  
    self.menu_juego.add_cascade(label="Integración", menu = sub_menu_integration)  
    self.menu_juego.add_cascade(label="Series", menu = sub_menu_taylor)  

    self.menu_juego.add_command(label="Salir",font=("Arial","10"),command = self.salir_ventana)
    self.barra_menu.add_cascade(label = "Iniciar", menu = self.menu_juego ) 
    self.config(menu = self.barra_menu)