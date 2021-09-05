from abstract.instruccion import Instruccion
from abstract.NodoAST import NodoAST
from TS.Excepcion import Excepcion
from TS.Tipo import TIPO
from TS.TablaSimbolos import TablaSimbolos
from Instrucciones.Break import Break
from Instrucciones.Case import Case

class Switch(Instruccion):
    def __init__(self, condicion, cases, fila, columna):
        self.condicion = condicion
        self.cases = cases
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        condicion = self.condicion.interpretar(tree, table)
        if isinstance(condicion, Excepcion): return condicion
        nuevaTabla = TablaSimbolos(table)       #NUEVO ENTORNO
        for case in self.cases:
            if isinstance(case, Case):
                case.setSwitch(condicion)
            result = case.interpretar(tree, nuevaTabla) #EJECUTA INSTRUCCION ADENTRO DEL CASE
            if isinstance(result, Excepcion): return result

    def getNodo(self):
        nodo = NodoAST("SWITCH")
        for case in self.cases:
                nodo.agregarHijoNodo(case.getNodo())
        return nodo