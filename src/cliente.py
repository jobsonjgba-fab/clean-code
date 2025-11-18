class Cliente:
    def __init__(self, nome: str, telefone: str, email: str):
        self.nome = nome
        self.telefone = telefone
        self.email = email

    def __eq__(self, instance) -> bool:
        if not isinstance(instance, Cliente):
            return False
        return (
            self.nome == instance.nome
            and self.telefone == instance.telefone
            and self.email == instance.email
        )
