
class Agendamento:
    def __init__(self, cliente, pet, tipo_servico, preco, data):
        self.cliente = cliente
        self.pet = pet
        self.data = data

        # O agendamento cria e controla seu serviço
        self.servico = tipo_servico(preco)

    def realizar_agendamento(self):
        print("\nAgendamento realizado!")
        print(f"Cliente: {self.cliente.nome}")
        print(f"Pet: {self.pet.nome}")
        print(f"Serviço: {self.servico.nome}")
        print(f"Data: {self.data}")

    def realizar_servico(self):
        self.servico.executar(self.pet)
