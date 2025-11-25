class Cardapio:
    def __init__(self, descricao: str, valor: float):
        self.descricao = descricao
        self.valor = valor

    def __eq__(self, instance) -> bool:
        if not isinstance(instance, Cardapio):
            return False
        return self.descricao == instance.descricao and self.valor == instance.valor
