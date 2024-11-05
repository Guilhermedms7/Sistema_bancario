# services/sistema_bancario.py

from models.cliente import Cliente
from models.agencia import Agencia
from models.conta import Conta

class SistemaBancario:
    def __init__(self):
        self.clientes = []
        self.agencias = []
        self.contas = []

    def cadastrar_cliente(self, nome, cpf):
        cliente = Cliente(nome, cpf)
        self.clientes.append(cliente)
        print(f"Cliente {nome} cadastrado com sucesso.")

    def alterar_cliente(self, cpf_antigo, novo_nome, novo_cpf):
        cliente = next((c for c in self.clientes if c.cpf == cpf_antigo), None)
        if cliente:
            cliente.nome = novo_nome
            cliente.cpf = novo_cpf
            print(f"Cliente {cpf_antigo} alterado com sucesso.")
        else:
            print("Cliente não encontrado.")

    def remover_cliente(self, cpf):
        cliente = next((c for c in self.clientes if c.cpf == cpf), None)
        if cliente:
            self.clientes.remove(cliente)
            print(f"Cliente {cpf} removido com sucesso.")
        else:
            print("Cliente não encontrado.")

    def cadastrar_agencia(self, numero, endereco):
        agencia = Agencia(numero, endereco)
        self.agencias.append(agencia)
        print(f"Agência {numero} cadastrada com sucesso.")

    def alterar_agencia(self, numero_antigo, novo_numero, novo_endereco):
        agencia = next((a for a in self.agencias if a.numero == numero_antigo), None)
        if agencia:
            agencia.numero = novo_numero
            agencia.endereco = novo_endereco
            print(f"Agência {numero_antigo} alterada com sucesso.")
        else:
            print("Agência não encontrada.")

    def remover_agencia(self, numero):
        agencia = next((a for a in self.agencias if a.numero == numero), None)
        if agencia:
            self.agencias.remove(agencia)
            print(f"Agência {numero} removida com sucesso.")
        else:
            print("Agência não encontrada.")

    def abrir_conta(self, nome_cliente, numero_agencia):
        cliente = next((c for c in self.clientes if c.nome == nome_cliente), None)
        agencia = next((a for a in self.agencias if a.numero == numero_agencia), None)
        if cliente and agencia:
            conta = Conta(cliente, agencia)
            self.contas.append(conta)
            print(f"Conta aberta com sucesso para {cliente.nome}.")
        else:
            print("Cliente ou agência não encontrado.")

    def consultar_saldo(self, nome_cliente, numero_agencia):
        conta = next((c for c in self.contas if c.cliente.nome == nome_cliente and c.agencia.numero == numero_agencia), None)
        if conta:
            saldo = conta.consultar_saldo()
            print(f"Saldo da conta de {nome_cliente}: R$ {saldo:.2f}")
        else:
            print("Conta não encontrada.")

    def depositar(self, nome_cliente, numero_agencia, valor):
        conta = next((c for c in self.contas if c.cliente.nome == nome_cliente and c.agencia.numero == numero_agencia), None)
        if conta:
            conta.depositar(valor)
        else:
            print("Conta não encontrada.")

    def sacar(self, nome_cliente, numero_agencia, valor):
        conta = next((c for c in self.contas if c.cliente.nome == nome_cliente and c.agencia.numero == numero_agencia), None)
        if conta:
            conta.sacar(valor)
        else:
            print("Conta não encontrada.")

    def consultar_extrato(self, nome_cliente, numero_agencia):
        conta = next((c for c in self.contas if c.cliente.nome == nome_cliente and c.agencia.numero == numero_agencia), None)
        if conta:
            extrato = conta.consultar_extrato()
            print(f"Extrato da conta de {nome_cliente}:")
            for movimento in extrato:
                print(movimento)
        else:
            print("Conta não encontrada.")
