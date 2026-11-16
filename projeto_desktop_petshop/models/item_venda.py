class ItemVenda:
    def __init__(self, descricao, quantidade, preco_unitario):
        self.descricao = descricao
        self.quantidade = quantidade
        self.preco_unitario = preco_unitario

    def subtotal(self):
        return self.quantidade * self.preco_unitario
    