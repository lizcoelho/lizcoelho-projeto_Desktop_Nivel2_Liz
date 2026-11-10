
from models.servico import Servico


class Consulta(Servico):
    def __init__(self, preco):
        super().__init__("Consulta veterinária", preco)

    def executar(self, pet):
        print(f"Realizando consulta veterinária para {pet.nome}.")
