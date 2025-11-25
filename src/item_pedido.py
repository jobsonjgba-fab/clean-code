from . import Cardapio


class ItemPedido:
    def __init__(self, cardapio: Cardapio, quantidade: int, observacao: str):
        if quantidade < 0:
            raise QuantidadeInvalidaError()
        self.opcao_menu = cardapio
        self.quantidade = quantidade
        self.observacao = observacao
        self.valor_total = cardapio.valor * quantidade


class QuantidadeInvalidaError(ValueError):
    pass
