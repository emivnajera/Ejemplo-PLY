from TS.Excepcion import Excepcion
from TS.Tipo import TIPO
from Instrucciones.Funcion import Funcion


class Round(Funcion):
    def __init__(self, nombre, parametros, instrucciones, fila, columna):
        self.nombre = nombre.lower()
        self.parametros = parametros
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna
        self.tipo = TIPO.NULO

    def interpretar(self, tree, table):
        simbolo = table.getTabla("Round##Param1")
        if simbolo == None : return Excepcion("Semantico", "No se encontró el parámetro de Round", self.fila, self.columna)

        if simbolo.getTipo() != TIPO.DECIMAL and simbolo.getTipo() != TIPO.ENTERO:
            return Excepcion("Semantico", "Tipo de parametro de Truncate no es numerico.", self.fila, self.columna)

        self.tipo = simbolo.getTipo()
        return round(float(simbolo.getValor()))