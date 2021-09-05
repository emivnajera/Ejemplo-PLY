from TS.Excepcion import Excepcion
from abstract.instruccion import Instruccion
from abstract.NodoAST import NodoAST
from TS.Simbolo import Simbolo
from TS.Tipo import TIPO
from Instrucciones.Simbolo import Tsimbolo
from Instrucciones.Llamada import Llamada

class Declaracion(Instruccion):
    def __init__(self, identificador, fila, columna, expresion=None):
        self.identificador = identificador
        self.expresion = expresion
        self.fila = fila
        self.columna = columna
        self.tipo = None
        self.arreglo = False

    def interpretar(self, tree, table):
        if self.expresion != None:
                value = self.expresion.interpretar(tree, table)  # Valor a asignar a la variable

                self.tipo = self.expresion.tipo

                if isinstance(value, Excepcion): return value


                simbolo = Simbolo(str(self.identificador), self.tipo, self.arreglo, self.fila, self.columna, value)

                nsimbolo = Tsimbolo(str(self.identificador), str(self.fila), str(self.columna), str(self.tipo), str(value))

                tree.addSimbolo(nsimbolo)

                result = table.setTabla(simbolo)

                if isinstance(result, Excepcion): return result
        else:
            self.tipo = TIPO.NULO
            simbolo = Simbolo(str(self.identificador), self.tipo,self.arreglo, self.fila, self.columna, None)

            nsimbolo = Tsimbolo(str(self.identificador), str(self.fila), str(self.columna), str(self.tipo), str(None))

            tree.addSimbolo(nsimbolo)

            result = table.setTabla(simbolo)

            if isinstance(result, Excepcion): return result
        return None

    def getNodo(self):
        nodo = NodoAST("DECLARACION")
        nodo.agregarHijo(str(self.tipo))
        nodo.agregarHijo(str(self.identificador))
        if self.expresion != None:
            nodo.agregarHijoNodo(self.expresion.getNodo())
        return nodo