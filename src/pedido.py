from datetime import datetime
from enum import Enum

from . import Cliente, ItemPedido


class Pedido:
    def __init__(
        self,
        cliente: Cliente,
        data_pedido: datetime,
        endereco: str,
        situacao_aberto: bool = True,
    ):
        self.cliente = cliente
        self.data_hora = data_pedido
        self.endereco = endereco
        self.situacao_aberto = situacao_aberto
        self.status = StatusPedido.RECEBIDO
        self.itens = []

    @property
    def valor_total(self) -> float:
        return sum(item.valor_total for item in self.itens)

    def add_item(self, item: ItemPedido) -> None:
        self.itens.append(item)

    def avancar_status(self) -> "StatusPedido":
        self.status = self.status.proximo_estado()
        if self.status == StatusPedido.ENTREGUE:
            self.situacao_aberto = False
        return self.status

    def cancelar(self, motivo: str) -> None:
        if motivo_invalido(motivo):
            raise MotivoCancelamentoObrigatorioError()
        if self.status == StatusPedido.ENTREGUE:
            raise PedidoJaEntregueError()
        self.status = StatusPedido.CANCELADO
        self.cancelamento_motivo = motivo
        self.situacao_aberto = False

    def definir_forma_pagamento(self, forma_pagamento: "str | FormaPagamento") -> str:
        if self.status == StatusPedido.CANCELADO:
            raise PagamentoNaoPermitidoError()
        if isinstance(forma_pagamento, str):
            forma_pagamento = forma_pagamento.lower()
        try:
            self.forma_pagamento = FormaPagamento(forma_pagamento).value
            return self.forma_pagamento
        except ValueError as error:
            raise FormaPagamentoInvalidaError() from error

    def fechar_pedido(self) -> None:
        self.situacao_aberto = False


def motivo_invalido(motivo: str) -> bool:
    if not motivo:
        return True
    return not motivo.strip()


def forma_pagamento_invalida(forma_pagamento: str) -> bool:
    return forma_pagamento == "boleto"


class FormaPagamento(Enum):
    CARTAO = "cartao"
    DINHEIRO = "dinheiro"
    PIX = "pix"


class StatusPedido(Enum):
    A_CAMINHO = "a caminho"
    CANCELADO = "cancelado"
    EM_PREPARO = "em preparo"
    ENTREGUE = "entregue"
    PRONTO = "pronto"
    RECEBIDO = "recebido"

    def proximo_estado(self) -> "StatusPedido":
        proximo = PROXIMO_STATUS_PEDIDO.get(self)
        if not proximo:
            raise AttributeError(f"Estado sem próximo estado definido: {str(self)}")
        return proximo


PROXIMO_STATUS_PEDIDO = {
    StatusPedido.RECEBIDO: StatusPedido.EM_PREPARO,
    StatusPedido.EM_PREPARO: StatusPedido.PRONTO,
    StatusPedido.PRONTO: StatusPedido.A_CAMINHO,
    StatusPedido.A_CAMINHO: StatusPedido.ENTREGUE,
    StatusPedido.ENTREGUE: StatusPedido.ENTREGUE,
    StatusPedido.CANCELADO: StatusPedido.CANCELADO,
}


class FormaPagamentoInvalidaError(ValueError):
    pass


class MotivoCancelamentoObrigatorioError(ValueError):
    pass


class PagamentoNaoPermitidoError(Exception):
    pass


class PedidoJaEntregueError(Exception):
    pass
