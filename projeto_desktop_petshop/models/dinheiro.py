from models.pagamento import Pagamento


class Dinheiro(Pagamento):
    def pagar(self, valor):
        print(f"Pagamento de R$ {valor:.2f} realizado em dinheiro.")
        