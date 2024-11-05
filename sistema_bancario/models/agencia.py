# models/agencia.py

class Agencia:
    def __init__(self, numero, endereco):
        self.numero = numero
        self.endereco = endereco

    def __str__(self):
        return f"Agência: {self.numero}, Endereço: {self.endereco}"
