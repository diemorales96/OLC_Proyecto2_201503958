from abc import ABC, abstractmethod
from Symbol.Environment import *

class Expression(ABC):
    
    def __init__(self, fila, columna):
        self.line = fila
        self.column = columna
        self.trueLbl = ''
        self.falseLbl = ''
        self.structType = ''
    
    @abstractmethod
    def compile(self, environment):
        pass