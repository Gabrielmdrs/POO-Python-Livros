from livro import Livro
class LivroReferencia(Livro):
    def __init__(self,titulo,autor,isbn,tema):
        super().__init__(titulo,autor,isbn)
        self.tema = tema

    def reservar(self):
        return "Este livro nao pode ser reservado"