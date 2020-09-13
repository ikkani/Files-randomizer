import os
import random
import shutil
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
from tkinter import *


rutaCarpetaOrigen = ""
rutaCarpetaDestino = ""

window = Tk()
 
window.title("Files randomizer")
window.geometry('450x250')
window.resizable(False, False)


def clickarCarpetaOrigen():
	global rutaCarpetaOrigen
	window.filename = filedialog.askdirectory(initialdir=("."))
	rutaCarpetaOrigen = window.filename
	global l1
	mostrarCarpetaOrigen = rutaCarpetaOrigen.split("/")
	if len(mostrarCarpetaOrigen) > 1:
		mostrarCarpetaOrigen = mostrarCarpetaOrigen[-1]
	try:
		l1["text"] = "Carpeta origen: " + ".../" + mostrarCarpetaOrigen
	except:
		l1["text"] = "Carpeta origen"

def clickarCarpetaDestino():
	global rutaCarpetaDestino
	window.filename = filedialog.askdirectory(initialdir=("."))
	rutaCarpetaDestino = window.filename
	global l2
	mostrarCarpetaDestino = rutaCarpetaDestino.split("/")
	if len(mostrarCarpetaDestino) > 1:
		mostrarCarpetaDestino = mostrarCarpetaDestino[-1]
	try:
		l2["text"] = "Carpeta destino: " + ".../" + mostrarCarpetaDestino
	except:
		l1["text"] = "Carpeta destino"


def clickarStart():
	global rutaCarpetaOrigen
	global rutaCarpetaDestino
	confirmacion = messagebox.askokcancel("Renombrador","Renombrar archivos?")
	if confirmacion:
		if rutaCarpetaOrigen == "":
			messagebox.showerror("Error", "Carpeta origen no seleccionada")
		elif rutaCarpetaDestino == "":
			messagebox.showerror("Error", "Carpeta destino no seleccionada")
		elif rutaCarpetaDestino == rutaCarpetaOrigen:
			messagebox.showerror("Error", "La carpeta origen no puede ser la misma que la carpeta destino")
		else:
			carpeta = os.listdir(rutaCarpetaOrigen)
			nArchivos = len(carpeta)
			vectorNumeros = list(range(1,nArchivos+1))
			random.shuffle(vectorNumeros)
			global txtPre
			global txtPos
			i = 0

			for archivo in carpeta:
	 			nuevoNombre = str(vectorNumeros[i])
	 			i += 1
	 			shutil.copy2(rutaCarpetaOrigen + "/" + archivo, rutaCarpetaDestino + "/" + txtPre.get() + nuevoNombre + txtPos.get())



btnOrg = Button(window, text="Seleccionar carpeta de origen",command=clickarCarpetaOrigen, bd = 3, relief = "ridge")
btnOrg.grid(column = 0, row = 0, padx = 15, pady = 10)


btnDst = Button(window, text="Seleccionar carpeta de destino",command=clickarCarpetaDestino, bd = 3, relief = "ridge")
btnDst.grid(column = 1, row = 0)

l1 = ttk.Label(text="Carpeta origen: ")
l1.grid(column = 0, row = 2, pady = 7)

l2 = ttk.Label(text="Carpeta destino: ")
l2.grid(column = 0, row = 3, pady = 7)

(ttk.Label(text = "Prefijo")).grid(column = 0, row = 4)
txtPre = Entry(window,width=10)
txtPre.grid(column = 1, row = 4, sticky = "we", pady = 7)

(ttk.Label(text = "Posfijo")).grid(column = 0, row = 5)
txtPos = Entry(window,width=10)
txtPos.grid(column = 1, row = 5, sticky = "we", pady = 7)

btnStart = Button(window, text="Empezar",command=clickarStart, width = 7, bd = 3, relief= "ridge")
btnStart.grid(column = 0, row = 6, pady = 7, padx = 20)

window.mainloop()




