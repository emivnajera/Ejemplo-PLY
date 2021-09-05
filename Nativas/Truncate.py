from TS.Excepcion import Excepcion
from TS.Tipo import TIPO
from Instrucciones.Funcion import Funcion
from math import trunc

class Truncate(Funcion):
    def __init__(self, nombre, parametros, instrucciones, fila, columna):
        self.nombre = nombre.lower()
        self.parametros = parametros
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna
        self.tipo = TIPO.NULO

    def interpretar(self, tree, table):
        simbolo = table.getTabla("Truncate##Param1")
        if simbolo == None : return Excepcion("Semantico", "No se encontró el parámetro de Length", self.fila, self.columna)

        if simbolo.getTipo() != TIPO.DECIMAL and simbolo.getTipo() != TIPO.ENTERO:
            return Excepcion("Semantico", "Tipo de parametro de Truncate no es numerico.", self.fila, self.columna)

        self.tipo = simbolo.getTipo()
        return trunc(float(simbolo.getValor()))