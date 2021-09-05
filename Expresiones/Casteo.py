from abstract.instruccion import Instruccion
from abstract.NodoAST import NodoAST
from TS.Excepcion import Excepcion
from TS.Tipo import TIPO, OperadorLogico

class Casteo(Instruccion):
    def __init__(self, tipo, expresion, fila, columna):
        self.expresion = expresion
        self.fila = fila
        self.columna = columna
        self.tipo = tipo

    def interpretar(self, tree, table):
        val = self.expresion.interpretar(tree, table)


        if self.tipo == TIPO.DECIMAL:
            if self.expresion.tipo == TIPO.ENTERO:
                try:
                    return float(self.obtenerVal(self.expresion.tipo, val))
                except:
                    return Excepcion("Semantico", "No se puede castear para Float.", self.fila, self.columna)
            elif self.expresion.tipo == TIPO.CADENA:
                try:
                    return float(self.obtenerVal(self.expresion.tipo, val))
                except:
                    return Excepcion("Semantico", "No se puede castear para Float.", self.fila, self.columna)
            elif self.expresion.tipo == TIPO.CARACTER:
                try:
                    return float(ord(self.obtenerVal(self.expresion.tipo, val)))
                except:
                    return Excepcion("Semantico", "No se puede castear para Float.", self.fila, self.columna)
            return Excepcion("Semantico", "Tipo Erroneo de casteo para Double.", self.fila, self.columna)


        if self.tipo == TIPO.ENTERO:
            if self.expresion.tipo == TIPO.DECIMAL:
                try:
                    return int(self.obtenerVal(self.expresion.tipo, val))
                except:
                    return Excepcion("Semantico", "No se puede castear para Int. decimal", self.fila, self.columna)
            elif self.expresion.tipo == TIPO.CADENA:
                try:
                    return int(self.obtenerVal(self.expresion.tipo, val))
                except:
                    return Excepcion("Semantico", "No se puede castear para Int. str", self.fila, self.columna)
            elif self.expresion.tipo == TIPO.CARACTER:
                try:
                    return int(ord(self.obtenerVal(self.expresion.tipo, val)))
                except:
                    return Excepcion("Semantico", "No se puede castear para Int. char", self.fila, self.columna)
            return Excepcion("Semantico", "Tipo Erroneo de casteo para Int.", self.fila, self.columna)

        if self.tipo == TIPO.CADENA:
            if self.expresion.tipo == TIPO.ENTERO:
                try:
                    return str(self.obtenerVal(self.expresion.tipo, val))
                except:
                    return Excepcion("Semantico", "No se puede castear para String.", self.fila, self.columna)
            elif self.expresion.tipo == TIPO.DECIMAL:
                try:
                    return str(self.obtenerVal(self.expresion.tipo, val))
                except:
                    return Excepcion("Semantico", "No se puede castear para String.", self.fila, self.columna)
            return Excepcion("Semantico", "Tipo Erroneo de casteo para String.", self.fila, self.columna)

        if self.tipo == TIPO.CARACTER:
            if self.expresion.tipo == TIPO.ENTERO:
                try:
                    return str(self.obtenerVal(self.expresion.tipo, val))
                except:
                        return Excepcion("Semantico", "No se puede castear para Char.", self.fila, self.columna)
            return Excepcion("Semantico", "Tipo Erroneo de casteo para Char.", self.fila, self.columna)

        if self.tipo == TIPO.BOOLEANO:
            if self.expresion.tipo == TIPO.CADENA:
                exp = self.obtenerVal(self.expresion.tipo, val)
                if exp.lower()=="false":
                    valor = 0
                if exp.lower()=='true':
                    valor=1
                try:
                    return bool((valor))
                except:
                        return Excepcion("Semantico", "No se puede castear para bool.", self.fila, self.columna)
            return Excepcion("Semantico", "Tipo Erroneo de casteo para bool.", self.fila, self.columna)


    def obtenerVal(self, tipo, val):
        if tipo == TIPO.ENTERO:
            return int(val)
        elif tipo == TIPO.DECIMAL:
            return float(val)
        elif tipo == TIPO.BOOLEANO:
            return bool(val)
        return str(val)

    def getNodo(self):
        nodo = NodoAST("CASTEO")
        nodo.agregarHijo(str(self.tipo))
        nodo.agregarHijoNodo(self.expresion.getNodo())
        return nodo