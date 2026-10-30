# Sistema Bancário

Aplicação de linha de comando em Python para simular operações básicas de uma agência bancária.

## Funcionalidades

- Cadastro, consulta, alteração e remoção de clientes e agências
- Abertura e consulta de contas correntes e especiais
- Consulta de saldo e extrato
- Depósitos e saques

## Estrutura

- `sistema_bancario/main.py` — menu e interação pelo terminal
- `sistema_bancario/models/` — modelos de cliente, agência, conta e movimentação
- `sistema_bancario/services/` — regras das operações bancárias

## Executar

Com Python instalado, execute na raiz do repositório:

```bash
python sistema_bancario/main.py
```