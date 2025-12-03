from collections import deque

from . import Cardapio, Cliente, Pedido, StatusPedido


class System:
    def __init__(self):
        self.cardapio: list[Cardapio] = []
        self.clientes: list[Cliente] = []
        self.pedidos_abertos: deque[Pedido] = deque()
        self.pedidos_fechados = []

    def add_cliente(self, cliente: Cliente) -> None:
        self.clientes.append(cliente)

    def add_item_cardapio(self, prato: Cardapio) -> None:
        self.cardapio.append(prato)

    def add_pedido(self, pedido: Pedido) -> None:
        self.pedidos_abertos.append(pedido)

    def avancar_status_primeiro_pedido(self) -> StatusPedido:
        primeiro_pedido = self.pedidos_abertos[0]
        novo_estado = primeiro_pedido.avancar_status()
        if novo_estado == StatusPedido.ENTREGUE:
            # TODO: reavaliar esta lógica, pois não está utilizando o primeiro_pedido
            self.processar_proximo_pedido()
        return primeiro_pedido.status

    def cancelar_primeiro_pedido(self, motivo: str) -> bool:
        primeiro_pedido = self.pedidos_abertos[0]
        primeiro_pedido.cancelar(motivo)
        self.processar_proximo_pedido()
        return True

    def listar_pedidos_abertos(self) -> list:
        return list(
            (pedido, pedido.status)
            for pedido
            in self.pedidos_abertos
        )

    def mostrar_cardapio(self) -> str:
        # TODO: discutir opção na apresentação
        # listagem_cardapio = ""
        # for index in range(len(self.cardapio)):
        #     if index + 1 == len(self.cardapio):
        #         listagem_cardapio += self.cardapio[index].descricao
        #     else:
        #         listagem_cardapio += self.cardapio[index].descricao + "\n"
        # return listagem_cardapio
        # TODO: outra alternativa:
        # return "\n".join(map(lambda x: x.descricao, self.cardapio))
        return "\n".join(item.descricao for item in self.cardapio)

    def processar_proximo_pedido(self) -> None:
        if not self.pedidos_abertos:
            return
        pedido = self.pedidos_abertos.popleft()
        pedido.fechar_pedido()
        self.pedidos_fechados.append(pedido)

    def remove_cliente_por_telefone(self, telefone: str) -> None:
        """
        Filtra a lista de clientes, deixando permanecer apenas
        aqueles que não possuam o telefone informado
        """
        # TODO: discutir as alternativas abaixo com os demais grupos
        #
        # clientes_que_permanecem = lambda cliente: cliente.telefone != telefone
        # self.clientes = list(filter(clientes_que_permanecem, self.clientes))

        nova_lista_clientes: list[Cliente] = []
        for cliente in self.clientes:
            if cliente.telefone != telefone:
                nova_lista_clientes.append(cliente)
        self.clientes = nova_lista_clientes

    def search_cliente_por_nome(self, nome: str) -> "list[Cliente]":
        """
        Encontra todos os clientes por nome 'parcial'
        """
        clientes_encontrados: list[Cliente] = []
        for cliente in self.clientes:
            if nome in cliente.nome:
                clientes_encontrados.append(cliente)
        return clientes_encontrados

    def search_cliente_por_telefone(self, telefone: str) -> "list[Cliente]":
        """
        Encontra todos os clientes por telefone 'exato'
        """
        clientes_encontrados: list[Cliente] = []
        for cliente in self.clientes:
            if cliente.telefone == telefone:
                clientes_encontrados.append(cliente)
        return clientes_encontrados
