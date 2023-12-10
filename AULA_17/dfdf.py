class ContaBancaria:
    def __init__(self):
        # Inicializando sem saldo no início
        self.saldo = 0

    def deposito(self, valor):
        self.saldo += valor
        print(f"Depósito de {valor} realizado. Novo saldo: {self.saldo}")

    def saque(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de {valor} realizado. Novo saldo: {self.saldo}")
        else:
            print("Saldo insuficiente. Operação de saque não realizada.")

# Criando um objeto da classe ContaBancaria
minha_conta = ContaBancaria()

# Permitindo ao usuário escolher entre depósito e saque
opcao = input("Digite 'D' para depósito ou 'S' para saque: ")

if opcao.upper() == 'D':
    valor_deposito = float(input("Digite o valor do depósito: "))
    minha_conta.deposito(valor_deposito)
elif opcao.upper() == 'S':
    valor_saque = float(input("Digite o valor do saque: "))
    minha_conta.saque(valor_saque)
else:
    print("Opção inválida.")

# Salvando o valor do saldo após as operações
saldo_atual = minha_conta.saldo

# Imprimindo o saldo resultante
print(f"Saldo final: {saldo_atual}")
