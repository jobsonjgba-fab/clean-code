from . import Cardapio


class ItemPedido:
    def __init__(self, cardapio: Cardapio, quantidade, observacao: str):
        if not isinstance(quantidade, int):
            raise QuantidadeInvalidaError()
        if quantidade < 0:
            raise QuantidadeInvalidaError()
        self.opcao_menu = cardapio
        self._quantidade = quantidade
        self.observacao = observacao

    @property
    def valor_total(self) -> float:
        return self.opcao_menu.valor * self.quantidade

    @property
    def quantidade(self) -> int:
        return self._quantidade

    @quantidade.setter
    def quantidade(self, value) -> None:
        if not isinstance(value, int):
            raise QuantidadeInvalidaError()
        if value < 0:
            raise QuantidadeInvalidaError()
        self._quantidade = value


class QuantidadeInvalidaError(ValueError):
    pass
