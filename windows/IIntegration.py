import tkinter as tk


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


class CTrapeze(AIntegration):
  def __init__(self, parent, controller, order=0, squares=0):
    squares = ["f","a","b","n"]
    super().__init__(parent, controller, order, squares)
    last_row = self.grid_size()[1] - 1
    
    self.result = tk.Label(self, text="" , width=65, wraplength=200)
    self.result.grid(row=last_row+1, column=1, padx=1, pady=1,sticky='nsew' )
    
    execute = tk.Button(self,text="Ejecutar",command=lambda:self.solve_minimos())  
    execute.grid(row=last_row+2, column=0, padx=2, pady=5)
