class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

    def saudacao(self):
        return f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos."


pessoa1 = Pessoa("Alice", 30)
mensage1 = pessoa1.saudacao()
print(mensage1)

pessoa2 = Pessoa("Rodrigo", 32)
mensage2 = pessoa2.saudacao()
print(mensage2)
