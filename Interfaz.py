from tkinter import *
#Nueva ventana
ventana = Tk()

#Dimension de ventana
ventana.geometry("800x600")

#Titulo de la ventana
ventana.title("Generador de rubricas")

#Titulo del programa
titulo = Label(text="Sistema de secuencias")
titulo.pack()

#Asignatura
asignaturaLabel = Label(text="Asignatura")
asignaturaLabel.pack()
asignaturaListbox = Listbox()
asignaturaListbox.pack()
for item in ["Fisica", "Matematicas", "Ciencias", "Diseño"]:
    asignaturaListbox.insert(END, item)
#Bloque
bloqueLabel = Label(text="Bloque")
bloqueLabel.pack()
bloqueListbox = Listbox(selectmode=BROWSE)
bloqueListbox.pack()
for item in ["1", "2", "3"]:
    bloqueListbox.insert(END, item)
#Semestre
semestreLabel = Label(text="Semestre")
semestreLabel.pack()
semestreListbox = Listbox(selectmode=BROWSE)
semestreListbox.pack()
for item in ["1", "2", "3"]:
    semestreListbox.insert(END, item)
#Docente
docenteLabel = Label(text="Nombre Docente")
docenteLabel.pack()
#Boton
button = Button(text="Iniciar rubrica")
button.pack()


#Para los usuarios de windows linux no lo necesita
ventana.mainloop()
