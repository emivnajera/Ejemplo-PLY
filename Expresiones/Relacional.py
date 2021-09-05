from abstract.instruccion import Instruccion
from abstract.NodoAST import NodoAST
from TS.Excepcion import Excepcion
from TS.Tipo import TIPO, OperadorRelacional

class Relacional(Instruccion):
    def __init__(self, operador, OperacionIzq, OperacionDer, fila, columna):
        self.operador = operador
        self.OperacionIzq =OperacionIzq
        self.OperacionDer = OperacionDer
        self.fila = fila
        self.columna = columna
        self.tipo = TIPO.BOOLEANO


    def interpretar(self, tree, table):
        izq = self.OperacionIzq.interpretar(tree, table)
        if isinstance(izq, Excepcion): return izq
        der = self.OperacionDer.interpretar(tree, table)
        if isinstance(der, Excepcion): return der


        if self.operador == OperadorRelacional.MENORQUE:
            if self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.ENTERO:#int con int
                return self.obtenerVal(self.OperacionIzq.tipo, izq) < self.obtenerVal(self.OperacionDer.tipo, der)

            elif self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.DECIMAL:#int con double
                return self.obtenerVal(self.OperacionIzq.tipo, izq) < self.obtenerVal(self.OperacionDer.tipo, der)

            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.ENTERO:#double con int
                return self.obtenerVal(self.OperacionIzq.tipo, izq) < self.obtenerVal(self.OperacionDer.tipo, der)

            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.DECIMAL:#double con double
                return self.obtenerVal(self.OperacionIzq.tipo, izq) < self.obtenerVal(self.OperacionDer.tipo, der)

            elif self.OperacionIzq.tipo == TIPO.BOOLEANO and self.OperacionDer.tipo == TIPO.BOOLEANO:#boolean con boolean
                return self.obtenerVal(self.OperacionIzq.tipo, izq) < self.obtenerVal(self.OperacionDer.tipo, der)
            return Excepcion("Semantico", "Tipo Erroneo de operacion para <.", self.fila, self.columna)

        elif self.operador == OperadorRelacional.MAYORQUE:
            if self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.ENTERO:#int con int
                return self.obtenerVal(self.OperacionIzq.tipo, izq) > self.obtenerVal(self.OperacionDer.tipo, der)

            elif self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.DECIMAL:#int con double
                return self.obtenerVal(self.OperacionIzq.tipo, izq) > self.obtenerVal(self.OperacionDer.tipo, der)

            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.ENTERO:#decimal con int
                return self.obtenerVal(self.OperacionIzq.tipo, izq) > self.obtenerVal(self.OperacionDer.tipo, der)

            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.DECIMAL:#decimal con decimal
                return self.obtenerVal(self.OperacionIzq.tipo, izq) > self.obtenerVal(self.OperacionDer.tipo, der)

            elif self.OperacionIzq.tipo == TIPO.BOOLEANO and self.OperacionDer.tipo == TIPO.BOOLEANO:#boolean con boolean
                return self.obtenerVal(self.OperacionIzq.tipo, izq) > self.obtenerVal(self.OperacionDer.tipo, der)
            return Excepcion("Semantico", "Tipo Erroneo de operacion para >.", self.fila, self.columna)

        elif self.operador == OperadorRelacional.IGUALIGUAL:
            if self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.ENTERO:#int con int
                return self.obtenerVal(self.OperacionIzq.tipo, izq) == self.obtenerVal(self.OperacionDer.tipo, der)

            elif self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.DECIMAL:#int con double
                return self.obtenerVal(self.OperacionIzq.tipo, izq) == self.obtenerVal(self.OperacionDer.tipo, der)

            elif self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.CADENA:#int con string
                return str(self.obtenerVal(self.OperacionIzq.tipo, izq))== self.obtenerVal(self.OperacionDer.tipo, der)

            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.ENTERO:#double con int
                return self.obtenerVal(self.OperacionIzq.tipo, izq) == self.obtenerVal(self.OperacionDer.tipo, der)

            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.DECIMAL:#double con double
                return self.obtenerVal(self.OperacionIzq.tipo, izq) == self.obtenerVal(self.OperacionDer.tipo, der)

            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.CADENA:#double con string
                return str(self.obtenerVal(self.OperacionIzq.tipo, izq)) == self.obtenerVal(self.OperacionDer.tipo, der)

            elif self.OperacionIzq.tipo == TIPO.BOOLEANO and self.OperacionDer.tipo == TIPO.BOOLEANO:#boolean con boolean
                return self.obtenerVal(self.OperacionIzq.tipo, izq) == self.obtenerVal(self.OperacionDer.tipo, der)

            elif self.OperacionIzq.tipo == TIPO.BOOLEANO and self.OperacionDer.tipo == TIPO.CADENA:#boolean con cadena
                return self.obtenerVal(self.OperacionIzq.tipo, izq) == bool(self.obtenerVal(self.OperacionDer.tipo, der))

            elif self.OperacionIzq.tipo == TIPO.CARACTER and self.OperacionDer.tipo == TIPO.CARACTER:#caracter con caracter
                return self.obtenerVal(self.OperacionIzq.tipo, izq) == self.obtenerVal(self.OperacionDer.tipo, der)

            elif self.OperacionIzq.tipo == TIPO.CADENA and self.OperacionDer.tipo == TIPO.ENTERO:#cadena con entero
                return self.obtenerVal(self.OperacionIzq.tipo, izq) == str(self.obtenerVal(self.OperacionDer.tipo, der))

            elif self.OperacionIzq.tipo == TIPO.CADENA and self.OperacionDer.tipo == TIPO.DECIMAL:#cadena con decimal
                return self.obtenerVal(self.OperacionIzq.tipo, izq) == str(self.obtenerVal(self.OperacionDer.tipo, der))

            elif self.OperacionIzq.tipo == TIPO.CADENA and self.OperacionDer.tipo == TIPO.BOOLEANO:#cadena con boolean
                return bool(self.obtenerVal(self.OperacionIzq.tipo, izq)) == self.obtenerVal(self.OperacionDer.tipo, der)

            elif self.OperacionIzq.tipo == TIPO.CADENA and self.OperacionDer.tipo == TIPO.CADENA:#cadena con cadena
                return self.obtenerVal(self.OperacionIzq.tipo, izq) == self.obtenerVal(self.OperacionDer.tipo, der)
            return Excepcion("Semantico", "Tipo Erroneo de operacion para ==.", self.fila, self.columna)

        elif self.operador == OperadorRelacional.DIFERENTE:
            if self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.ENTERO:  # int con int
                return self.obtenerVal(self.OperacionIzq.tipo, izq) != self.obtenerVal(self.OperacionDer.tipo, der)

            elif self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.DECIMAL:  # int con double
                return self.obtenerVal(self.OperacionIzq.tipo, izq) != self.obtenerVal(self.OperacionDer.tipo, der)

            elif self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.CADENA:  # int con string
                return str(self.obtenerVal(self.OperacionIzq.tipo, izq)) != self.obtenerVal(self.OperacionDer.tipo, der)

            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.ENTERO:  # double con int
                return self.obtenerVal(self.OperacionIzq.tipo, izq) != self.obtenerVal(self.OperacionDer.tipo, der)

            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.DECIMAL:  # double con double
                return self.obtenerVal(self.OperacionIzq.tipo, izq) != self.obtenerVal(self.OperacionDer.tipo, der)

            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.CADENA:  # double con string
                return str(self.obtenerVal(self.OperacionIzq.tipo, izq)) != self.obtenerVal(self.OperacionDer.tipo, der)

            elif self.OperacionIzq.tipo == TIPO.BOOLEANO and self.OperacionDer.tipo == TIPO.BOOLEANO:  # boolean con boolean
                return self.obtenerVal(self.OperacionIzq.tipo, izq) != self.obtenerVal(self.OperacionDer.tipo, der)

            elif self.OperacionIzq.tipo == TIPO.BOOLEANO and self.OperacionDer.tipo == TIPO.CADENA:  # boolean con cadena
                return self.obtenerVal(self.OperacionIzq.tipo, izq) != bool(self.obtenerVal(self.OperacionDer.tipo, der))

            elif self.OperacionIzq.tipo == TIPO.CARACTER and self.OperacionDer.tipo == TIPO.CARACTER:  # caracter con caracter
                return self.obtenerVal(self.OperacionIzq.tipo, izq) != self.obtenerVal(self.OperacionDer.tipo, der)

            elif self.OperacionIzq.tipo == TIPO.CADENA and self.OperacionDer.tipo == TIPO.ENTERO:  # cadena con entero
                return self.obtenerVal(self.OperacionIzq.tipo, izq) != str(self.obtenerVal(self.OperacionDer.tipo, der))

            elif self.OperacionIzq.tipo == TIPO.CADENA and self.OperacionDer.tipo == TIPO.DECIMAL:  # cadena con decimal
                return self.obtenerVal(self.OperacionIzq.tipo, izq) != str(self.obtenerVal(self.OperacionDer.tipo, der))

            elif self.OperacionIzq.tipo == TIPO.CADENA and self.OperacionDer.tipo == TIPO.BOOLEANO:  # cadena con boolean
                return bool(self.obtenerVal(self.OperacionIzq.tipo, izq)) != self.obtenerVal(self.OperacionDer.tipo,                                                                                           der)

            elif self.OperacionIzq.tipo == TIPO.CADENA and self.OperacionDer.tipo == TIPO.CADENA:  # cadena con cadena
                return self.obtenerVal(self.OperacionIzq.tipo, izq) != self.obtenerVal(self.OperacionDer.tipo, der)
            return Excepcion("Semantico", "Tipo Erroneo de operacion para =!.", self.fila, self.columna)

        elif self.operador == OperadorRelacional.MENORIGUAL:
            if self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.ENTERO:#int con int
                return self.obtenerVal(self.OperacionIzq.tipo, izq) <= self.obtenerVal(self.OperacionDer.tipo, der)

            elif self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.DECIMAL:#int con double
                return self.obtenerVal(self.OperacionIzq.tipo, izq) <= self.obtenerVal(self.OperacionDer.tipo, der)

            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.ENTERO:#double con int
                return self.obtenerVal(self.OperacionIzq.tipo, izq) <= self.obtenerVal(self.OperacionDer.tipo, der)

            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.DECIMAL:#double con double
                return self.obtenerVal(self.OperacionIzq.tipo, izq) <= self.obtenerVal(self.OperacionDer.tipo, der)

            elif self.OperacionIzq.tipo == TIPO.BOOLEANO and self.OperacionDer.tipo == TIPO.BOOLEANO:#boolean con boolean
                return self.obtenerVal(self.OperacionIzq.tipo, izq) <= self.obtenerVal(self.OperacionDer.tipo, der)
            return Excepcion("Semantico", "Tipo Erroneo de operacion para <=.", self.fila, self.columna)

        elif self.operador == OperadorRelacional.MAYORIGUAL:
            if self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.ENTERO:#int con int
                return self.obtenerVal(self.OperacionIzq.tipo, izq) >= self.obtenerVal(self.OperacionDer.tipo, der)

            elif self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.DECIMAL:#int con double
                return self.obtenerVal(self.OperacionIzq.tipo, izq) >= self.obtenerVal(self.OperacionDer.tipo, der)

            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.ENTERO:#double con int
                return self.obtenerVal(self.OperacionIzq.tipo, izq) >= self.obtenerVal(self.OperacionDer.tipo, der)

            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.DECIMAL:#double con double
                return self.obtenerVal(self.OperacionIzq.tipo, izq) >= self.obtenerVal(self.OperacionDer.tipo, der)

            elif self.OperacionIzq.tipo == TIPO.BOOLEANO and self.OperacionDer.tipo == TIPO.BOOLEANO:#boolean con boolean
                return self.obtenerVal(self.OperacionIzq.tipo, izq) >= self.obtenerVal(self.OperacionDer.tipo, der)
            return Excepcion("Semantico", "Tipo Erroneo de operacion para >=.", self.fila, self.columna)
        return Excepcion("Semantico", str(self.operador), self.fila, self.columna)


    def obtenerVal(self, tipo, val):
        if tipo == TIPO.ENTERO:
            return int(val)
        elif tipo == TIPO.DECIMAL:
            return float(val)
        elif tipo == TIPO.BOOLEANO:
            return bool(val)
        return str(val)

    def getNodo(self):
        nodo = NodoAST("RELACIONAL")
        nodo.agregarHijoNodo(self.OperacionIzq.getNodo())
        nodo.agregarHijo(str(self.operador))
        nodo.agregarHijoNodo(self.OperacionDer.getNodo())


        return nodo