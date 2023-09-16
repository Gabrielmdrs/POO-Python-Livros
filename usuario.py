
class Usuario:
    def __init__(self, nome, id):
        self.nome = nome
        self.id = id

    def fazerReserva(self, livro):
        return livro.reservar()
    

    def fazerdevolver(self, livro):
        return livro.devolver()

        
        