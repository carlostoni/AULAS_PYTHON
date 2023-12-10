<<<<<<< HEAD
from saque import Saque
from deposito import Deposito

class ContaBancaria:
    def __init__(self, saldo):
        self.saldo = saldo

    def depositar(self,valor):
        deposito =  Deposito(valor)
        saldo_atual = deposito.executar2(self.saldo)
        print(f'o deposito e {valor}, saldo atual é {self.saldo}')

    def sacar(self,valor):
        saque = Saque(valor)
        saldo_atual =  saque.executar(self.saldo)
        if saldo_atual is not None:
            self.saldo = saldo_atual
            print(f'saque {valor}, saldo atual - {self.saldo}')
        else:
            print('Saldo insufi')


if __name__ == '__main__':
    conta = ContaBancaria(20)
print('''
      Bem vindo
      qual operacao voce deseja fazer
      1 - saque
      2 - deposito 
      ''')

lang = input()
match lang:
        case "1":  
          valor_saque = float(input('digite o valor que deseja sacar:'))
          conta.sacar(valor_saque)
        
            
        case "2":
            valor_deposito = float(input('digite o valor que deseja depositar:'))
            conta.depositar(valor_deposito)


   
=======
from saque import Saque
from deposito import Deposito

class ContaBancaria:
    def __init__(self, saldo):
        self.saldo = saldo

    def depositar(self,valor):
        deposito =  Deposito(valor)
        saldo_atual = deposito.executar2(self.saldo)
        print(f'o deposito e {valor}, saldo atual é {self.saldo}')

    def sacar(self,valor):
        saque = Saque(valor)
        saldo_atual =  saque.executar(self.saldo)
        if saldo_atual is not None:
            self.saldo = saldo_atual
            print(f'saque {valor}, saldo atual - {self.saldo}')
        else:
            print('Saldo insufi')


if __name__ == '__main__':
    conta = ContaBancaria(20)
print('''
      Bem vindo
      qual operacao voce deseja fazer
      1 - saque
      2 - deposito 
      ''')

lang = input()
match lang:
        case "1":  
          valor_saque = float(input('digite o valor que deseja sacar:'))
          conta.sacar(valor_saque)
        
            
        case "2":
            valor_deposito = float(input('digite o valor que deseja depositar:'))
            conta.depositar(valor_deposito)


   
>>>>>>> 2dcac4952d542ed043f8b3e7cd3db907baa00a78
   