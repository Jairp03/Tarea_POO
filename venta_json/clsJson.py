from abc import ABC, abstractmethod

class InterfaceJson(ABC):
    def __init__(self, filename):
        self.filename = filename

    @abstractmethod
    def save(self, data):
        pass
    @abstractmethod  
    def read(self):
        pass
    @abstractmethod 
    def find(self,atributo,buscado):
        pass