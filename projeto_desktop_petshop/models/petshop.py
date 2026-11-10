
class PetShop:
    def confirmar_agendamento(self, agendamento, funcionario):
        print("\nAgendamento confirmado pelo Pet Shop!")
        print(f"Responsável: {funcionario.nome}")
        agendamento.realizar_agendamento()
