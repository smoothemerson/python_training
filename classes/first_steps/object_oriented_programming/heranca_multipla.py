class Animal:
    def __init__(self, nome) -> None:
        self.nome = nome

    def emitir_som(self) -> str:
        return ""


class Mamifero(Animal):
    def amamentar(self):
        return f"{self.nome} está amamentando."


class Ave(Animal):
    def voar(self):
        return f"{self.nome} está voando."


class Morcego(Mamifero, Ave):
    def emitir_som(self) -> str:
        return "Morcegos emitem sons ultrassônicos"


morcego = Morcego("Batman")

print(f"Nome: {morcego.nome}")
print(f"Som do morcego: {morcego.emitir_som()}")

print(f"Morcego amamentando: {morcego.amamentar()}")
print(f"Morcego voando: {morcego.voar()}")
