
class Servico:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def executar(self, pet):
        raise NotImplementedError

    def __str__(self):
        return f"{self.nome} - R$ {self.preco:.2f}"
