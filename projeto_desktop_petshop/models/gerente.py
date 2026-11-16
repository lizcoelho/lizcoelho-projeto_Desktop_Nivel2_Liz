
from models.funcionario import Funcionario


class Gerente(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)

    def gerenciar_petshop(self):
        print(f"{self.nome} está gerenciando o Pet Shop.")
