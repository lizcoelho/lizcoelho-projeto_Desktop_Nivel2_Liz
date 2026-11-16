
from models.servico import Servico


class Banho(Servico):
    def __init__(self, preco):
        super().__init__("Banho", preco)

    def executar(self, pet):
        print(f"Realizando banho no pet {pet.nome}.")
