from datetime import datetime

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
        self.valor_total = 0
        self.itens = []

    def add_item(self, item: ItemPedido):
        self.itens.append(item)
        self.valor_total += item.opcao_menu.valor * item.quantidade


class FormaPagamento:
    pass


class StatusPedido:
    pass


class FormaPagamentoInvalidaError:
    pass


class MotivoCancelamentoObrigatorioError:
    pass


class PagamentoNaoPermitidoError:
    pass


class PedidoJaEntregueError:
    pass
