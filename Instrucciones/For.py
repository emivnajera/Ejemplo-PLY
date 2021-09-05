from abstract.instruccion import Instruccion
from abstract.NodoAST import NodoAST
from TS.Excepcion import Excepcion
from TS.Tipo import TIPO
from TS.TablaSimbolos import TablaSimbolos
from Instrucciones.Break import Break
from Instrucciones.Return import Return
from Instrucciones.Continue import Continue

class For(Instruccion):
    def __init__(self, declaracion, condicion, actualizacion, instrucciones, fila, columna):
        self.declaracion = declaracion
        self.condicion = condicion
        self.condicion = condicion
        self.instrucciones = instrucciones
        self.actualizacion = actualizacion
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        nuevaTabla = TablaSimbolos(table)
        declaracion = self.declaracion.interpretar(tree, nuevaTabla)
        if isinstance(declaracion, Excepcion): return declaracion
        while True:
            condicion = self.condicion.interpretar(tree, nuevaTabla)
            if isinstance(condicion, Excepcion): return condicion

            if self.condicion.tipo == TIPO.BOOLEANO:
                if bool(condicion) == True:   # VERIFICA SI ES VERDADERA LA CONDICION
                    for instruccion in self.instrucciones:
                        result = instruccion.interpretar(tree, nuevaTabla) #EJECUTA INSTRUCCION ADENTRO DEL IF
                        if isinstance(result, Excepcion) :
                            tree.getExcepciones().append(result)
                            tree.updateConsola(result.toString())
                        actualizacion = self.actualizacion.interpretar(tree,nuevaTabla)
                        if isinstance(actualizacion, Excepcion): return actualizacion
                        if isinstance(result, Break): return None
                        if isinstance(result, Return): return result
                        if isinstance(result, Return): return result
                        if isinstance(result, Continue): break
                else:
                    break
            else:
                return Excepcion("Semantico", "Tipo de dato no booleano en While.", self.fila, self.columna)


    def getNodo(self):
        nodo = NodoAST("FOR")

        instrucciones = NodoAST("INSTRUCCIONES")
        for instr in self.instrucciones:
            instrucciones.agregarHijoNodo(instr.getNodo())
        nodo.agregarHijoNodo(instrucciones)
        return nodo