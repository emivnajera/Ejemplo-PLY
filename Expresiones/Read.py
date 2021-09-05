from abstract.instruccion import Instruccion
from abstract.NodoAST import NodoAST
from TS.Tipo import TIPO
import tkinter as tk
from tkinter import simpledialog


class Read(Instruccion):
    def __init__(self, fila, columna):
        self.fila = fila
        self.columna = columna
        self.tipo = TIPO.CADENA

    def interpretar(self, tree, table):
        tree.getTexto().insert(tk.END, tree.getConsola())
        tree.setConsola("")  # RESETEA LA CONSOLA
        root = tk.Tk()  # Create an instance of tkinter
        lectura = simpledialog.askstring(title = "Read",prompt = "Ingrese el Valor de la Variable")  # OBTENERME EL VALOR INGRESADO
        return str(lectura)

    def getNodo(self):
        nodo = NodoAST("READ")
        return nodo


