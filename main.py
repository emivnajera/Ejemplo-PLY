import tkinter as tk
from tkinter import scrolledtext as st
import sys
from tkinter import filedialog as fd
from tkinter import  messagebox as mb
import os
import grammar



archivo = ""
entra = ""

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.agregar_menu()

        self.scrolledtext1=st.ScrolledText(self.ventana1, width=70, height=30)
        self.scrolledtext1.pack(side=tk.LEFT, padx=75,pady=50)

        self.scrolledtext2= st.ScrolledText(self.ventana1, width=100, height=30)
        self.scrolledtext2.config(bg="black", fg="white")
        self.scrolledtext2.pack(side=tk.RIGHT, padx=200, pady=50)

        self.ventana1.geometry("1080x1080")
        self.ventana1.config(bg="gray")
        self.ventana1.title("JPR Editor")
        self.ventana1.iconbitmap("escudo10.ico")

        self.titulo=tk.Label(self.ventana1,text="JPR Editor")
        self.titulo.config(bg="gray", font=('Arial',15))
        self.titulo.pack()

        self.widget = tk.Label(self.ventana1, text='[FILA,COLUMNA]')
        self.widget.config( bg="gray",font=("Arial", 8))
        self.widget.place(x=150, y=100)

        self.lentrada = tk.Label(self.ventana1, text='Archivo de Entrada')
        self.lentrada.config( bg="gray",font=("Arial", 8))
        self.lentrada.place(x=70, y=130)

        self.widgett = tk.Label(self.ventana1, text='0')
        self.widgett.config(bg="gray", font=("Arial", 15))
        self.widgett.place(x=775,y=100)

        self.boton = tk.Button(self.ventana1,text="Next")
        self.boton.place(x=765,y=130)

        self.botone = tk.Button(self.ventana1, text="Ejecutar", command=self.ejecutar)
        self.botone.place(x=130, y=800)


        self.ventana1.mainloop()


    def agregar_menu(self):
        global archivo
        menubar1 = tk.Menu(self.ventana1)
        self.ventana1.config(menu=menubar1)
        opciones1 = tk.Menu(menubar1, tearoff=0)
        opciones1.add_command(label="Abrir Archivo", command=self.abrir)
        opciones1.add_command(label="Guardar Archivo Como", command=self.guardarcomo)
        opciones1.add_command(label="Guardar Archivo", command=self.guardarArchivo)
        opciones1.add_command(label="Reporte de Errores", command=self.reporteError)
        opciones1.add_command(label="Reporte de Tabla", command=self.reporteTabla)
        opciones1.add_separator()
        opciones1.add_command(label="Salir", command=self.salir)
        menubar1.add_cascade(label="Archivo", menu=opciones1)

    def ejecutar(self):
        self.scrolledtext2.delete("1.0",tk.END)
        grammar.run(self.scrolledtext1.get("1.0",tk.END), self.scrolledtext2)
        self.scrolledtext2.insert(tk.END,grammar.consola)
        errr = open("Errores.html","w")
        errr.write(grammar.reporterror)
        errr.close()
        simbb = open("TablaDeSimbolos.html","w")
        simbb.write(grammar.reporttabla)
        simbb.close()

    def salir(self):
        sys.exit(0)


    def reporteError(self):
        os.startfile("Errores.html")

    def reporteTabla(self):
        os.startfile("TablaDeSimbolos.html")

    def guardarcomo(self):
        global archivo
        nombrearch=fd.asksaveasfilename(initialdir = "/",title = "Guardar como",filetypes = (("txt files","*.jpr"),("todos los archivos","*.*")))
        archivo = nombrearch
        if nombrearch!='':
            archi1=open(nombrearch, "w", encoding="utf-8")
            archi1.write(self.scrolledtext1.get("1.0", tk.END), self.scrolledtext2)
            archi1.close()
            mb.showinfo("Información", "Los datos fueron guardados en el archivo.")

    def guardarArchivo(self):  # GUARDAR
        global archivo
        if archivo == "":
            self.guardarcomo()
        else:
            guardarc = open(archivo, "w")
            conte = self.scrolledtext1.get("1.0", tk.END)
            guardarc.write(conte, encoding="utf-8")
            guardarc.close()


    def abrir(self):
        global archivo
        nombre_arc = fd.askopenfilename(initialdir="D:\OneDrive",title="Seleccione Archivo de Entrada",filetypes=(("text files","*.jpr"),("todos los archivos","*.*")))
        archivo = nombre_arc
        if nombre_arc != '':
            archi1=open(nombre_arc,"r",encoding="utf-8")
            contenido=archi1.read()
            archi1.close()
            self.scrolledtext1.delete("1.0", tk.END)
            self.scrolledtext1.insert("1.0", contenido)
aplicacion1 = Aplicacion()