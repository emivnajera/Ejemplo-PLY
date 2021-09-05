from abstract.instruccion import Instruccion
from abstract.NodoAST import NodoAST
from TS.Excepcion import Excepcion
from TS.Tipo import TIPO
from TS.TablaSimbolos import TablaSimbolos
from Instrucciones.Break import Break
from Instrucciones.Return import Return

class Default(Instruccion):
    def __init__(self, instrucciones, fila, columna):
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
            nuevaTabla = TablaSimbolos(table)  # NUEVO ENTORNO
            for instruccion in self.instrucciones:
                result = instruccion.interpretar(tree, nuevaTabla)  # EJECUTA INSTRUCCION ADENTRO DEL IF
                if isinstance(result, Excepcion):
                    tree.getExcepciones().append(result)
                    tree.updateConsola(result.toString())
                if isinstance(result, Break): return result
                if isinstance(result, Return): return result



    def getNodo(self):
        nodo = NodoAST("DEFAULT")

        instrucciones = NodoAST("INSTRUCCIONES DEFAULT")
        for instr in self.instrucciones:
            instrucciones.agregarHijoNodo(instr.getNodo())
        nodo.agregarHijoNodo(instrucciones)

        return nodo