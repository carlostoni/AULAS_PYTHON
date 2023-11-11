# Exercício 4: Crie uma classe chamada Conta_bancaria com um atributo saldo inicializado com 0. 
# Em seguida, crie métodos deposito e saque que atualizem o saldo. 
# Crie um objeto da classe ContaBancaria, faça um depósito e um saque, e imprima o saldo resultante.

class Conta_bancaria:
    def __init__(self, saldo = 0):
        self.saldo = saldo
    def deposito(self):
        saldo + deposito
        
    def saque(self):
        saldo - saque
    
    print('''
      Bem vindo
      qual operacao voce deseja fazer
      1 - saque
      2 - deposito 
      ''')

    lang = input()
    

    match lang:
        case "1":      
            valor = int(input('digite o valor que deseja sacar:'))
            sacar = Conta_bancaria(saldo - valor)
        case "2":
            valor = int(input('digite o valor que deseja depositar:'))
          