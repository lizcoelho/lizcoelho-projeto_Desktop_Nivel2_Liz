from models.item_venda import ItemVenda


class Venda:
    def __init__(self, cliente):
        self.cliente = cliente
        self.itens = []

    def adicionar_item(self, descricao, quantidade, preco_unitario):
        item = ItemVenda(descricao, quantidade, preco_unitario)
        self.itens.append(item)

    def calcular_total(self):
        return sum(item.subtotal() for item in self.itens)

    def exibir_venda(self):
        print("\nVenda realizada!")
        print(f"Cliente: {self.cliente.nome}")

        for item in self.itens:
            print(
                f"{item.descricao} - "
                f"Quantidade: {item.quantidade} - "
                f"Subtotal: R$ {item.subtotal():.2f}"
            )

        print(f"Total: R$ {self.calcular_total():.2f}")
        