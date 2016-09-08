from tkinter import *
from tkinter import ttk
from Fachada.Asignatura import Asignatura
#Nueva ventana
ventana = Tk()

#Dimension de ventana
cuadro = Frame(ventana)
cuadro.grid(row=0, column=0, padx=(10), pady=(10))
ventana.geometry("550x160")

#Titulo de la ventana
ventana.title("Rubricas")
#Subtitulo
subTitulo = Label(cuadro,text="Sistema de secuencias").grid(row=0,column=1)
#Asignatura
asignatura = Asignatura()
asignaturaLabel = Label(cuadro,text="Asignatura").grid(row=1,column=0)
asignaturaBox = ttk.Combobox(cuadro,asignatura.listarAsignaturas()).grid(row=2,column=0)
#Bloque
bloqueLabel = Label(cuadro,text="Bloque").grid(row=1,column=3)
bloqueBox = ttk.Combobox(cuadro).grid(row=2,column=3)
#Semestre
semestreLabel = Label(cuadro,text="Semestre").grid(row=3,column=0,padx=(0),pady=(10,0))
semestreBox = ttk.Combobox(cuadro).grid(row=4,column=0)
#Docente
docenteLabel = Label(cuadro,text="Nombre del docente").grid(row=3,column=3,padx=(0),pady=(10,0))
docenteBox = ttk.Combobox(cuadro).grid(row=4,column=3)
#Rubrica
iniciarBoton = Button(cuadro,text="Iniciar rubrica").grid(row=5,column=5,padx=(35),pady=(5,0))


#Para los usuarios de windows linux no lo necesita
ventana.mainloop()
