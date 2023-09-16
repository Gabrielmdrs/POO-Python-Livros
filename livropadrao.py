from datetime import datetime, timedelta
from livro import Livro,Status

class LivroPadrao(Livro):
    def __init__(self, titulo,autor,isbn):
        super().__init__(titulo,autor,isbn)
        self.dataDevolucao = None

    def reservar(self):
        if self.status == Status.DISPONIVEL:
            self.status = Status.RESERVADO
            self.dataDevolucao = datetime.now() + timedelta(days = 7)
            return f"Reserva realiza, devolver até: {self.dataDevolucao}"
        else:
            return "Livro indisponivel"

