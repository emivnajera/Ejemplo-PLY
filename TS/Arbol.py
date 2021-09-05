class Arbol:
    def __init__(self, instrucciones):
        self.instrucciones = instrucciones
        self.excepciones = []
        self.funciones = []
        self.consola = ""
        self.TSglobal = None
        self.dot = ""
        self.contador = 0
        self.texto = None
        self.simbolos = []

    def getInstrucciones(self):
        return self.instrucciones

    def setInstrucciones(self, instrucciones):
        self.instrucciones = instrucciones

    def getExcepciones(self):
        return self.excepciones

    def setExcepciones(self, excepciones):
        self.excepciones = excepciones

    def getConsola(self):
        return self.consola

    def setConsola(self, consola):
        self.consola = consola

    def updateConsola(self, cadena):
        self.consola += str(cadena) + '\n'

    def getTSGlobal(self):
        return self.TSglobal

    def setTSglobal(self, TSglobal):
        self.TSglobal = TSglobal

    def getFunciones(self):
        return self.funciones

    def getFuncion(self, nombre):
        for funcion in self.funciones:
            if funcion.nombre == nombre:
                return funcion
        return None

    def addFuncion(self, funcion):
        self.funciones.append(funcion)

    def getDot(self, raiz): ## DEVUELVE EL STRING DE LA GRAFICA EN GRAPHVIZ
        self.dot = ""
        self.dot += "digraph {\n"
        self.dot += "n0[label=\"" + raiz.getValor().replace("\"", "\\\"") + "\"];\n"
        self.contador = 1
        self.recorrerAST("n0", raiz)
        self.dot += "}"
        return self.dot

    def setTexto(self, texto):
        self.texto = texto

    def getTexto(self):
        return self.texto

    def recorrerAST(self, idPadre, nodoPadre):
        for hijo in nodoPadre.getHijos():
            nombreHijo = "n" + str(self.contador)
            self.dot += nombreHijo + "[label=\"" + hijo.getValor().replace("\"", "\\\"") + "\"];\n"
            self.dot += idPadre + "->" + nombreHijo + ";\n"
            self.contador += 1
            self.recorrerAST(nombreHijo, hijo)\

    def addSimbolo(self, simbolo):
        self.simbolos.append(simbolo)

    def getSimbolos(self):
        return self.simbolos
