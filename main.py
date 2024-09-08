from tkinter import Text, Tk, Button, Entry, Label, font

# Configuración ventana principal
root = Tk()
root.title("Calculadora POO")
root.resizable(False, False)
root.geometry("410x300")


# Configuración pantalla de salida 
pantalla = Entry(root, width=40, bg="black", fg="white", borderwidth=0, 
                 font=("arial", 18, "bold"))
pantalla.grid(row=0, column=0, columnspan=10, padx=1, pady=1)
label = Label(pantalla, width=40, height=2, bg="black", fg="white", borderwidth=0, font=('Arial', 13))
label.grid(column=0, row=0)

#Funciones para los eventos
def presionarBoton_1():
  contenido = pantalla.get()
  pantalla.insert(len(contenido), "1")
  label.config(text=pantalla.get())
def presionarBoton_2():
  contenido = pantalla.get()
  pantalla.insert(len(contenido), "2")
  label.config(text=pantalla.get())
def presionarBoton_3():
  contenido = pantalla.get()
  pantalla.insert(len(contenido), "3")
  label.config(text=pantalla.get())
def presionarBoton_4():
  contenido = pantalla.get()
  pantalla.insert(len(contenido), "4")
  label.config(text=pantalla.get())
def presionarBoton_5():
  contenido = pantalla.get()
  pantalla.insert(len(contenido), "5")
  label.config(text=pantalla.get())
def presionarBoton_6():
  contenido = pantalla.get()
  pantalla.insert(len(contenido), "6")
  label.config(text=pantalla.get())
def presionarBoton_7():
  contenido = pantalla.get()
  pantalla.insert(len(contenido), "7")
  label.config(text=pantalla.get())
def presionarBoton_8():
  contenido = pantalla.get()
  pantalla.insert(len(contenido), "8")
  label.config(text=pantalla.get())
def presionarBoton_9():
  contenido = pantalla.get()
  pantalla.insert(len(contenido), "9")
  label.config(text=pantalla.get())
def presionarBoton_0():
  contenido = pantalla.get()
  pantalla.insert(len(contenido), "0")  
  label.config(text=pantalla.get())
def presionarBoton_punto():
  contenido = pantalla.get()
  pantalla.insert(len(contenido), ".")
  label.config(text=pantalla.get())
def presionarBoton_mas():
  contenido = pantalla.get()
  pantalla.insert(len(contenido), "+")
  label.config(text=pantalla.get())
def presionarBoton_menos():
  contenido = pantalla.get()
  pantalla.insert(len(contenido), "-")
  label.config(text=pantalla.get())
def presionarBoton_multi():
  contenido = pantalla.get()
  pantalla.insert(len(contenido), "*")
  label.config(text=pantalla.get())
def presionarBoton_div():
  contenido = pantalla.get()
  pantalla.insert(len(contenido), "/")
  label.config(text=pantalla.get())

def hacerOperacion():
  primerNumero = 0
  segundoNumero = 0
  tamaño = len(pantalla.get())
  if (pantalla.get().find("+") != -1):
    primerNumero = pantalla.get().split("+")[0]
    segundoNumero = pantalla.get().split("+")[1]
    pantalla.delete(0, tamaño)
    pantalla.insert(0, str(float(primerNumero) + float(segundoNumero)))
    label.config(text=pantalla.get())
  if (pantalla.get().find("-") != -1):
    primerNumero = pantalla.get().split("-")[0]
    segundoNumero = pantalla.get().split("-")[1]
    pantalla.delete(0, tamaño)
    pantalla.insert(0, str(float(primerNumero) - float(segundoNumero)))
    label.config(text=pantalla.get())
  if (pantalla.get().find("*") != -1):
    primerNumero = pantalla.get().split("*")[0]
    segundoNumero = pantalla.get().split("*")[1]
    pantalla.delete(0, tamaño)
    pantalla.insert(0, str(float(primerNumero) * float(segundoNumero)))
    label.config(text=pantalla.get())
  if (pantalla.get().find("/") != -1):
    primerNumero = pantalla.get().split("/")[0]
    segundoNumero = pantalla.get().split("/")[1]
    pantalla.delete(0, tamaño)
    if int(segundoNumero != 0):
      pantalla.insert(0, str(float(primerNumero) / float(segundoNumero)))
      label.config(text=pantalla.get())
  


# Configuración botones
boton_1 = Button(root, text="1", width=9, height=3, bg="white", fg="red",command=presionarBoton_1, borderwidth=0, cursor="hand2").grid(row=1, column=0, padx=1, pady=0)
boton_2 = Button(root, text="2", width=9, height=3, bg="white", fg="red",command=presionarBoton_2, borderwidth=0, cursor="hand2").grid(row=1, column=1, padx=0, pady=1)
boton_3 = Button(root, text="3", width=9, height=3, bg="white", fg="red",command=presionarBoton_3, borderwidth=0, cursor="hand2").grid(row=1, column=2, padx=1, pady=1)
boton_4 = Button(root, text="4", width=9, height=3, bg="white", fg="red",command=presionarBoton_4, borderwidth=0, cursor="hand2").grid(row=2, column=0, padx=1, pady=1)
boton_5 = Button(root, text="5", width=9, height=3, bg="white", fg="red",command=presionarBoton_5, borderwidth=0, cursor="hand2").grid(row=2, column=1, padx=1, pady=1)
boton_6 = Button(root, text="6", width=9, height=3, bg="white", fg="red",command=presionarBoton_6, borderwidth=0, cursor="hand2").grid(row=2, column=2, padx=1, pady=1)
boton_7 = Button(root, text="7", width=9, height=3, bg="white", fg="red",command=presionarBoton_7, borderwidth=0, cursor="hand2").grid(row=3, column=0, padx=1, pady=1)
boton_8 = Button(root, text="8", width=9, height=3, bg="white", fg="red",command=presionarBoton_8, borderwidth=0, cursor="hand2").grid(row=3, column=1, padx=1, pady=1)
boton_9 = Button(root, text="9", width=9, height=3, bg="white", fg="red",command=presionarBoton_9, borderwidth=0, cursor="hand2").grid(row=3, column=2, padx=1, pady=1)
boton_igual = Button(root, text="=", width=20, height=3, bg="red", fg="white", borderwidth=0,command=hacerOperacion, cursor=" hand2").grid(row=4, column=0, columnspan=2, padx=1, pady=1)
boton_punto = Button(root, text=".", width=9, height=3, bg="spring green", fg="black", cursor="hand2",command=presionarBoton_punto,borderwidth=0).grid(row=4, column=2, padx=1, pady=1)
boton_mas = Button(root, text="+", width=9, height=3, bg="deep sky blue", fg="black",command=presionarBoton_mas, borderwidth=0, cursor="hand2").grid(row=1, column=3, padx=1, pady=1)
boton_menos = Button(root, text="-", width=9, height=3, bg="deep sky blue",command=presionarBoton_menos, fg="black", borderwidth=0, cursor="hand2").grid(row=2, column=3, padx=1, pady=1)
boton_multiplicacion = Button(root, text="*",  width=9, height=3, bg="deep sky blue",command=presionarBoton_multi, fg="black", borderwidth=0, cursor="hand2").grid(row=3, column=3, padx=1, pady=1)
boton_division = Button(root, text="/", width=9, height=3, bg="deep sky blue",command=presionarBoton_div, fg="black", borderwidth=0, cursor="hand2").grid(row=4, column=3, padx=1, pady=1)



root.mainloop()