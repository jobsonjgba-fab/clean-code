from . import Cardapio


class ItemPedido:
    def __init__(self, cardapio: Cardapio, quantidade: int, observacao: str):
        self.opcao_menu = cardapio
        self.quantidade = quantidade
        self.observacao = observacao


class QuantidadeInvalidaError:
    pass
