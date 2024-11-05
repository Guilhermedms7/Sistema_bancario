# models/conta.py

from models.movimento import Movimento

class Conta:
    def __init__(self, cliente, agencia, saldo=0):
        self.cliente = cliente
        self.agencia = agencia
        self.saldo = saldo
        self.extrato = []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            movimento = Movimento('entrada', valor)
            self.extrato.append(movimento)
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Valor de depósito deve ser positivo.")

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            movimento = Movimento('saida', valor)
            self.extrato.append(movimento)
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Valor de saque inválido.")

    def consultar_saldo(self):
        return self.saldo

    def consultar_extrato(self):
        return self.extrato
