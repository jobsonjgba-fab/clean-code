from . import Cardapio


class ItemPedido:
    def __init__(self, cardapio: Cardapio, quantidade, observacao: str):
        self._validar_quantidade(quantidade)
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
        self._validar_quantidade(value)
        self._quantidade = value

    def _validar_quantidade(self, value) -> None:
        if not isinstance(value, int):
            raise QuantidadeInvalidaError()
        if value < 0:
            raise QuantidadeInvalidaError()


class QuantidadeInvalidaError(ValueError):
    pass
