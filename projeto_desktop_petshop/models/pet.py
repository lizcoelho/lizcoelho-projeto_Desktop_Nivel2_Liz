
class Pet:
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie

    def __str__(self):
        return f"{self.nome} - {self.especie}"
