from TS.Excepcion import  Excepcion
from  TS.Tipo import TIPO

class TablaSimbolos:
    def __init__(self, anterior = None):
        self.tabla = {}
        self.anterior = anterior
        self.funciones = []

    def setTabla(self, simbolo):
        if simbolo.id in self.tabla:
            return Excepcion("Semantico", "Variable '" + simbolo.id + "' Ya existe", simbolo.fila, simbolo.columna)
        else:
            self.tabla[simbolo.id] = simbolo
            return None

    def getTabla(self, id):
        tablaActual = self
        while tablaActual != None:
            if id in tablaActual.tabla:
                return tablaActual.tabla[id]
            else:
                tablaActual = tablaActual.anterior
        return None


    def actualizarTabla(self, simbolo):
        tablaActual = self
        while tablaActual != None:
            if simbolo.id in tablaActual.tabla:
                if simbolo.id.lower() in tablaActual.tabla:
                    if (tablaActual.tabla[simbolo.id.lower()].getTipo() == TIPO.NULO or simbolo.getTipo() == TIPO.NULO) or (tablaActual.tabla[simbolo.id.lower()].getTipo() == simbolo.getTipo()):
                        tablaActual.tabla[simbolo.id.lower()].setValor(simbolo.getValor())
                        tablaActual.tabla[simbolo.id.lower()].setTipo(simbolo.getTipo())
                        return None # VARIABLE ACTUALIZADA
                return Excepcion("Semantico", "Tipo de dato Diferente a Nulo", simbolo.getFila(),simbolo.getColumna())
            else:
                tablaActual= tablaActual.anterior
        return None