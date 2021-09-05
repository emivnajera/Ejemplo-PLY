from TS.Excepcion import Excepcion
from abstract.NodoAST import NodoAST
from abstract.instruccion import Instruccion
from TS.Tipo import TIPO

class Identificador(Instruccion):
    def __init__(self, identificador, fila, columna):
        self.identificador = identificador
        self.fila = fila
        self.columna = columna
        self.tipo = None

    def interpretar(self, tree, table):
        simbolo = table.getTabla(self.identificador.lower())

        if simbolo == None:
            return Excepcion("Semantico", "Variable " + self.identificador + " no encontrada.", self.fila, self.columna)

        self.tipo = simbolo.getTipo()
        if self.tipo == TIPO.NULO:
            return Excepcion("Semantico", "NULLPOINTER EXCEPTION", self.fila, self.columna)
        else:
            return simbolo.getValor()

    def getNodo(self):
        nodo = NodoAST("IDENTIFICADOR")
        nodo.agregarHijo(str(self.identificador))
        return nodo