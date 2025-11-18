from . import Cliente


class System:
    def __init__(self):
        self.clientes: list[Cliente] = []

    def add_cliente(self, cliente: Cliente) -> None:
        self.clientes.append(cliente)
