from livro import Livro
from livropadrao import LivroPadrao
from livroreferencia import LivroReferencia
from usuario import Usuario

livro1 = LivroPadrao("xxx","John",4444)
livro2 = LivroReferencia("yyy","Mike",8888,"Artes")
Usuario1 = Usuario("Bruno", 33)
art = Usuario1.fazerReserva(livro1)
print(art)