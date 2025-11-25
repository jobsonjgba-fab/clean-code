from collections import deque

from . import Cardapio, Cliente, Pedido


class System:
    def __init__(self):
        self.clientes: list[Cliente] = []
        self.pedidos_abertos: deque[Pedido] = deque()
        self.cardapio: list[Cardapio] = []

    def add_cliente(self, cliente: Cliente) -> None:
        self.clientes.append(cliente)

    def add_item_cardapio(self, prato: Cardapio) -> None:
        self.cardapio.append(prato)

    def add_pedido(self, pedido: Pedido) -> None:
        self.pedidos_abertos.append(pedido)

    def mostrar_cardapio(self) -> str:
        # TODO: discutir opção na apresentação
        # listagem_cardapio = ""
        # for index in range(len(self.cardapio)):
        #     if index + 1 == len(self.cardapio):
        #         listagem_cardapio += self.cardapio[index].descricao
        #     else:
        #         listagem_cardapio += self.cardapio[index].descricao + "\n"
        # return listagem_cardapio
        return "\n".join(item.descricao for item in self.cardapio)

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
