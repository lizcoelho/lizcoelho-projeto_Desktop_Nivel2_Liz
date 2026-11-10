
class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.pets = []

    def adicionar_pet(self, pet):
        self.pets.append(pet)

    def listar_pets(self):
        for pet in self.pets:
            print(pet)

    def __str__(self):
        return f"Cliente: {self.nome}"
