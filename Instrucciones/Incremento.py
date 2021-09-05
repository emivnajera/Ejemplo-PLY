from TS.Excepcion import Excepcion
from abstract.instruccion import Instruccion
from abstract.NodoAST import NodoAST
from TS.Tipo import TIPO

class Incremento(Instruccion):
    def __init__(self, identificador, fila, columna):
        self.identificador = identificador
        self.tipo = None
        self.columna = columna
        self.fila = fila

    def interpretar(self, tree, table):
        simbolo = table.getTabla(self.identificador.lower())

        if simbolo == None:
            return Excepcion("Semantico", "Variable " + self.identificador + " no encontrada.", self.fila, self.columna)

        self.tipo = simbolo.getTipo()


        if self.tipo == TIPO.ENTERO or self.tipo == TIPO.DECIMAL:
            valor_ant = simbolo.getValor()

            valor_act = valor_ant + 1
            simbolo.setValor(valor_act)

            return simbolo.getValor()
        else:
            return Excepcion("Semantico", "Variable de Tipo Incorrecto", self.fila, self.columna)


    def getNodo(self):
        nodo = NodoAST("INCREMENTO")
        nodo.agregarHijo(str(self.identificador))
        return nodo
