# Exercício 4: Crie uma classe chamada Conta_bancaria com um atributo saldo inicializado com 0. 
# Em seguida, crie métodos deposito e saque que atualizem o saldo. 
# Crie um objeto da classe ContaBancaria, faça um depósito e um saque, e imprima o saldo resultante.

class Conta_bancaria:
    def __init__(self):
        self.saldo = 50
       
    def saque(self, valor):
        self.saldo -= valor
        print(f'O seu saldo é: {self.saldo} \nvalor disponivel para saque {valor}')

    def deposito(self, valor):
        self.saldo += valor
        print(f'O seu saldo é: {self.saldo} \nvalor a ser depositado: {valor}')   
        
minha_conta = Conta_bancaria()
print('''
      Bem vindo
      qual operacao voce deseja fazer
      1 - saque
      2 - deposito 
      ''')

lang = input()
match lang:
        case "1":
          valor_saque = int(input('digite o valor que deseja sacar:'))
          minha_conta.saque(valor_saque)
        
            
        case "2":
            valor = int(input('digite o valor que deseja depositar:'))
            minha_conta.deposito(valor)

saldo_atual = minha_conta.saldo          
print(f"Saldo final: {saldo_atual}")    
