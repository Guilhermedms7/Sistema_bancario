# main.py

from services.sistema_bancario import SistemaBancario

def exibir_menu():
    print("\nMenu:")
    print("1. Cadastrar Cliente")
    print("2. Alterar Cliente")
    print("3. Remover Cliente")
    print("4. Cadastrar Agência")
    print("5. Alterar Agência")
    print("6. Remover Agência")
    print("7. Abrir Conta")
    print("8. Consultar Saldo")
    print("9. Depositar")
    print("10. Sacar")
    print("11. Consultar Extrato")
    print("0. Sair")

def main():
    sistema = SistemaBancario()
    
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Nome do Cliente: ")
            cpf = input("CPF do Cliente: ")
            sistema.cadastrar_cliente(nome, cpf)

        elif opcao == '2':
            cpf_antigo = input("CPF antigo do Cliente: ")
            novo_nome = input("Novo Nome do Cliente: ")
            novo_cpf = input("Novo CPF do Cliente: ")
            sistema.alterar_cliente(cpf_antigo, novo_nome, novo_cpf)

        elif opcao == '3':
            cpf = input("CPF do Cliente: ")
            sistema.remover_cliente(cpf)

        elif opcao == '4':
            numero = input("Número da Agência: ")
            endereco = input("Endereço da Agência: ")
            sistema.cadastrar_agencia(numero, endereco)

        elif opcao == '5':
            numero_antigo = input("Número antigo da Agência: ")
            novo_numero = input("Novo Número da Agência: ")
            novo_endereco = input("Novo Endereço da Agência: ")
            sistema.alterar_agencia(numero_antigo, novo_numero, novo_endereco)

        elif opcao == '6':
            numero = input("Número da Agência: ")
            sistema.remover_agencia(numero)

        elif opcao == '7':
            nome_cliente = input("Nome do Cliente: ")
            numero_agencia = input("Número da Agência: ")
            sistema.abrir_conta(nome_cliente, numero_agencia)

        elif opcao == '8':
            nome_cliente = input("Nome do Cliente: ")
            numero_agencia = input("Número da Agência: ")
            sistema.consultar_saldo(nome_cliente, numero_agencia)

        elif opcao == '9':
            nome_cliente = input("Nome do Cliente: ")
            numero_agencia = input("Número da Agência: ")
            valor = float(input("Valor para depósito: "))
            sistema.depositar(nome_cliente, numero_agencia, valor)

        elif opcao == '10':
            nome_cliente = input("Nome do Cliente: ")
            numero_agencia = input("Número da Agência: ")
            valor = float(input("Valor para saque: "))
            sistema.sacar(nome_cliente, numero_agencia, valor)

        elif opcao == '11':
            nome_cliente = input("Nome do Cliente: ")
            numero_agencia = input("Número da Agência: ")
            sistema.consultar_extrato(nome_cliente, numero_agencia)

        elif opcao == '0':
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
