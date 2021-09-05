from TS.Excepcion import Excepcion
from TS.Tipo import TIPO
from Instrucciones.Funcion import Funcion


class Typeof(Funcion):
    def __init__(self, nombre, parametros, instrucciones, fila, columna):
        self.nombre = nombre.lower()
        self.parametros = parametros
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna
        self.tipo = TIPO.NULO

    def interpretar(self, tree, table):
        simbolo = table.getTabla("Typeof##Param1")
        if simbolo == None : return Excepcion("Semantico", "No se encontró el parámetro de Typeof", self.fila, self.columna)

        self.tipo = TIPO.CADENA

        if simbolo.getTipo() == TIPO.DECIMAL:
            return 'DOUBLE'
        if simbolo.getTipo() == TIPO.ENTERO:
            return 'INT'
        if simbolo.getTipo() == TIPO.CADENA:
            return 'STRING'
        if simbolo.getTipo() == TIPO.CARACTER:
            return 'CHAR'
        if simbolo.getTipo() == TIPO.NULO:
            return 'NULL'
        if simbolo.getTipo() == TIPO.BOOLEANO:
            return 'BOOLEAN'