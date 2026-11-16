class SistemaPagamento:
    def processar_pagamento(self, venda, pagamento):
        valor = venda.calcular_total()

        print("\nProcessando pagamento...")
        pagamento.pagar(valor)
        