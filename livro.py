from abc import ABC, abstractmethod
from enum import Enum

class Status(Enum):
    DISPONIVEL = 'disponivel'
    RESERVADO = "reservado"

class Livro(ABC):
    def __init__(self, titulo,autor,ISBN):
        self.titulo = titulo
        self.autor = autor
        self.ISBN = ISBN
        self.status = Status.DISPONIVEL

    @abstractmethod
    def reservar():
        raise NotImplementedError("Metodo abstrado deve ser implementado")

    def devolver(self):
        self.status = Status.DISPONIVEL
        print("Devolução feita com sucesso!")
         
