from abstract.instruccion import Instruccion
from abstract.NodoAST import NodoAST
from TS.Excepcion import Excepcion
from TS.Tipo import TIPO
from TS.TablaSimbolos import TablaSimbolos
from Instrucciones.Break import Break
from Instrucciones.Return import Return

class Case(Instruccion):
    def __init__(self, expresion, instrucciones, fila, columna):
        self.expresion = expresion
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna
        self.switch = None

    def interpretar(self, tree, table):
        expresion = self.expresion.interpretar(tree, table)
        if isinstance(expresion, Excepcion): return expresion
        if str(self.expresion.valor) == str(self.switch):
            nuevaTabla = TablaSimbolos(table)
            for instruccion in self.instrucciones:
                result = instruccion.interpretar(tree, nuevaTabla)
                if isinstance(result, Excepcion) :
                    tree.getExcepciones().append(result)
                    tree.updateConsola(result.toString())
                if isinstance(result, Break): return result
                if isinstance(result, Return): return result

    def setSwitch(self, switch):
        self.switch = switch

    def getNodo(self):
        nodo = NodoAST("CASE")

        instrucciones = NodoAST("INSTRUCCIONES CASE")
        for instr in self.instrucciones:
            instrucciones.agregarHijoNodo(instr.getNodo())
        nodo.agregarHijoNodo(instrucciones)

        return nodo