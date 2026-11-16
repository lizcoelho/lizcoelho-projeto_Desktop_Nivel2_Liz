from models.pagamento import Pagamento


class Pix(Pagamento):
    def pagar(self, valor):
        print(f"Pagamento de R$ {valor:.2f} realizado via Pix.")
        