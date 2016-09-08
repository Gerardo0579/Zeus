from tkinter import *
#Nueva ventana
ventana = Tk()

#Dimension de ventana
ventana.geometry("800x600")

#Titulo de la ventana
ventana.title("Rubricas")

label = Label(text="Sistema de secuencias").grid(row=0,column=1)

label = Label(text="Asignatura").grid(row=1,column=0)
label = Label(text="Bloque").grid(row=1,column=3)

label = Label(text="Semestre").grid(row=2,column=0)
label = Label(text="Nombre del docente").grid(row=2,column=3)

button = Button(text="Iniciar rubrica").grid(row=3,column=3)


#Para los usuarios de windows linux no lo necesita
ventana.mainloop()
