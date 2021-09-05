from abstract.instruccion import Instruccion
from abstract.NodoAST import NodoAST
from TS.Excepcion import Excepcion
from TS.Tipo import TIPO

class Imprimir(Instruccion):
    def __init__(self, expresion, fila, columna):
        self.expresion = expresion
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        value = self.expresion.interpretar(tree, table)
        if isinstance(value, Excepcion):
            return value
        if self.expresion.tipo == TIPO.ARRGELO:
            return Excepcion("Sematico", "No se puede imprimir un arreglo completo", self.fila, self.columna)
        tree.updateConsola(value)

    def getNodo(self):
        nodo = NodoAST("IMPRIMIR")
        nodo.agregarHijoNodo(self.expresion.getNodo())
        return nodo