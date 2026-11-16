
class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def trabalhar(self):
        print(f"{self.nome} está trabalhando.")

    def __str__(self):
        return f"Funcionário: {self.nome} | Salário: R$ {self.salario:.2f}"
