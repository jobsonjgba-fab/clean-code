from collections import deque

from . import Cardapio, Cliente, FormaPagamento, Pedido, StatusPedido


class System:
    def __init__(self):
        self.cardapio: list[Cardapio] = []
        self.clientes: list[Cliente] = []
        self.pedidos_abertos: deque[Pedido] = deque()
        self.pedidos_fechados: list[Pedido] = []

    @property
    def primeiro_pedido(self) -> Pedido:
        if not self.pedidos_abertos:
            raise IndexError("Nenhum pedido registrado no sistema")
        return self.pedidos_abertos[0]

    def add_cliente(self, cliente: Cliente) -> None:
        self.clientes.append(cliente)

    def add_item_cardapio(self, prato: Cardapio) -> None:
        self.cardapio.append(prato)

    def add_pedido(self, pedido: Pedido) -> None:
        self.pedidos_abertos.append(pedido)

    def avancar_status_primeiro_pedido(self) -> StatusPedido:
        novo_estado = self.primeiro_pedido.avancar_status()
        if novo_estado == StatusPedido.ENTREGUE:
            self.processar_proximo_pedido(self.primeiro_pedido)
        return novo_estado

    def cancelar_primeiro_pedido(self, motivo: str) -> bool:
        self.primeiro_pedido.cancelar(motivo)
        self.processar_proximo_pedido(self.primeiro_pedido)
        return True

    def definir_forma_pagamento_primeiro_pedido(
        self, forma_pagamento: "str | FormaPagamento"
    ) -> str:
        return self.primeiro_pedido.definir_forma_pagamento(forma_pagamento)

    def listar_pedidos_abertos(self) -> list:
        return [(pedido, pedido.status) for pedido in self.pedidos_abertos]

    def mostrar_cardapio(self) -> str:
        return "\n".join(item.descricao for item in self.cardapio)

    def processar_proximo_pedido(self, pedido: "Pedido | None" = None) -> None:
        if not self.pedidos_abertos:
            return
        if not pedido:
            pedido = self.primeiro_pedido
        elif pedido not in self.pedidos_abertos:
            return
        self.pedidos_abertos.remove(pedido)
        pedido.fechar_pedido()
        self.pedidos_fechados.append(pedido)

    def remove_cliente_por_telefone(self, telefone: str) -> None:
        self.clientes = [
            cliente for cliente in self.clientes if cliente.telefone != telefone
        ]

    def search_cliente_por_nome(self, nome: str) -> "list[Cliente]":
        return [cliente for cliente in self.clientes if nome in cliente.nome]

    def search_cliente_por_telefone(self, telefone: str) -> "list[Cliente]":
        return [cliente for cliente in self.clientes if telefone == cliente.telefone]
