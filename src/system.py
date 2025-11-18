from . import Cliente


class System:
    def __init__(self):
        self.clientes: list[Cliente] = []

    def add_cliente(self, cliente: Cliente) -> None:
        self.clientes.append(cliente)

    def remove_cliente_por_telefone(self, telefone: str) -> None:
        """
        Filtra a lista de clientes, deixando permanecer apenas
        aqueles que não possuam o telefone informado
        """
        # clientes_que_permanecem = lambda cliente: cliente.telefone != telefone
        # self.clientes = list(filter(clientes_que_permanecem, self.clientes))

        nova_lista_clientes: list[Cliente] = []
        for cliente in self.clientes:
            if cliente.telefone != telefone:
                nova_lista_clientes.append(cliente)
        self.clientes = nova_lista_clientes
