
from models.funcionario import Funcionario


class Atendente(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)

    def atender_cliente(self):
        print(f"{self.nome} está atendendo um cliente.")
