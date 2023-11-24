from Admin import Admin

if __name__=="__main__": 
  ventana = Admin()
  ventana.geometry("700x700")
  ventana.resizable(False, False)
  ventana.title("Analisis númerico")
  ventana.iconbitmap("OIP.ico")
  ventana.config(background='alice blue')
  ventana.mainloop()