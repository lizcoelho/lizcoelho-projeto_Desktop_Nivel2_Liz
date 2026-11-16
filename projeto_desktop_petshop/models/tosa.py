
from models.servico import Servico


class Tosa(Servico):
    def __init__(self, preco):
        super().__init__("Tosa", preco)

    def executar(self, pet):
        print(f"Realizando tosa no pet {pet.nome}.")
