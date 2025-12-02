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
        self.valor_total = 0
        self.itens = []

    def add_item(self, item: ItemPedido):
        self.itens.append(item)
        self.valor_total += item.valor_total

    def avancar_status(self) -> None:
        self.status = self.status.proximo_estado()
        if self.status == StatusPedido.ENTREGUE:
            self.situacao_aberto = False


class FormaPagamento:
    pass


class StatusPedido(Enum):
    A_CAMINHO = 'a caminho'
    EM_PREPARO = 'em preparo'
    ENTREGUE = 'entregue'
    PRONTO = 'pronto'
    RECEBIDO = 'recebido'

    def proximo_estado(self) -> "StatusPedido":
        proximo = PROXIMO_STATUS_PEDIDO.get(self, None)
        if not proximo:
            raise AttributeError(f"Estado sem próximo estado definido: {str(self)}")
        return proximo


PROXIMO_STATUS_PEDIDO = {
    StatusPedido.RECEBIDO: StatusPedido.EM_PREPARO,
    StatusPedido.EM_PREPARO: StatusPedido.PRONTO,
    StatusPedido.PRONTO: StatusPedido.A_CAMINHO,
    StatusPedido.A_CAMINHO: StatusPedido.ENTREGUE,
    StatusPedido.ENTREGUE: StatusPedido.ENTREGUE,
}


class FormaPagamentoInvalidaError:
    pass


class MotivoCancelamentoObrigatorioError:
    pass


class PagamentoNaoPermitidoError:
    pass


class PedidoJaEntregueError:
    pass
