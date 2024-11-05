class Movimento:
    def __init__(self, tipo, valor):
        self.tipo = tipo  # 'entrada' ou 'saida'
        self.valor = valor

    def __str__(self):
        return f"{self.tipo.capitalize()}: R$ {self.valor:.2f}"
