from abc import ABC, abstractmethod

class Instruccion(ABC):
    def __init__(self, fila, columna):
        self.fila = fila
        self.columna = columna
        self.arreglo = False
        super().__init__()

    @abstractmethod
    def interpretar(self, tree, table):
        pass

    @abstractmethod
    def getNodo(self):
        pass
